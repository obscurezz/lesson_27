import json
from csv import DictReader


class CsvToJson:
    def __init__(self, csv_file_path: str, json_file_path: str) -> None:
        self.csv = csv_file_path
        self.json = json_file_path

    def decode_csv_to_list(self) -> list:
        with open(self.csv, 'r', encoding='utf-8') as csv_file:
            csv_reader: DictReader = DictReader(csv_file)
            csv_list: list = [row for row in csv_reader]

        return csv_list

    def decode_list_to_json(self) -> None:
        with open(self.json, 'w', encoding='utf-8') as json_file:
            json_dump = json.dumps(self.decode_csv_to_list(), indent=4, ensure_ascii=False)
            json_file.write(json_dump)


ads_file = r'datasets/ads.json'
categories_file = r'datasets/categories.json'

ads = CsvToJson('datasets/ads.csv', ads_file)
ads.decode_list_to_json()

categories = CsvToJson('datasets/categories.csv', categories_file)
categories.decode_list_to_json()
