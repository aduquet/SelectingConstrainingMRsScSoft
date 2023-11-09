# def square(data):

#     for i in range(0, len(data)):
#         data[i] = data[i] * data[i]

#     return data

def square(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")
    
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")
    
    return [x**2 for x in data]
