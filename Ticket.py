speed = 0
ticket = 3
print("Exucse me sir do you know fast you where going? I'm going to have to ask you a few questions.")
birthday = input("Is today your birthday? (y/n) ")
if birthday.lower() not in ["y", "n", "yes", "no"]:
  print("Awsome Sauce")
  import sys
  sys.exit()

speed = input("How fast were you going? Nummber only please ")
if speed.isdigit():
   speed = int(speed)
   if birthday.lower() == "y":
       speed -= 5
       print(f" Officer I was going {speed}")
       if 61 <= speed <= 80:
         ticket = 1
       elif speed > 80:
         ticket = 2
       else:
         ticket = 0
   elif birthday.lower() == "n":
       print(f" Officer I was going {speed}")
       if 61 <= speed <= 80:
         ticket = 1
       elif speed > 80:
         ticket = 2
       else:
         ticket = 0 

if ticket == 0:
  print("Sorry sir seems you weren't speeding have a nice day now.")
elif ticket == 1:
  print("Since you wheren't majorly speeding I'm going to have to issue a small ticket. Don't let me catch you speeding again.")
elif ticket == 2:
  print("Please step out of the vechicle sir. You are under arest for reckless driving as well as a big ticket for your speeding.")