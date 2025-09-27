import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Transform:
    """Classe responsável por transformar os dados extraídos da PokeAPI."""

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def add_category(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Adiciona uma coluna 'Categoria' baseada na experiência base do Pokémon:
        - < 50 → Fraco
        - 50–100 → Médio
        - > 100 → Forte
        """
        df["Categoria"] = df["Experiência Base"].apply(
            lambda exp: "Fraco" if exp < 50 else "Médio" if exp <= 100 else "Forte"
        )
        return df

    def stats_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula a média de HP, Ataque e Defesa por tipo de Pokémon.
        """
        return (
            df.explode("Tipos")
            .groupby("Tipos")[["HP", "Ataque", "Defesa"]]
            .mean()
            .reset_index().round(2)
        )

    def pokemon_count_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Conta a quantidade de Pokémon por tipo.
        """
        return (
            df.explode("Tipos")
            .groupby("Tipos")
            .size()
            .reset_index(name="Quantidade")
        )
    
    def top5_by_experience(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Retorna os 5 Pokémon com maior experiência base.
        """
        return df.nlargest(5, "Experiência Base")[["ID", "Nome", "Experiência Base"]]

    def process_transform_data_pokemon(self, df: pd.DataFrame):
        """
        Executa todas as transformações:
        - Top 5 por experiência
        - Categorias por experiência
        - Estatísticas médias por tipo
        - Contagem por tipo
        """
        df_top5_by_experience = self.top5_by_experience(df)
        df_category_pokemon = self.add_category(df)
        df_type_pokemon = self.stats_by_type(df)
        print(df_type_pokemon)
        df_count_by_type_pokemon = self.pokemon_count_by_type(df)
        return df_top5_by_experience, df_category_pokemon, df_type_pokemon, df_count_by_type_pokemon
