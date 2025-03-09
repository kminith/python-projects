def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    return count
input_string = "Hello World"
print("Number of vowels in 'input_string' is :" ,{count_vowels(input_string)})

