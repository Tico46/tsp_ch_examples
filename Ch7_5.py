# Multiply all the #s in list [8, 19, 148, 4] with #s in
# [9, 1, 33, 83] and append each result to a third list.

list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
total = []

for i in list_1:
        for j in list_2:
                mult = i * j
                total.append(mult) #in first run, i will multiply with each j in list 2 then i = 1, repeat

print(total)

"""
First run:
list_1[0] * list_2[0]
list_1[0] * list_2[1]
list_1[0] * list_2[2]
list_1[0] * list_2[3]

Second run:
list_1[1] * list_2[0]
list_1[1] * list_2[1]
list_1[1] * list_2[2]
list_1[1] * list_2[3]

etc
"""



