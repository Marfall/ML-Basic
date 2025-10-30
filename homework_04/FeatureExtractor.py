from homework_04.MediaFile import MediaFile

# Экстрактор фич из медиа-файлов
class FeatureExtractor:
    def extract(self, file: MediaFile) :
        print(f"Извлекаем фичи из {file.file_id}")
        return file.features