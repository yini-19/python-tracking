# Day 2 Python Core Engineering Assessment
# yiyakazahn@gmail.com Switch account
 
# Question 3 Protect the original profile
# Moderate  |  11 minutes  |  20 marks
# The function should return a new profile with an extra tag. 
# The original profile and its tags must stay unchanged. 
# The profile has only a string name and a list of string tags; both keys always exist.
def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])
# Q3 Part C
# Write assertions showing that the original tags remain unchanged 
# and the returned tags contain the new tag. 
# Then append another tag to the returned list and assert that the original still 
# has only its initial tag. [6 marks]
assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]
changed["tags"].append("asserting")
assert original["tags"] == ["python"]

# Q3 Part B
# Repair add_tag so its returned dictionary and tags list are independent of the original. 
# Do not change the public function signature. [7 marks]
def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = updated["tags"] + [tag]
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])

# Q3 Part A
# Before running the code, predict all three output lines.
"""
["python"]
False
True
""" 
# Explain what copy() copies here and which object is still shared. [7 marks]
"""
The copy() function only duplicates the inner dictionary but the outer dict is shared
so the "tags" object is shared
"""
# Page 4 of 6
# Never submit passwords through Google Forms.
# This content is neither created nor endorsed by Google. - Contact form owner - Terms of Service - Privacy Policy
# Does this form look suspicious? Report

# Google Forms