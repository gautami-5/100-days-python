words = {
    "Paani": "Water",
    "Kitaab": "Book",
    "Dost": "Friend",
    "Kursi": "Chair",
    "Khana": "Food",
    "Ghar": "House",
    "Suraj": "Sun",
    "Raat": "Night",
    "Ped": "Tree",
    "Baccha": "Child"
}

print("Welcome to the Hindi-English Dictionary!")
input("Press Enter to see the available Hindi words...")
print("\nAvailable Hindi words:")
for word in words.keys():
    print(word)
x = input("\nEnter a Hindi word to get its English meaning: ")
if x in words:
    print(f"The English meaning of '{x}' is: {words[x]}")