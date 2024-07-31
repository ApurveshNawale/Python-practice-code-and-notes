name = input("Write your name: ")
letter = input("Write a letter you want to find: ")

print("Name:", name)
print("Letter to find:", letter)

index = name.find(letter)

if index != -1:
    print(f"The letter '{letter}' is found at index {index}.")
else:
    print(f"The letter '{letter}' is not found in the name.")