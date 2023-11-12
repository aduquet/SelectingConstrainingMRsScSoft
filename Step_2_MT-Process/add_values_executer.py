from adapter.adapter_inputs import AdapterInputs
from mr_add_mt_process import MR_ADD
from mr_exc_mt_process import MR_EXC
from mr_inc_mt_process import MR_INC
from mr_inv_mt_process import MR_INV
from mr_mul_mt_process import MR_MUL
from mr_per_mt_process import MR_PER

import pandas as pd
from pathlib import Path
import pathlib
import json
import sys
import os

all_methods_path = Path(__file__).parent / '/Users/alduck/Documents/GitHub/AST2024-SelectingConstrainingMRsScSoft/AllMethods'

# Making sure the directory exists
if not all_methods_path.is_dir():
    raise ImportError(f"The directory {all_methods_path} does not exist")

# Add the parent directory of AllMethods to the Python path
sys.path.append(str(all_methods_path.parent))

from AllMethods.Group_1.add_values.src.add_values import add_values


def _get_ttd(input):
    
    return AdapterInputs(input).ttd_all_mrs(2)

def _get_td_output(td):    
    return add_values(td)

def _get_ttd_output(ttd):
    return add_values(ttd)

td_ttd = _get_ttd([1, 0])

print(_get_ttd([1, 0]))
# if __name__ == '__main__':
    
#     import click
    
#     global mainDF
#     mainDF = pd.DataFrame()
    
#     global auxList
#     auxList = []
    
#     @click.command()
#     @click.option('-i', '--input_path', 'input_path')
#     @click.option('-o', '--output_file', 'output_file')

#     def main(input_path, output_file):
        
#         mainPathMRChecker = str(pathlib.Path().absolute()) + '/' + 'Logs'

#         try:
#             os.mkdir(mainPathMRChecker)
#         except:
#             pass
        
#         with open(input_path, 'r') as readfiles:
#             inputs = json.load(readfiles)
#             json.dumps(inputs, indent=4)
            
#         for i in range(0, len(inputs)):

#             output = add_values(inputs[str(i)]['test_data'])
#             output_transformed = testDataTransformedExecution(inputs[str(i)]['MR2-ADD'])
#             mr = MTexecuterMRADD(output)
#             violationStatus = mr.mr_ADD(output_transformed)
            
#         #     mainDF = {
#         #         'id': inputs[str(i)]['id'],
#         #         'test_data': inputs[str(i)]['test_data'],
#         #         'test_data_transformed': inputs[str(i)]['MR2-ADD'],
#         #         'output': output,
#         #         'output_transformed': output_transformed,
#         #         'MR_Status': violationStatus
#         #     }
            
#         #     auxList.append(mainDF)
            
#         # final_df = pd.DataFrame(auxList)
        
#         # save_csv(final_df, output_file, mainPathMRChecker)
#         # save_json(final_df, output_file, mainPathMRChecker)
        
# main()
    