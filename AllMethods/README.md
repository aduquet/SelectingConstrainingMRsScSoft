

# AllMethods: A Collection of Python Functions

## Overview
`AllMethods` contains 99 Python functions, each designed to process numerical inputs and returns numerical outputs. The functions are systematically organized into 11 groups based on shared characteristics, such as the number and type of inputs and outputs.

## Group Organization
Below is the detailed information for each group within `AllMethods`, outlining the specific categories of functions:

### Group 01
- **Number of Inputs**: 1
- **Input Type**: List
- **Number of Outputs**: 1
- **Output Type**: Numerical (integer or float)

### Group 02
- **Number of Inputs**: 2
- **Input Type**: List
- **Number of Outputs**: 1
- **Output Type**: Numerical (integer or float)

### Group 03
- **Number of Inputs**: 2
- **Input Type**: List
- **Number of Outputs**: 1
- **Output Type**: List

### Group 04
- **Number of Inputs**: 1
- **Input Type**: List
- **Number of Outputs**: 1
- **Output Type**: List

### Group 05
- **Number of Inputs**: 2
- **Input Type**: List and Numerical (integer or float)
- **Number of Outputs**: 1
- **Output Type**: List and Numerical (integer or float)

### Group 06
- **Number of Inputs**: 2
- **Input Type**: List and Numerical (integer or float)
- **Number of Outputs**: 1
- **Output Type**: List

### Group 07 - Special Cases
- **Functions**: autoCorrelation, partition, biSearchFromTo
    - **Number of Inputs**: 4
    - **Input Type**: 1 List, and 3 Numerical (integer or float)
    - **Number of Outputs**: 1
    - **Output Type**: List
- **Function**: clip
    - **Number of Inputs**: 3
    - **Input Type**: 1 List, and 2 Numerical (integer or float)
    - **Number of Outputs**: 1
    - **Output Type**: List
- **Function**: evaluateWeightedProduct
    - **Number of Inputs**: 4
    - **Input Type**: 2 List, and 2 Numerical (integer or float)
    - **Number of Outputs**: 1
    - **Output Type**: Numerical (integer or float)

### Group 08
- **2 Functions with**:
    - **Number of Inputs**: 2
    - **Input Type**: List
    - **Number of Outputs**: 1
    - **Output Type**: Boolean
- **2 Functions with**:
    - **Number of Inputs**: 1
    - **Input Type**: List
    - **Number of Outputs**: 1
    - **Output Type**: Boolean

### Group 09
- **Number of Inputs**: 3
- **Input Type**: List, 2 Numerical (integer or float)
- **Number of Outputs**: 1
- **Output Type**: Numerical (integer or float)

### Group 10
- **Number of Inputs**: 3
- **Input Type**: 2 List and 1 Numerical (integer or float)
- **Number of Outputs**: 1
- **Output Type**: Numerical (integer or float)

### Group 11
- **Number of Inputs**: 3
- **Input Type**: 3 Numerical (integer or float)
- **Number of Outputs**: 1
- **Output Type**: Numerical (integer or float)


## Group Organization and Function Count
Below is the detailed information for each group within `AllMethods`, outlining the specific categories of functions along with the number of functions in each group (`groupID`):

| Group ID | Number of Functions | Description |
|----------|---------------------|-------------|
| Group_01 | 24                  | **Number of Inputs**: 1<br>**Input Type**: List<br>**Number of Outputs**: 1<br>**Output Type**: Numerical (integer or float) |
| Group_02 | 24                  | **Number of Inputs**: 2<br>**Input Type**: List<br>**Number of Outputs**: 1<br>**Output Type**: Numerical (integer or float) |
| Group_03 | 14                  | **Number of Inputs**: 2<br>**Input Type**: List<br>**Number of Outputs**: 1<br>**Output Type**: List |
| Group_04 | 8                   | **Number of Inputs**: 1<br>**Input Type**: List<br>**Number of Outputs**: 1<br>**Output Type**: List |
| Group_05 | 8                   | **Number of Inputs**: 2<br>**Input Type**: List and Numerical (integer or float)<br>**Number of Outputs**: 1<br>**Output Type**: Numerical (integer or float) |
| Group_06 | 5                   | **Number of Inputs**: 2<br>**Input Type**: List and Numerical (integer or float)<br>**Number of Outputs**: 1<br>**Output Type**: List |
| Group_07 | 5                   | Special case with multiple function types (autoCorrelation, partition, biSearchFromTo, clip, evaluateWeightedProduct) |
| Group_08 | 4                   | Includes functions with Boolean outputs, both with single and dual list inputs |
| Group_09 | 3                   | **Number of Inputs**: 3<br>**Input Type**: List, 2 Numerical (integer or float)<br>**Number of Outputs**: 1<br>**Output Type**: 2 Numerical (integer or float) |
| Group_10 | 2                   | **Number of Inputs**: 3<br>**Input Type**: 2 List and 1 Numerical (integer or float)<br>**Number of Outputs**: 1<br>**Output Type**: Numerical (integer or float) |
| Group_11 | 2                   | **Number of Inputs**: 3<br>**Input Type**: 3 Numerical (integer or float)<br>**Number of Outputs**: 1<br>**Output Type**: Numerical (integer or float) |



## Usage
To utilize a function from `AllMethods`, import the desired function from its respective group module and provide the required numerical inputs.

Example:
```python
from Group_01 import function_name
result = function_name([input_list])
```
