python_assignment.pyn = int(input("please enter a number : "))
prime_number=[]
for i in range(2,n+1):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        prime_number.append(i)
print(prime_number)
