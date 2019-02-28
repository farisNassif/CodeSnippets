import datetime as dt
import math
import csv

# Create a filename formt he current date and fime
filename = dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d-%H-%M-%S.csv")

with open(filename,"w",newline='') as f:
    # Enable CSV writing to the file
    writer = csv.writer(f)
    writer.writerow(["i","j","gcd"])
    # Write the GCD for all (i,j) pairs from 0 to 100
    for i in range(100):
        for j in range(100):
            writer.writerow([i,j,math.gcd(i,j)])

print(dt.datetime.now())

# Prints without the decimal after the second
print(dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d-%H-%M-%S"))

# Prints without the decimal after the second
print(dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d-%H-%M-%S.csv"))

# Takes away decimal
print(math.floor(1.23))

# Factorial of a number
print("Factorial of four: ", math.factorial(4))

# Greatest common divisor
print("The greatest common divisor of 10 and 60: ",math.gcd(10,60))

# Greatest common divisor
print("The greatest common divisor of 10 and 65: ",math.gcd(10,65))