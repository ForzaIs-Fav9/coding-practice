import numpy as np
import time
#Let us a make a huge dataset
size = 10_000_000
#Let's make a Python list
lst = list(range(size))
#And a NumPy array
array = np.array(lst)
#Now, for the Python list, let's calculate the time taken to multiply each element in it by 2
start1 = time.time()
new_list = [i * 2 for i in lst]
# This is equivalent to:
# new_list = []
# for i in lst:
#  new_list.append(i*2)
end1 = time.time()
# Now, the execution time is end1 - start1
print("The time taken for the Python list is: ", end1 - start1)

#Now for the NumPy array
start2 = time.time()
new_list = array * 2
end2 = time.time()
print("The time taken for the NumPy array is: ", end2 - start2)

#Now, when this is run, we see that, there's a huge difference between the times taken by the Python list and NumPy array. This is because,
# A NumPy array works on the basis of vectorized math functions on special C language, which is way faster than normal Python lists.
# A normal Python list does this by manually multiplying each element by 2 individually, therefore, taking a longer time.
# This is a huge deal for data at scale because fields like AI or ML have operations that run millions or billions of time. If data is processed this slowly, it can waste hours on end.
# Therefore, saving milliseconds on an operation will collectively save hours.
