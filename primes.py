"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes >= 1:
        count = 1
        while len(list) < number_of_primes:
            count += 1
            isPrime = True
            for num in range(2, count):
                if count % num == 0:
                    isPrime = False
                    break

            if isPrime:
                list.append(count)
    else:
        raise ValueError

    return list