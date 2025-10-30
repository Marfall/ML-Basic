import datetime

class MediaFile:
    def __init__(self, file_id, features):
        self.file_id = file_id
        self.features = features
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()


    def read(self):
        print("Чтение файла")
        pass

    def write(self, data):
        print("Запись в файл")
        pass

    def delete(self):
        print("Удаление файла")
        pass