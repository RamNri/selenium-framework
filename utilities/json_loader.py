import json
from pathlib import Path
from core.exceptions import JsonLoadException
import logging

logger = logging.getLogger(__name__)

class JsonLoader:

  _cache ={}

  @classmethod
  def load(cls, path: Path):
    if path in cls._cache:
      return cls._cache[path]
    
    try:

        if path not in cls._cache:
          with open(path,  "r", encoding="utf-8") as file:
            cls._cache[path] = json.load(file)
          return cls._cache[path]
    except FileNotFoundError as ex:
      logger.error("Unable to load JSON file %s", path,)
      raise JsonLoadException(
        f"JSON file not found: {path}"
      ) from ex
    
    except json.JSONDecodeError as ex:
      logger.error("Invalid JSON format in %s", path,)
      raise JsonLoadException(
        f"Invalid JSON format in file: {path}"
      ) from ex
    
    except OSError as ex:
      logger.error("Unable to read JSON file %s", path,)
      raise JsonLoadException(
        f"Unable to read JSON file: {path}"
      ) from ex