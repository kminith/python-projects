def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
celsius = 25
fahrenheit = 77

print("{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
print("{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")

