# Create an empty set:
#Sets are different from lists and tuples in that they are unordered
#it does not append repeated elements
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

"""
Output:
{1, 3, 4}
The set has 3 elements.
"""
