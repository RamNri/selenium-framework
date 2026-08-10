import json
from pathlib import Path
import pytest
from core.exceptions import JsonLoadException
from utilities.json_loader import JsonLoader

class TestJsonLoader:

  def setup_method(self):
    JsonLoader._cache.clear()

  def test_load_valid_json(self, tmp_path):
    json_file = tmp_path / "booking.json"
    json_file.write_text(json.dumps(
      {
        "name" : "Test"
      }
    ))
    data = JsonLoader.load(json_file)
    assert data["name"] == "Test"
  
  def test_missing_file_raises_exeception(self):
    with pytest.raises(JsonLoadException):
      JsonLoader.load(Path("does_not_exist.json"))
  
  def test_invalid_json_raises_exception(self, tmp_path):
    json_file = tmp_path/"invalid.json"

    json_file.write_text("invalid json")
    with pytest.raises(JsonLoadException):
      JsonLoader.load(json_file)
