import datetime
from homework_04.MediaFile import MediaFile

class Cloud(MediaFile):

    def __init__(self, bucket, file_id, created_at):
        self.bucket = bucket
        super().__init__(file_id, created_at)

    def read(self):
        if not self.exists():
            raise FileNotFoundError("Файл не найден")
        return open(self.bucket, "r")

    def write(self, data: bytes):
        open(self.bucket, 'wb').write(data)
        self.updated_at = datetime.datetime.now()

    def delete(self):
        if self.exists():
            self.bucket.unlink()

    def exists(self) -> bool:
        return self.bucket.exists()