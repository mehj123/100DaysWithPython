def prime_checker(number):
    prime = True
    if(number == 1):
        print("It's not a prime number.")
    else:
        for i in range (2, number):
            if(number % i == 0):
                print("It's not a prime number.")
                prime = False
                break
        if prime:
            print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)