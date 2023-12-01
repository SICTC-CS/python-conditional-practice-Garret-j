firstNumber = input("First Number: ")
secondNumber = input("Second Number: ")
thirdNumber = input("Thrid Number: ")

if firstNumber and secondNumber and thirdNumber.isdigit():
  firstNumber = int(firstNumber)
  secondNumber = int(secondNumber)
  thirdNumber = int(thirdNumber)
else:
  print("Please enter a number")

if isinstance(firstNumber, int) and isinstance(secondNumber, int) and isinstance(thirdNumber, int):
  if firstNumber > thirdNumber:
      firstNumber = firstNumber + thirdNumber
      thirdNumber = firstNumber - thirdNumber
      firstNumber = firstNumber - thirdNumber  
  if firstNumber > secondNumber:
      firstNumber = firstNumber + secondNumber
      secondNumber = firstNumber - secondNumber
      firstNumber = firstNumber - secondNumber
  if secondNumber > thirdNumber:
      secondNumber = secondNumber + thirdNumber
      thirdNumber = secondNumber - thirdNumber
      secondNumber = secondNumber - thirdNumber
  print (firstNumber, "<", secondNumber, "<", thirdNumber)