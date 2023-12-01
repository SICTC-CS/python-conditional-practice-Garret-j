num=int(input("Enter a number, to check if it is a palindrome: "))
storage=num
reverse=0
while(num>0):
    dig=num%10
    reverse=reverse*10+dig
    num=num//10
if(storage==reverse):
    print("This is a palindrome")
else:
    print("This is not a palindrome")
print("A palindrome is a word phrase or sequenece that reads the same forwards and backwards.")