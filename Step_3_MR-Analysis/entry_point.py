import json
import os
from parser.mr_analysis_parser import FileParser


if __name__ == '__main__':
  
  import click
  
  @click.command()
  @click.option('-i', '--file', 'root_file_path', help = 'Root file path')
  
  def main(root_file_path):
    
    print(root_file_path.split('_logs'))
    with open(root_file_path) as f:
      data = json.load(f)
    
    FileParser(root_file_path).get_td()
    
    # print(data)
    
main()