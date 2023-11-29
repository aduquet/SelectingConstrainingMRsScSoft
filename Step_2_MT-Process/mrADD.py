import math
import traceback
import pandas as pd

def _ttd(td, const):
    ttdAux = []
    if isinstance(td, list):
        for item in td:
            ttdAux.append(item + const)
        return ttdAux
    
    if isinstance(td, int):
        return td + const

class MR_ADD:
    def __init__(self, *args):
        # Constructor for MR_ADD class
        
        # Store the input arguments as tdArgs
        self.tdArgs = args
        
        # Initialize const to None
        self.const = None
        
        # Lists to store column names for td and ttd
        self.keyNames_td = []
        self.keyNames_ttd = []
        
        # Lists to store the results of _ttd for td and ttd
        self.ttd = []
        self.td = []

    def followUP(self, const):
        # Method to perform follow-up calculations
        
        # Set the value of const
        self.const = const
        
        # Iterate through the input arguments
        for i, arg in enumerate(self.tdArgs):
            # Generate column names for td and ttd
            self.keyNames_td.append('td_' + str(i + 1))
            self.keyNames_ttd.append('ttd_' + str(i + 1))
            
            # Calculate and store the result of _ttd for td
            self.ttd.append(_ttd(td=arg, const=self.const))
            
            # Store the arg 
            self.td.append(arg) 
            
        # Create a DataFrame with columns for td
        self.df = pd.DataFrame(columns=self.keyNames_td)
        
        # Create a DataFrame with columns for ttd (Note: You should adjust this based on your requirements)
        df_aux = pd.DataFrame(columns=self.keyNames_ttd)
        
        # Insert the calculated values for td into the DataFrame
        self.df.loc[len(self.df)] = self.td
        
        # Insert the calculated values for ttd into the DataFrame (Note: You should adjust this based on your requirements)
        df_aux.loc[0] = self.ttd

        # Concatenate the two DataFrames horizontally
        result = pd.concat([self.df, df_aux], axis=1)

        return result
