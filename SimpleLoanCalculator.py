L = input("cost of the Loan: ")
i = input("interest rate: ")
n = input("no. of years of the Loan: ")
#now change the datatype of str to an int
n = int(n)
i = int(i)
#5% interest rate
i = i*5/100
L = int(L)

#didnt use [] these as used for a list
m = L*(i*(1+i)*n)/((1+i)*n-1)
print("your monthly payment is %.2f" %m)

