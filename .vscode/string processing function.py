python = "python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isalnum())
print(len(python))
print(python.replace("python", "Java"))
index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java"))
print(python.count("n"))