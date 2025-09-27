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
        try:
            df["Categoria"] = df["Experiência Base"].apply(
                lambda exp: "Fraco" if exp < 50 else "Médio" if exp <= 100 else "Forte"
            )
            return df
        except Exception as e:
            self.logger.error(f"Erro ao adicionar a coluna 'Categoria': {e}")
            return None

    def stats_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula a média de HP, Ataque e Defesa por tipo de Pokémon.
        """
        try:
            return (
                df.explode("Tipos")
                .groupby("Tipos")[["HP", "Ataque", "Defesa"]]
                .mean()
                .reset_index().round(2)
            )
        except Exception as e:
            self.logger.error(f"Erro ao calcular as médias: {e}")
            return None
        
    def pokemon_count_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Conta a quantidade de Pokémon por tipo.
        """
        try:
            return (
                df.explode("Tipos")
                .groupby("Tipos")
                .size()
                .reset_index(name="Quantidade")
            )
        except Exception as e:
            self.logger.error(f"Erro ao contar os Pokémon por tipo: {e}")
            return None
        
    def top5_by_experience(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Retorna os 5 Pokémon com maior experiência base.
        """
        try:
            df_top5_by_experience = df.nlargest(5, "Experiência Base")[["ID", "Nome", "Experiência Base"]]
            self.logger.info("Top 5 Pokémon com maior experiência")
            return df_top5_by_experience
        except Exception as e:
            self.logger.error(f"Erro ao converter a coluna 'Experiência Base': {e}")
            return None

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
        df_count_by_type_pokemon = self.pokemon_count_by_type(df)
        return df_top5_by_experience, df_category_pokemon, df_type_pokemon, df_count_by_type_pokemon
