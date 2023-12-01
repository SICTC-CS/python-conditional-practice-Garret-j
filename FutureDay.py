sunday=0
monday=1
tuesday=2
wednesday=3
thursday=4
friday=5
saturday=6
weekday=int(input("What is today's day as a number 0-6 (Sunday thorugh Saturday) "))
while True:
  if weekday in [0,1,2,3,4,5,6]:
    print(f"Thank you for Today's Date {weekday}")
    break
  else:
    weekday=int(input("Please enter a valid day "))

future=int(input("How many days have elapsed "))
if weekday==0:
  future=future%7
  if future==0:
    print("Today is Sunday and the future will be Sunday ")
  elif future==1:
    print("Today is Sunday and the future will be Monday ")
  elif future==2:
    print("Today is Sunday and the future will be Tuesday ")
  elif future==3:
    print("Today is Sunday and the future will be Wednesday ")
  elif future==4:
    print("Today is Sunday and the future will be Thursday" )
  elif future==5:
    print("Today is Sunday and the future will be Friday" )
  elif future==6:
    print("Today is Sunday and the future will be Saturday" )

if weekday==1:
  future=future%7
  if future==0:
    print("Today is Monday and the future will be Monday" )
  elif future==1:
    print("Today is Monday and the future will be Tuesday" )
  elif future==2:
    print("Today is Monday and the future will be Wedensday" )
  elif future==3:
    print("Today is Monday and the future will be Thursday" )
  elif future==4:
    print("Today is Monday and the future will be Friday" )
  elif future==5:
    print("Today is Monday and the future will be Saturday" )
  elif future==6:
    print("Today is Monday and the future will be Sunday" )

if weekday==2:
  future=future%7
  if future==0:
    print("Today is Tuesday and the future will be Tuesday" )
  elif future==1:
    print("Today is Tuesday and the future will be Wedensday" )
  elif future==2:
    print("Today is Tuesday and the future will be Thursday" )
  elif future==3:
    print("Today is Tuesday and the future will be Friday" )
  elif future==4:
    print("Today is Tuesday and the future will be Saturday" )
  elif future==5:
    print("Today is Tuesday and the future will be Sunday" )
  elif future==6:
    print("Today is Tuesday and the future will be Monday" )

if weekday==3:
  future=future%7
  if future==0:
    print("Today is Wedensday and the future will be Wednsday" )
  elif future==1:
    print("Today is Wedensday and the future will be Thursday" )
  elif future==2:
    print("Today is Wedensday and the future will be Friday" )
  elif future==3:
    print("Today is Wedensday and the future will be Saturday" )
  elif future==4:
    print("Today is Wedensday and the future will be Sunday" )
  elif future==5:
    print("Today is Wedensday and the future will be Monday" )
  elif future==6:
    print("Today is Wedensday and the future will be Tuesday" )

if weekday==4:
  future=future%7
  if future==0:
    print("Today is Thursday and the future will be Thursday" )
  elif future==1:
    print("Today is Thursday and the future will be Friday" )
  elif future==2:
    print("Today is Thursday and the future will be Saturday" )
  elif future==3:
    print("Today is Thursday and the future will be Sunday" )
  elif future==4:
    print("Today is Thursday and the future will be Monday" )
  elif future==5:
    print("Today is Thursday and the future will be Tuesday" )
  elif future==6:
    print("Today is Thursday and the future will be Wedensday" )

if weekday==5:
  future=future%7
  if future==0:
    print("Today is Friday and the future will be Friday" )
  elif future==1:
    print("Today is Friday and the future will be Saturday" )
  elif future==2:
    print("Today is Friday and the future will be Sunday" )
  elif future==3:
    print("Today is Friday and the future will be Monday" )
  elif future==4:
    print("Today is Friday and the future will be Tuesday" )
  elif future==5:
    print("Today is Friday and the future will be Wedensday" )
  elif future==6:
    print("Today is Friday and the future will be Thursday" )

if weekday==6:
  future=future%7
  if future==0:
    print("Today is Saturday and the future will be Saturday" )
  elif future==1:
    print("Today is Saturday and the future will be Sunday" )
  elif future==2:
    print("Today is Saturday and the future will be Monday" )
  elif future==3:
    print("Today is Saturday and the future will be Tuesday" )
  elif future==4:
    print("Today is Saturday and the future will be Wedensday" )
  elif future==5:
    print("Today is Saturday and the future will be Thursday" )
  elif future==6:
    print("Today is Saturday and the future will be Friday") 