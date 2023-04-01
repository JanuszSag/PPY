def isPrime(*numbers):
    ppl = (numbers)
    for i in ppl:
        prime = True
        if i == 1 or i == 0 or (i%2==0 and i!=2):
            prime = False
        if i == 2 or i == 3:
            prime = True
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                prime = False
                break
        if(prime):
            print(str(i)+" is prime")
        else:
            print(str(i)+" is not prime")

isPrime(1,5,4,2,3,7,0,30,21)