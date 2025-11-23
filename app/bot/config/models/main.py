from pathlib import Path
from bot.config.models.example import ExampleModels

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseGeneration(BaseSettings):
    """Общий класс для генерации моделей."""
    
    example_models: ExampleModels = ExampleModels()

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        extra="ignore",
        env_nested_delimiter="__",
    )
