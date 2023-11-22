import os
import json
import pathlib
import pandas as pd


class SaveFiles():
    
    mainPath = None
    file_name_json = None
    file_name_csv = None
    
    def __init__(self, data: dict, file_name: str):
        self.data = data
        self.file_name_json = file_name + '.json'
        self.file_name_csv = file_name + '.csv'
        
        self.mainPath = str(pathlib.Path().absolute()) + '/Files'
        
        if os.path.exists(self.mainPath) == False:
            os.mkdir(self.mainPath)
        
    def saveJSON(self):
        filePath = self.mainPath + '/' + self.file_name_json
        with open(filePath, 'w') as file:
            json.dump(self.data, file)

    def saveCSV(self):
        filePath = self.mainPath + '/' + self.file_name_csv
        with open(filePath, 'w') as file:
            json.dump(self.data, file)