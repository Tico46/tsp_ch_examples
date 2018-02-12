# 3a. Use Python's "re module" to match "boo" and "loo" in a sentence
# "The ghost that says boo haunts the loo".

import re

string = "The ghost that says boo haunts the loo"

match = re.findall(".oo", string)

print(match)
