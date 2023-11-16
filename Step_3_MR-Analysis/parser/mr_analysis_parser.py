import os
import json
import tempfile

class FileParser():
    
    id: str | None
    data: dict | None
    
    def __init__(self, id: str, data: dict) -> None:
        
        self.id = id
        self.data = data

            
    def get_td(self):
        
        for i in range(0,len(self.data)):
            # print('*****', i)
            print(type(self.data[str(i)]))
    
def _get_additional_attributes(td, index):
        
    self.data[index] = 