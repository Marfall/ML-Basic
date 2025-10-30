import datetime
from pathlib import Path

from homework_04.MediaFile import MediaFile

# Локальный медиа-файл
class LocalMediaFile(MediaFile):

    def __init__(self, file_path, file_id, created_at):
        self.file_path = Path(file_path)
        super().__init__(file_id, created_at)

    def read(self):
        if not self.exists():
            raise FileNotFoundError("Файл не найден")
        return open(self.file_path, "r")

    def write(self, data: bytes):
        open(self.file_path, 'wb').write(data)
        self.updated_at = datetime.datetime.now()

    def delete(self):
        if self.exists():
            self.file_path.unlink()

    def exists(self) -> bool:
        return self.file_path.exists()
