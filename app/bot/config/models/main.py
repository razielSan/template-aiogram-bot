from pathlib import Path
from bot.config.models.example import ExampleModels, MusicModels

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseGeneration(BaseSettings):
    """Общий класс для генерации моделей."""

    music_models: MusicModels = MusicModels()
    example_models: ExampleModels = ExampleModels()

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent.parent / ".env",
        extra="ignore",
        env_nested_delimiter="__",
    )
