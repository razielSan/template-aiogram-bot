from typing import Optional

from pydantic import BaseModel

from bot.config.models.filed import FieldGeneration


class Example(FieldGeneration, BaseModel):
    SERVICE_NAME: str = "Example"
    SERVICE_ID: str = "example"

    # Данные кнопок
    TEXT_PREFIX: str = "=)"
    CALLBACK_PREFIX: str = "example"
    
    API_KEY: Optional[str] = None


class ExampleModels(BaseModel):
    example: Example = Example()