
# write out various datatypes in python

print("type('This is a String')")
print(type("this is a string"))  # String

print(type(42))                  # Integer
print(type(3.14))                # Float
print(type(True))                # Boolean
print(type([1, 2, 3]))          # List

# compare datatypes

a = '100'
b = 100

print(f"Is '100' a string? {isinstance(a, str)}")
print(f"Is 100 an integer? {isinstance(b, int)}")

print(f"Is a == b ? {a == b} because they are different datatypes")
print(f"Is a != b ? {a != b} because they are different datatypes")

a = "a String"
a = 1234
print(f"Now a is {a} => an integer and of class: {type(a)}")