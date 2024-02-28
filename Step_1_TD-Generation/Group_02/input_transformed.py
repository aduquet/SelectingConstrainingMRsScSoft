import random
import json
import math

def MR_ADD(td_a, td_b, cons):
    """ MR ADD 
    Change in the input -> Add a possitive constant
    Expected change in the output -> Increase or remain constant
    """
    
    aux_list_a = []
    aux_list_b = []
    
    if len(td_a) != 0 and type(td_a) == list and len(td_b) != 0 and type(td_b) == list:
        for item in td_a:
            aux_list_a.append(item + cons)
        
        for item in td_b:
            aux_list_b.append(item + cons)
        
    return aux_list_a, aux_list_b

def MR_EXC(td_a, td_b):
    
    """ MR EXC 
    Change in the input -> Remove an element
    Expected change in the output -> Decrease or remain constant
    """
    
    aux_list_a = td_a.copy()
    aux_list_b = td_b.copy()
    
    if len(td_a) != 0 and type(td_a) == list and len(td_b) != 0 and type(td_b) == list:
        
        position = random.randint(0, len(td_a)-1)
        aux_list_a.pop(position)
        aux_list_b.pop(position)
        
        return aux_list_a, aux_list_b
        
    else:
        return [], []
    
def MR_INC(td_a, td_b, cons):
    
    """ MR INC 
    Change in the input -> Add new element
    Expected change in the output -> Increase or remain constant
    """
    
    aux_list_a = td_a.copy()
    aux_list_b = td_b.copy()
        
    if len(td_a) != 0 and type(td_a) == list and len(td_b) != 0 and type(td_b) == list:
        position = random.randint(0, len(aux_list_b))
        aux_list_a.insert(position, cons)
        aux_list_b.insert(position, cons)

        return aux_list_a, aux_list_b
    else:
        return [cons], [cons]

def MR_INV(td_a, td_b):
    # MR_INV -> Take the inverse of each element
    aux_list_a = td_a.copy()
    aux_list_b = td_b.copy()
    
    if len(td_a) != 0 and type(td_a) == list and len(td_b) != 0 and type(td_b) == list:
        for item in td_a:
            if item != 0:
                aux_list_a.append(1 / item )

            else:
                aux_list_a.append('ZeroDivisionError')
                
        for item in td_b:
            if item != 0:
                aux_list_b.append(1 / item )

            else:
                aux_list_b.append('ZeroDivisionError')
        
    return aux_list_a, aux_list_b

def MR_MUL(td_a, td_b, cons):
    """ MR MUL 
    Change in the input -> Multiply by a possitive constant
    Expected change in the output -> Increase or remain constant
    """
    
    aux_list_a = []
    aux_list_b = []
    
    if len(td_a) != 0 and type(td_a) == list and len(td_b) != 0 and type(td_b) == list:
        for item in td_a:
            aux_list_a.append(item * cons)
        
        for item in td_b:
            aux_list_b.append(item * cons)
        
    return aux_list_a, aux_list_b
    
def MR_PER(td_a, td_b):
    """ MR PER 
    Change in the input -> Randomly permute the elements
    Expected change in the output -> Remain constant
    """
    
    all_equal_a = len(set(td_a)) == 1
    all_equal_b = len(set(td_b)) == 1

    aux_list_a = td_a.copy()
    aux_list_b = td_b.copy()
        
    if all_equal_a != 1 and len(td_a) != 0 and type(td_a) == list and all_equal_b != 1 and len(td_b) != 0 and type(td_b) == list:
        while td_a == aux_list_a and td_b == aux_list_b:
            random.shuffle(aux_list_a)
            random.shuffle(aux_list_b)
        return aux_list_a, aux_list_b
    else:
        return aux_list_a, aux_list_b
    
def save_json(json_object, output_file):
    
    # Save JSON object to file
    with open(output_file, "w") as json_file:
        json.dump(json_object, json_file, indent= 4)

    print("JSON object saved to", output_file)
    
if __name__ == '__main__':
    
    import click
    
    global auxList
    auxList = []
    
    @click.command()
    @click.option('-i', '--input_path', 'input_path')
    @click.option('-o', '--output_file', 'output_file')

    def main(input_path, output_file):
        
        
        with open(input_path, 'r') as readfiles:
            inputs = json.load(readfiles)
            json.dumps(inputs, indent=4)
            
        for i in range(0, len(inputs)):
            td_a = inputs[str(i)]['td_a']
            td_b = inputs[str(i)]['td_b']
                       
            td_ttd_a_add, td_ttd_b_add = MR_ADD(td_a, td_b, 4)
            inputs[str(i)]['td_ttd_a_MR_ADD'] = td_ttd_a_add
            inputs[str(i)]['td_ttd_b_MR_ADD'] = td_ttd_b_add

            td_ttd_a_exc, td_ttd_b_exc = MR_EXC(td_a, td_b)
            inputs[str(i)]['td_ttd_a_MR_EXC'] = td_ttd_a_exc
            inputs[str(i)]['td_ttd_b_MR_EXC'] = td_ttd_b_exc
            
            td_ttd_a_inc, td_ttd_b_inc = MR_INC(td_a, td_b, 4)
            inputs[str(i)]['td_ttd_a_MR_INC'] = td_ttd_a_inc
            inputs[str(i)]['td_ttd_b_MR_INC'] = td_ttd_b_inc
            
            td_ttd_a_inv, td_ttd_b_inv = MR_INV(td_a, td_b)
            inputs[str(i)]['td_ttd_a_MR_INV'] = td_ttd_a_inv
            inputs[str(i)]['td_ttd_b_MR_INV'] = td_ttd_b_inv

            td_ttd_a_mul, td_ttd_b_mul = MR_MUL(td_a, td_b, 4)
            inputs[str(i)]['td_ttd_a_MR_MUL'] = td_ttd_a_mul
            inputs[str(i)]['td_ttd_b_MR_MUL'] = td_ttd_b_mul
            
            td_ttd_a_per, td_ttd_b_per = MR_PER(td_a, td_b)
            inputs[str(i)]['td_ttd_a_MR_PER'] = td_ttd_a_per
            inputs[str(i)]['td_ttd_b_MR_PER'] = td_ttd_b_per 
        
        save_json(inputs, output_file)           
            
        #     input_outputs = _get_outputs(td_ttd)
        #     checkers = mr_checker(input_outputs)
            
        #     auxList.append(checkers)

        # final_df = pd.DataFrame(auxList)
        
        # save_csv(final_df, output_file, mainPathMRChecker)
        # save_json(final_df, output_file, mainPathMRChecker)
        
main()