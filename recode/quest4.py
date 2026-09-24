# Question 4 Validate an import
# Challenging  |  13 minutes  |  25 marks
# You receive a list of strings representing whole-unit amounts. 
# Return a dictionary with total and rejected. Use Python int(raw) conversion: 
# surrounding whitespace is accepted. A converted amount of zero or more is valid. 
# Negative amounts and strings that cannot be converted must each increase rejected by one. 
# An empty list returns both values as zero. Do not change the input.
def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    for raw in raw_values:
        try:
            if int(raw) < 0:
                rejected += 1
            else:
                total += int(raw)
        except ValueError:
            rejected += 1
    return {"total": total, "rejected": rejected}
print(summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]))

# Required example: ["10", " 5 ", "bad", "-3", "0", ""] must return {"total": 15, "rejected": 3}. 
# Inputs are always strings; no other type validation is required.
# Q4 Part A
# Identify three defects or risks in the supplied function. 
# Explain why a bare except can hide an unrelated failure. [6 marks]
"""
accepts negative values
does not count rejected items
Has a bare except
"""
# Q4 Part B
# Rewrite the function to meet every rule. Catch only the expected conversion exception. [11 marks]
def summarise_amounts(raw_values):
    total = 0
    rejected = 0
    for raw in raw_values:
        try:
            if int(raw) < 0:
                rejected += 1
            else:
                total += int(raw)
        except ValueError:
            rejected += 1
    return {"total": total, "rejected": rejected}
print(summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]))

# Q4 Part C
# Write four executable assertions covering the required mixed example, 
# empty input, all rejected input, and a valid zero. 
# State why checking only total could miss a bug. [8 marks]
assert summarise_amounts([]) == {"total": 0, "rejected": 0}
assert summarise_amounts(["bad", "-3"]) == {"total": 0, "rejected": 2}
assert summarise_amounts(["0", " 0 "]) == {"total": 0, "rejected": 0}