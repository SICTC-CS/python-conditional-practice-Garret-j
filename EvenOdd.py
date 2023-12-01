num = input("Enter an even or odd number ")
if "." in num:
        num=input("Whole Number Please: ")
if int(num) % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
print("")