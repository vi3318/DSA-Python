# Infinite Recursion
def greet():
    print("Hello!")
    greet()

greet()

# Stack Overflow will occur due to infinite recursion