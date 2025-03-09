def swap(a, b):
    a, b = b, a
    return a, b

x = 5
y = 10
print("Before swapping: x = {x}, y = {y}")
x, y = swap(x, y)
print("After swapping: x = {x}, y = {y}")

