# 2. Write a program that collects two strings from a user, inserts them into the string 
# "Yesterday I wrote a [response_one]. I sent it to [response_two]!" and prints a new string.

response_1 = input("Please input the first noun: ")
response_2 = input("Now input the second noun: ")

message = """Yesterday I wrote a {}. I sent it to {}.""".format(response_1, response_2)

print(message)
