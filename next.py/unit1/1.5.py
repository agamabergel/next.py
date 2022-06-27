import functools
names = ""
with open("./1.5Names.txt") as names:
    names = names.read().splitlines()

### option 1:
print(f"Longest name: {max(names, key=len)}")

### option 2:
print(f"Sum names length: {sum(list(map(len, names)))}")

### option 3:
print("Shortest names: ")
sorted_names = sorted(names, key=len)
[print(name) for name in sorted_names if len(name) == len(sorted_names[0])]

### option 4:
names_length = [len(name) for name in names]
with open("./name_length.txt", "w") as file_names:
    [file_names.write(f"{name}\n") for name in names_length]

### option 5:
length = int(input("Enter name length: "))
[print(names[idx]) for idx, name in enumerate(names) if len(name) == length]






