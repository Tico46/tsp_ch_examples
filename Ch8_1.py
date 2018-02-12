# Call a different function from the "statistics" module

import statistics
import random

# generate a list of random numbers from 0-100 and print
rndm_list = []
i = 0

for i in range(0, 11):
    num = random.randint(0, 101)
    rndm_list.append(num)
    i += 1

print(rndm_list)

#get the average of list of random numbers
average = round(statistics.mean(rndm_list))
print("The average of this list of numbers is: {}".format(average))
# Note: ".format()" will convert number string in this example

    
