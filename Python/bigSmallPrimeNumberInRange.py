def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bigSmallPrimeInRange(start,end):
    listPrimes=[i for i in range(start,end+1) if is_prime(i)]
    
    if(len(listPrimes)>=2):
        return listPrimes[0],listPrimes[-1]
    if(len(listPrimes)==1):
        return listPrimes[0]
    return []

def get_input():
    start,end = map(int,input("Enter two numbers: ").split())
    return start,end

def main():
    start,end=get_input()
    print(f"The smallest and the largest prime number in range {start}, {end} :",bigSmallPrimeInRange(start,end))

main()

