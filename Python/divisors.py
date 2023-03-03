num = int(input("What is your number: "))
i = 0
divisors = []
while num >= i:
    i = i + 1
    if num % i == 0:
        divisors.append(i)
print("The divsors of " + str(num) + " are: " + ' '.join(str(i) for i in divisors))