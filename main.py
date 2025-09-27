import logging
from datetime import datetime

from src import Analyze, Extractor, Transform

log_filename = f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_filename, encoding="utf-8"),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)

def main() -> bool:
    try:
        extractor = Extractor(logger)
        transformer = Transform(logger)
        analyzer = Analyze(logger)
        df = extractor.process_extractor(limit=100, offset=0)
        if df is None:
            logger.error("Failed to fetch data from PokeAPI")
            return False
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
        return True
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    main()
    