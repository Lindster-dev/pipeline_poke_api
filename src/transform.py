import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Transform:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def add_category(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add a 'Category' column based on the Pokémon's base experience:
        - < 50 → Weak
        - 50–100 → Medium
        - > 100 → Strong
        """
        try:
            df["Categoria"] = df["Experiência Base"].apply(
                lambda exp: "Fraco" if exp < 50 else "Médio" if exp <= 100 else "Forte"
            )
            return df
        except Exception as e:
            self.logger.error(f"Failed to add 'Category' column: {e}")
            return None

    def stats_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate the average HP, Attack, and Defense by Pokémon type.
        """
        try:
            return (
                df.explode("Tipos")
                .groupby("Tipos")[["HP", "Ataque", "Defesa"]]
                .mean()
                .reset_index().round(2)
            )
        except Exception as e:
            self.logger.error(f"Failed to calculate stats by type: {e}")
            return None
        
    def pokemon_count_by_type(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Count the number of Pokémon per type.
        """
        try:
            return (
                df.explode("Tipos")
                .groupby("Tipos")
                .size()
                .reset_index(name="Quantidade")
            )
        except Exception as e:
            self.logger.error(f"Failed to count Pokémon by type: {e}")
            return None
        
    def top5_by_experience(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Return the Top 5 Pokémon with the highest base experience.
        """
        try:
            df_top5_by_experience = df.nlargest(5, "Experiência Base")[["ID", "Nome", "Experiência Base"]]
            self.logger.info("Top 5 Pokémon com maior experiência")
            return df_top5_by_experience
        except Exception as e:
            self.logger.error(f"Failed to get Top 5 Pokémon by base experience: {e}")
            return None

    def process_transform_data_pokemon(self, df: pd.DataFrame):
        """
        Execute all transformations:
        - Top 5 by base experience
        - Category by experience
        - Average stats by type
        - Count by type
        """
        df_top5_by_experience = self.top5_by_experience(df)
        df_category_pokemon = self.add_category(df)
        df_type_pokemon = self.stats_by_type(df)
        df_count_by_type_pokemon = self.pokemon_count_by_type(df)
        return df_top5_by_experience, df_category_pokemon, df_type_pokemon, df_count_by_type_pokemon
