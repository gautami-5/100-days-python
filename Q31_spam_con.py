s = input("Enter a sentence: ")

if "Make a lot of money" in s:
    print("SPAM")
elif "Buy now" in s:
    print("SPAM")
elif "Subscribe this" in s:
    print("SPAM")
elif "Click this" in s:
    print("\nThis is a SPAM comment")
else:
    print("\nThis is not a SPAM comment")
