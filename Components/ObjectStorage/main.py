import os
import hashlib


class ObjectStore:
    def __init__(self, storage_directory):
        self.storage_directory = storage_directory

    def put(self, data):
        filename = hashlib.md5(data).hexdigest()
        with open(os.path.join(self.storage_directory, filename), "wb") as f:
            f.write(data)
        return filename

    def get(self, filename):
        with open(os.path.join(self.storage_directory, filename), "rb") as f:
            data = f.read()
        return data


object_store = ObjectStore("/")
data = b"This is some test data"
filename = object_store.put(data)
retrieved_data = object_store.get(filename)
print(retrieved_data)
