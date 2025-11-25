from typing import Optional

from pydantic import BaseModel

from bot.config.models.filed import FieldGeneration


# Пример 1
class Example(FieldGeneration, BaseModel):
    SERVICE_NAME: str = "Example"
    SERVICE_ID: str = "example"

    # Данные кнопок
    TEXT_PREFIX: str = "=)"
    CALLBACK_PREFIX: str = "example"

    API_KEY: Optional[str] = None


class ExampleModels(BaseModel):
    example: Example = Example()



# Пример 2
class ExampleMusic(BaseModel):
    """Модель для примера."""

    SERVICE_NAME: str = "Example_Music"
    SERVICE_ID: str = "example_music"


class NewMusicItemsModels(BaseModel):
    """Модель содержащая другие модели по поиску музыкальных новинок."""

    SERVICE_NAME: str = "New_Music"
    SERVICE_ID: str = "new_music"

    # Данные кнопок для подлкючаемых моделей
    CALLBACK_BUTTON_TEXT_EXAMPLE_MUSIC: str = "1⃣ example_music"
    CALLBACK_BUTTON_DATA_EXAMPLE_MUSIC: str = "new_music example_music"

    example_music: ExampleMusic = ExampleMusic()


class MusicModels(BaseModel):
    """Общий класс для генерации музакальных моделей."""

    SERVICE_NAME: str = "Music"
    SERVICE_ID: str = "music"

    # Данные кнопок для подлключаемых моделей
    CALLBACK_BUTTON_TEXT_NEW_MUSIC: str = "🎻 Музыкальные новинки"
    CALLBACK_BUTTON_DATA_NEW_MUSIC: str = "music new_music"
    START_BOT_MENU_REPLY_TEXT: str = "🎧 Mузыка"

    new_music: NewMusicItemsModels = NewMusicItemsModels()
