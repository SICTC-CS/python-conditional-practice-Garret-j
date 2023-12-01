import random
playerChoice=int(input("What will you player? Rock (0), Paper (1), Scissors (2), Lizard (3), or Spock (4): "))
print(f"You have choosen {playerChoice}")
if playerChoice == 0:
  print("Rock")
elif playerChoice == 1:
  print("Paper")
elif playerChoice == 2:
  print("Scissors")
elif playerChoice == 3:
  print("Lizard")
elif playerChoice == 4:
  print("Spock")
print("The computer will now choose")
computerChoice=random.randint(0,4)
replay = 0

if replay == 0: 
  if playerChoice == 0 and computerChoice == 0:
    print("Both chose rock. It's a tie")
    replay = 1
  elif playerChoice == 1 and computerChoice == 1:
    print("Both chose paper. It's a tie")
    replay = 1
  elif playerChoice == 2 and computerChoice == 2:
    print("Both chose scissors. It's a tie")
    replay = 1
  elif playerChoice == 3 and computerChoice == 3:
    print("Both chose lizard. I tip my hat to you. One legend to another. It's a tie")
    replay = 1
  elif playerChoice == 4 and computerChoice == 4:
    print("Both chose spock. It's a tie")
    replay = 1

  if playerChoice == 0 and computerChoice == 1:
    print("Player chose rock. Computer chose paper. Paper covers rock. Computer wins")
    replay = 1
  elif playerChoice == 0 and computerChoice == 2:
    print("Player chose rock. Computer chose scissors. Rock crushes scissors. Player wins.")
    replay = 1
  elif playerChoice == 0 and computerChoice == 3:
    print("Player chose rock. Computer chose lizard. Rock crushes lizard. Player wins.")
    replay = 1
  elif playerChoice == 0 and computerChoice == 4:
    print("Player chose rock. Computer chose Spock. Spock vaporizes rock. Player wins.")
    replay = 1
#results of player choosing paper.
  if playerChoice == 1 and computerChoice == 0:
    print("Player chose paper. Computer chose rock. Paper covers rock. Player wins.")
    replay = 1
  elif playerChoice == 1 and computerChoice == 2:
    print("Player chose paper. Computer chose scissors. Scissors cut paper. Computer wins.")
    replay = 1
  elif playerChoice == 1 and computerChoice == 3:
    print("Player chose paper. Computer chose lizard. Lizard eats paper. Computer wins.")
    replay = 1
  elif playerChoice == 1 and computerChoice == 4:
    print("Player chose paper. Computer chose spock. Paper disporves spock. Player wins.")
    replay = 1

  if playerChoice == 2 and computerChoice == 0:
    print("Player chose scissors. Computer chose rock. Rock crushes paper. Computer wins.")
    replay = 1
  elif playerChoice == 2 and computerChoice == 1:
    print("Player chose scissors. Computer chose paper. Scissors cut paper. Player wins.")
    replay = 1
  elif playerChoice == 2 and computerChoice == 3:
    print("Player chose scissors. Computer chose lizard. Scissors decapites lizard. Player wins.")
    replay = 1
  elif playerChoice == 2 and computerChoice == 4:
    print("Player chose scissors. Computer chose spock. Spock smashes scissors. Computer wins.")
    replay = 1
#all results of player choosing lizard
  if playerChoice == 3 and computerChoice == 0:
   print("player chose lizard. Computer chose rock. Rock crushes lizard. Computer win.")
   replay = 1  
  elif playerChoice == 3 and computerChoice == 1:
    print("Player chose lizard. Computer chose paper. Lizard eats paper. Player win.")
    replay = 1
  elif playerChoice == 3 and computerChoice == 2:
    print("Player chose lizard. Computer chose scissors. Scissors decapites lizard. Computer win.")
    replay = 1
  elif playerChoice == 3 and computerChoice == 4:
    print("Player chose lizard. Computer chose spock. Lizard poisons spock. Player win.")
    replay = 1
#all results of player choosing spock
  if playerChoice == 4 and computerChoice == 0:
    print("Player chose spock. Computer chose rock. Spock vaporises rock. Player wins.")
    replay = 1
  elif playerChoice == 4 and computerChoice == 1:
    print("Player chose spock. Computer chose paper. Paper disproves spock. Computer wins.")
    replay = 1
  elif playerChoice == 4 and computerChoice == 2:
    print("Player chose spock. Computer chose scissors. Spock smashes scissors. Player wins. ")
    replay = 1
  elif playerChoice == 4 and computerChoice == 3:
    print("Player chose spock. Computer chose lizard. The lizard posions the spock. Computer wins.")
    replay = 1