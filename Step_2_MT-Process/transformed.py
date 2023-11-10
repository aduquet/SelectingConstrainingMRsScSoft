from test_data_transformer import InputTransformed 
from mr_add_MT_process import MR_ADD
import numpy as np

a = InputTransformed([]).mrADD(9)
print(a)

b = InputTransformed([1,2,3,4]).mrPER()
print(b)

b = InputTransformed([]).mrPER()
print(b)

b = InputTransformed([12,4,5,6]).mrINC(900)
print(b)

b = InputTransformed([12,4,5,6]).mrEXC()
print(b)

prueba = MR_ADD(test_data_one_input=[-12,4,5,-6], cons=2).followUpTD()

vsn = MR_ADD([-12,4,5,-6], cons = 2).mrChecker(outputTD=np.sum([-12,4,5,-6]), outputTTD=np.sum(prueba))
print(prueba)
print(vsn)
print(np.sum([-12,4,5,-6]))
print(np.sum(prueba))