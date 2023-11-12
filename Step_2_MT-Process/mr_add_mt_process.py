import math

class MR_ADD():
    """ MR ADD 
    Change in the input -> Add a possitive constant
    Expected change in the output -> Increase or remain constant
    """
    ttd = None
    vs = None
    vs_string = None
    td_output = None
    ttd_output = None
    
    def __init__(self, test_data_one_input, cons):
        self.test_data_one_input = test_data_one_input
        self.cons = cons
    
    # MR_ADD -> Add a positive constant
    def followUpTD(self):
        aux_list = []
        
        if len(self.test_data_one_input) != 0 and type(self.test_data_one_input) == list:    
            for item in self.test_data_one_input:
                aux_list.append(item + self.cons)
        
        return aux_list
    
    def mrChecker(self, outputTD, outputTTD):
        
        self.td_output = outputTD
        self.ttd_output = outputTTD
        self.ttd = self.followUpTD()
        
        if math.isclose(outputTD, outputTTD, rel_tol=1e-9, abs_tol=0) or outputTD < outputTTD:
            self.vs = 0
            self.vs_string = 'No-violate'
        
        else:
            self.vs = 1
            self.vs_string = 'Violate'
            
        return self.mrCheckerResult()
    
    def mrCheckerResult(self):
        
        return {
            'td' : self.test_data_one_input,
            'ttd': self.ttd,
            'td_output': self.td_output,
            'ttd_output': self.ttd_output,
            'vs_str': self.vs_string,
            'vs': self.vs,
        }
        
            
            