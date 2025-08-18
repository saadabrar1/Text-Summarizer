import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any, Callable
import inspect


# Custom replacement for ensure_annotations
def ensure_annotations(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        for name, value in bound.arguments.items():
            if name in func.__annotations__:
                expected_type = func.__annotations__[name]
                # Skip if annotation is 'Any'
                if expected_type is not Any and not isinstance(value, expected_type):
                    raise TypeError(
                        f"Argument '{name}' must be {expected_type}, got {type(value)}"
                    )
        return func(*args, **kwargs)
    return wrapper


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"
