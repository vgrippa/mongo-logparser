# Example usage:
# file_path = 'path/to/your/file.json'
# json_reader = JSONFileHandler(file_path)
# json_data = json_reader.read_file()
# print(json_data)

import json

class JSONFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

