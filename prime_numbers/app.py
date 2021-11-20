
def is_prime(number: int) -> bool:
    primes = [x for x in range(1, 101) if number % x == 0]
    return len(primes) == 2

def run():

    number: int = "caca"
    if is_prime(number):
        print(str(number) + " is prime.")
    else:
        print(str(number) + " isn't prime")

if __name__ == "__main__": 
    run()