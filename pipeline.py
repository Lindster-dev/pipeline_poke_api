import logging

from src import Analyze, Extractor, Transform

logger = logging.getLogger(__name__)


def run_pipeline():
    try:
        extractor = Extractor(logger)
        transformer = Transform(logger)
        analyzer = Analyze(logger)
        df = extractor.process_extractor(limit=100, offset=0)
        if df is None:
            logger.error("Failed to fetch data from PokeAPI")
            return
        (
            df_top5_by_experience,
            df_category_pokemon,
            df_stats_by_type,
            df_count_by_type,
        ) = transformer.process_transform_data_pokemon(df)
        analyzer.generate_report(
            df=df,
            top5=df_top5_by_experience,
            stats=df_stats_by_type,
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    run_pipeline()
