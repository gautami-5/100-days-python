d = {"india": "Delhi", "usa": "washington DC", "uk": "London", "france": "Paris"}

x = input("Enter the name of the country: ")
y = x.lower()
print("Capital: ", d.get(y, "Not found")) #returns the value for the given key, if key is not found returns "Not found"
