from homework_04.MediaFile import MediaFile

# Конвертер медиа-файлов
class MediaConverter:
    def __init__(self, target_format):
        self.target_format = target_format

    def convert(self, media_file: MediaFile) -> MediaFile:
        print(f"Конвертируем {media_file.file_id} в {self.target_format}")
        return media_file