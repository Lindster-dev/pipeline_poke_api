import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Analyze:
    """Class responsible for analysis and report generation."""

    def __init__(self, logger: logging.Logger = None):
        self.logger = logger or logging.getLogger(__name__)

    def generate_top5_pokemon_csv(self, df_top5_by_experience: pd.DataFrame):
        """
        Generate a consolidated CSV report containing:
        - Ensures the folder "data/reports" exists, creating it if necessary
        - Saves the report to "data/reports/pokemon_top5.csv"
        - Top 5 Pokémon by base experience
        """
        try:
            file_name = "relatorio_pokemon_top5.csv"
            reports_dir = Path("data") / "reports"
            reports_dir.mkdir(parents=True, exist_ok=True)
            file_path = reports_dir / file_name
            df_top5_by_experience.to_csv(file_path, index=False, encoding="utf-8")
            self.logger.info(f"Top 5 Pokémon CSV saved at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to save Top 5 Pokémon CSV: {e}")

    def generate_stats_csv(self, df_stats_by_type: pd.DataFrame) -> Path:
        """
        Generate a CSV report containing:
        - Ensures the folder "data/reports" exists, creating it if necessary
        - Saves the report to "data/reports/pokemon_stats.csv"
        - Average HP, Attack, and Defense by type
        """
        try:
            file_name = "relatorio_pokemon_stats.csv"
            reports_dir = Path("data") / "reports"
            reports_dir.mkdir(parents=True, exist_ok=True)
            file_path = reports_dir / file_name
            df_stats_by_type.to_csv(file_path, index=False, encoding="utf-8")
            self.logger.info(f"Stats CSV saved at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to save Stats CSV: {e}")
        return file_path

    def plot_distribution_by_type_pokemon(self, df_data_pokemon: pd.DataFrame):
        """
        Generate and save a distribution chart of Pokémon by type
        inside the folder data/reports/.
        - Ensures the folder "data/reports" exists, creating it if necessary
        - Saves the chart to "data/reports/pokemon_distribution_by_type.png"
        """
        try:
            filename: str = "distribuicao_por_tipo_pokemon.png"
            reports_dir = Path("data") / "reports"
            reports_dir.mkdir(parents=True, exist_ok=True)
            file_path = reports_dir / filename
            df_exploded = df_data_pokemon.explode("Tipos")
            plt.figure(figsize=(10, 6))
            sns.countplot(
                data=df_exploded,
                x="Tipos",
                order=df_exploded["Tipos"].value_counts().index,
                palette="viridis",
            )
            plt.title("Distribuição de Pokémon por Tipo")
            plt.xlabel("Tipo do Pokémon")
            plt.ylabel("Quantidade de Pokémon")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(file_path)
            plt.close()
            self.logger.info(f"Distribution chart saved at {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to generate distribution chart: {e}")

    def generate_report(
        self, df_data_pokemon: pd.DataFrame, df_top5_by_experience : pd.DataFrame, df_stats_by_type: pd.DataFrame
    ):
        """
        Generate the full report (CSV + chart).
        """
        self.generate_top5_pokemon_csv(df_top5_by_experience)
        self.generate_stats_csv(df_stats_by_type)
        self.plot_distribution_by_type_pokemon(df_data_pokemon)
        self.logger.info("Full report successfully generated")
