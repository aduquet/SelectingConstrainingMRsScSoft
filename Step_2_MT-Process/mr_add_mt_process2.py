import math
import traceback
from adapters.aux_class import is_valid_input

class MR_ADD:
    """
    MR_ADD tests a metamorphic relation where a positive constant is added to each element 
    in a list of test data (td). It checks if the output increases or remains constant after the transformation.
    """
    def __init__(self, td_list, cons):
        """
        Initializes the MR_ADD object.
        
        :param td_list: List of test data lists. Each test data list is a list of numeric values.
        :param cons: A positive constant to be added to each element of the test data lists.
        """
        self.td_list = td_list
        self.cons = cons
        self.td_output_list = []
        self.ttd_output_list = []

    def followUpTD(self):
        """
        Applies the metamorphic transformation to each test data list by adding the constant.

        :return: List of transformed test data lists.
        """
        transformed_td_list = []
        
        print(is_valid_input(self.td_list))

        if is_valid_input(self.td_list):
            
            for td in self.td_list:
                print(td)
                
                if isinstance(td, list):
                    transformed_td_list.append([item + self.cons for item in td])
                else:
                    transformed_td_list.append(td + self.cons )
            return transformed_td_list

        else:
            if isinstance(self.td_list, list):
                return [item + self.cons for item in self.td_list]
        
    def mrChecker(self, outputTD, outputTTD):
        error_message = None
        
        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()

        try:
            if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0) or outputTD < outputTTD:
                self.vs = 0
                self.vs_string = 'No-violate'
            else:
                self.vs = 1
                self.vs_string = 'Violate'
                
            return self.mrCheckerResult()
        
        except TypeError:
            error_message = traceback.format_exc()
            self.vs = 'error'
            self.vs_string = 'error'
            return self.mrCheckerResult()

    def mrCheckerResult(self):
        
        return {
            'td' : self.td_list,
            'ttd': self.ttd,
            'td_output': self.td_output,
            'ttd_output': self.ttd_output,
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
# Example Usage
# td_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3], 3,4,5]
# td_list = [1, 2, 3]

# cons = 2
# mr_add = MR_ADD(td_list, cons)
# print(mr_add.followUpTD())
# # Assuming we have output lists for the original and transformed test data
# outputTD_list = [some_function(td) for td in td_list]
# outputTTD_list = [some_function(ttd) for ttd in mr_add.followUpTD()]

# results = mr_add.mrChecker(outputTD_list, outputTTD_list)
