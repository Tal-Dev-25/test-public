import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    """
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    if number == 2:
        return True   # 2 is the only even prime number

    # Optimization: check for divisors up to the square root of the number
    limit = int(math.sqrt(number)) + 1 
    for i in range(2, limit):
        if (number % i) == 0:
            return False  # Found a divisor, so it's not prime
    
    return True # No divisors found, so it is prime

# Example usage:
user_input = int(input("Enter a number to check: "))

if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is not a prime number.")

