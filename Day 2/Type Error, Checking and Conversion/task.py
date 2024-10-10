# Pause 1
len("12345")

# Pause 2
# Type Checking = (type())
print(type("Doom Eternal")) # Str
print(type(1000))           # Int
print(type(1234.5678))      # Float
print(type(True))           # Bool

print("")

# Type Data Conversion
print(int("456") + (int("789")))        # Convert a String to an Integer
print(str(987) + (str(654)))            # Convert an Integer to a String
print(float(256) + (float(256)))        # Convert an Integer to a Float
print(bool("True") + (bool("False")))   # Convert a String to a Boolean

print("")

# Pause 3
# print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name: "))))
