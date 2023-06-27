# main.py
from json_file_handler import JSONFileHandler


json_reader = JSONFileHandler( sys.argv[0])
json_data = json_reader.read_file()

for line in json_data:
    print(line)
