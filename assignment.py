# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)    
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
   
fizz_buzz(7)  # This will return 7
fizz_buzz(9)  # This will return 'Fizz'
fizz_buzz(10)  # This will return 'Buzz'


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    return sum(x ** 2 for x in numbers if isinstance(x, (int, float))) # Ensure only numbers – whole numbers and those with decimal points – are processed



# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    vowels =  "aeiouAEIOU" #ensuring both uppercase and lowercase vowels are counted
    return sum(1 for char in string if char in vowels) # Count each vowel in the string
   


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    1
    >>> count_repeats("aeiou")
    0
    """
    from collections import Counter # Importing Counter to count occurrences of each character
    counts = Counter(string) # Counting occurrences of each character in the string
    return sum(1 for char, count in counts.items() if count > 1) # Count how many characters appear more than once


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
