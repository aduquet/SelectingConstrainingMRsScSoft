import os
import json
from parser.mr_analysis_parser import FileParser
from save_files import SaveFiles

if __name__ == '__main__':
  
  import click
  
  @click.command()
  @click.option('-i', '--file', 'root_file_path', help = 'Root file path')
  
  def main(root_file_path):
    
    print(root_file_path.split('_logs'))
    with open(root_file_path) as f:
      data = json.load(f)
    
    data_procesed = FileParser(data=data).get_td()
    
    SaveFiles(data=data_procesed, file_name='hale').saveJSON()
    # print(data)
    
main()