import numpy as np
import array as arr

numbers=arr.array('i',[0, 13, 5, -4, 6])

numbers[1]=15
numbers[2]=7
numbers[4]=12

print(np.square(numbers[3]))
print(numbers)