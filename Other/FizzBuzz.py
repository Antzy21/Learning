
    
for n in range(1,23):
    if n%3 == 0:
        if n%5 == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if n%5 == 0:
            print("buzz")
        else:
            print(n)



#n % 3 -> n is divisible by 3