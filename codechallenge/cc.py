# Summing Values from a Dictionary

# Given an object/dictionary with keys and values that consist of both strings and integers,
# design an algorithm to calculate and return the sum of all of the numeric values.
# Verbalize your thought process as much as possible before writing any code.

# Run through the UPER problem solving framework while going through your thought process.

# looking sum of all numeric values
# iterate dic
# if value is num 
# add num to total
# return total

# Example
# {
# "cat" : "bob",
# "dog" : 23,
# 19 : 18,
# 90 : "fish"
# }
# Running your algorithm should output 41, the sum of the values 23 and 18.

example = {
"cat" : "bob",
"dog" : 23,
19 : 10,
90 : "fish"
}

def sum_of_values(d):
    total = 0

    for v in d.values():
        if isinstance(v, int):
            total += v

    
    return total

print(sum_of_values(example))