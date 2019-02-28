x = int(input("Enter a number : "))

for i in range(x):
    # Important! String output and int on the same line 
    print ("Your Number is ", i+1)

for i in range(x):
    x = x + x
    print (x)