import requests
import logging
import pandas as pd


class Extractor:
    """Classe responsável por extrair dados da PokeAPI."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def get_pokemon_list(self, limit: int = 100, offset: int = 0) -> list[dict] | None:
        """
        Retorna a lista de Pokémon com base em limite e offset.
        """
        url_https = "https://pokeapi.co/api/v2/"
        url = f"{url_https}/pokemon?limit={limit}&offset={offset}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get("results", [])
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch Pokémon list: {e}")
            return None
        
    def get_pokemon_details(self, pokemon_url: str) -> dict:
        """
        Retorna os detalhes de um Pokémon específico a partir da URL.
        """
        try:
            pokemon_id = pokemon_url.split("/")[-2]
            url_details = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
            response = requests.get(url_details, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch Pokémon details: {e}")
            return {}
   
    def parse_pokemon(self, detils_pokemon: dict) -> dict:
        """
        Converte o JSON de detalhes do Pokémon em um dicionário simplificado.
        """
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in detils_pokemon["stats"]}
        return {
            "ID": detils_pokemon["id"],
            "Nome": detils_pokemon["name"].capitalize(),
            "Experiência Base": detils_pokemon.get("base_experience", 0),
            "Tipos": [t["type"]["name"].capitalize() for t in detils_pokemon["types"]],
            "HP": stats.get("hp"),
            "Ataque": stats.get("attack"),
            "Defesa": stats.get("defense")
        }
        
    def process_extractor(self, limit: int, offset: int) -> pd.DataFrame | None:
        """
        Orquestra a extração: busca a lista de Pokémon, coleta os detalhes
        e retorna um DataFrame consolidado.
        """
        pokemon_list = self.get_pokemon_list(limit, offset)
        if not pokemon_list:
            return None
        all_pokemons = []
        for pokemon in pokemon_list:
            details = self.get_pokemon_details(pokemon.get("url"))
            if details:
                parsed = self.parse_pokemon(details)
                all_pokemons.append(parsed)
        return pd.DataFrame(all_pokemons)
