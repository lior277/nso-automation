import json, importlib.resources as res
from jsonschema import validate

def load_schema(name: str) -> dict:
    with res.files("resources.schemas").joinpath(name).open("r", encoding="utf-8") as f:
        return json.load(f)

def assert_valid(instance: dict, schema_name: str) -> None:
    schema = load_schema(schema_name)
    validate(instance=instance, schema=schema)
