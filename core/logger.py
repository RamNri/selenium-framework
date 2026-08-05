import logging
from pathlib import Path


def configure_logging():
    """
    Configure logging for the entire framework.
    Creates artifacts/logs/execution.log.
    """
    log_folder = Path("artifacts") / "logs"
    log_folder.mkdir(parents=True, exist_ok=True)

    log_file = log_folder / "execution.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, mode="w"),
            logging.StreamHandler(),
        ],
        force=True,
    )
    return logging.getLogger()


__all__ = ["configure_logging"]
