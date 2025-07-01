s = "hello"

# Indexing
print(s[0])
print(s[-1])

# Slicing
print(s[1:4])
print(s[:3])
print(s[2:])

# Immutability
# s[0] = "H"
s = "Hello"

# Iterate over string
for ch in s:
    print(ch, end="\t")
print("\n")

# Multiply strings
print("ha" * 10) # ha + ha + ha....

# compare strings
print("apple" == "apple")
print("apple" > "Apple")

# in, not in
print("app" in "apple")
print("bat" not in "banana")