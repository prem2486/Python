n=int(input("specify the number: "))

for i in range(n):
    if i%2==0:
        print("Even: ",i)
print("\n")
        
for i in range(n):
    if i%2!=0:
        print("odd: ", i)# True if n is even, False if n is odd
# Output:
# specify the number: 5 