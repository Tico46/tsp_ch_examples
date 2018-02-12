# 10. Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." 
# to only include the characters before the comma.

text = "It was a bright cold day in April, and the clocks were striking thirteen."

slce = text[:33] #After running index(","), it indicated comma was at index[33]. slce is "slice"

print(slce)