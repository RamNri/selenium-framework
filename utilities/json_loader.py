import json
from pathlib import Path

class JsonLoader:

  _cache ={}

  @classmethod
  def load(cls, path):

    if path not in cls._cache:
       with open(path,  "r", encoding="utf-8") as file:
         cls._cache[path] = json.load(file)
    return cls._cache[path]