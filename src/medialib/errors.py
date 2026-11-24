class MediaLibError(Exception):
    "Родительский класс всех ошибок модуля medialib"


class UnsupportedFormatError(MediaLibError):
    "Неподдерживаемый формат файла"
    def __init__(self, format):
        super().__init__(f"Unsupported format: {format}")