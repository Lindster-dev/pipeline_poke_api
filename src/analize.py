import logging
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Analyze:
    """Classe responsável por análises e geração de relatórios."""

    def __init__(self, logger: logging.Logger = None):
        self.logger = logger or logging.getLogger(__name__)

    def generate_top5_pokemon_csv(self, top5: pd.DataFrame):
        """
        Gera um relatório CSV consolidado contendo:
        - Verifica se existe a pasta "datas / reports" e cria se nao existir
        - Salva o relatório em "datas / reports / relatorio_pokemon_top5.csv"
        - Top 5 Pokémon por experiência base
        - Média de HP, Ataque e Defesa por tipo
        """
        try:
            file_name = "relatorio_pokemon_top5.csv"
            reports_dir = Path("datas") / "reports"
            reports_dir.mkdir(parents=True, exist_ok=True)
            file_path = reports_dir / file_name
            top5.to_csv(file_path, index=False, encoding="utf-8")
        except Exception as e:
            self.logger.error(f"Erro ao salvar o CSV: {e}")
        self.logger.info(f"CSV salvo em {file_path}")

    def generate_stats_csv(self, stats: pd.DataFrame) -> Path:
        """
        Gera um relatório CSV contendo:
        - Verifica se existe a pasta "datas/reports" e cria se não existir
        - Salva o relatório em "datas/reports/relatorio_pokemon_stats.csv"
        - Média de HP, Ataque e Defesa por tipo
        """
        file_name = "relatorio_pokemon_stats.csv"
        reports_dir = Path("datas") / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        file_path = reports_dir / file_name
        try:
            stats.to_csv(file_path, index=False, encoding="utf-8")
            self.logger.info(f"CSV de estatísticas salvo em {file_path}")
        except Exception as e:
            self.logger.error(f"Erro ao salvar o CSV de estatísticas: {e}")
        return file_path

    def plot_distribution_by_type_pokemon(self, df: pd.DataFrame):
        """
        Gera e salva um gráfico de distribuição de Pokémon por tipo
        dentro da pasta datas/reports/.
        - Verifica se a pasta "datas / reports" e cria se nao existir
        - Salva o gráfico em "datas / reports / distribuicao_por_tipo_pokemon.png"
        """
        filename: str = "distribuicao_por_tipo_pokemon.png"
        reports_dir = Path("datas") / "reports"
        reports_dir.mkdir(parents=True, exist_ok=True)
        file_path = reports_dir / filename
        df_exploded = df.explode("Tipos")
        try:
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
            self.logger.info(f"Gráfico salvo em {file_path}")
        except Exception as e:
            self.logger.error(f"Erro ao gerar gráfico: {str(e)}")

    def generate_report(
        self, df: pd.DataFrame, top5: pd.DataFrame, stats: pd.DataFrame
    ):
        """
        Gera o relatório completo (CSV + gráfico).
        """
        self.generate_top5_pokemon_csv(top5)
        self.generate_stats_csv(stats)
        self.plot_distribution_by_type_pokemon(df)
        self.logger.info("Relatório completo gerado com sucesso")
