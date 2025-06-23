# Task 1: Function to add two numbers and return the result
def add_numbers(num1, num2):
    return num1 + num2

# Testing the function
print(add_numbers(5, 10))



#Task 2: Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Testing the function
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))



# Task 3: Function to reverse a string
def reverse_string(text):
    return text[::-1]

# Testing the function
print("Reversed 'hello':", reverse_string("hello"))  
print("Reversed 'python':", reverse_string("python"))




## Task 4: Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():  # Convert to lowercase first
        if char in vowels:
            count += 1
    return count

# Testing the function
print("Vowels in 'Hello':", count_vowels("Hello"))      
print("Vowels in 'Umbrella':", count_vowels("Umbrella")) 



#Task 5: Function to calculate the factorial of a number
def calculate_factorial(n):
    if n == 0:
        return 1  # Special case: 0! is 1
    result = 1
    for i in range(1, n + 1):  # From 1 to n (inclusive)
        result *= i  # Multiply result by i
    return result

# Testing the function
print("Factorial of 5:", calculate_factorial(5))
print("Factorial of 0:", calculate_factorial(0)) 





#Task 6:  The decorator function
def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

# This function applies the decorator to any input function
def apply_decorator(func):
    decorated = decorator_func(func)
    return decorated()

# Sample function to test
def say_hello():
    print("Hello!")

# Testing the decorator
apply_decorator(say_hello)



# Task 7: Function to sort a list of (name, age) tuples by age
def sort_by_age(people):
    return sorted(people, key=lambda person: person[1])

# Testing the function
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sort_by_age(people)
print("Sorted by age:", sorted_people)




# Task 8: Function to merge two dictionaries, summing values for common keys
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values if key exists
        else:
            merged[key] = value  # Otherwise, just add the key
    return merged

# Testing the function
dict1 = {"apples": 3, "bananas": 5}
dict2 = {"apples": 2, "oranges": 4}
merged = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged)




# Task 9:  Class representing a Car
class Car:
    # Constructor to initialize attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display the car's information
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

# Testing the class
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info() 
