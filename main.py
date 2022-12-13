import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you want to choose:")
print("Type 0 for rock")
print("Type 1 for paper")
a = int(input("Type 2 for scissors\n"))

b = random.randint(0,2)

hand = [rock,paper,scissors]
if(a==b):
  print(f"You chose {a}")
  print(hand[a])
  print(f"System chose {b}")
  print(hand[b])
  print("That's a TIE")
elif( (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0) ):
  print(f"You chose {a}")
  print(hand[a])
  print(f"System chose {b}")
  print(hand[b])
  print("System WINS !")
elif( (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1) ):
  print(f"You chose {a}")
  print(hand[a])
  print(f"System chose {b}")
  print(hand[b])
  print("You WIN !")
else:
  print("You didn't chose a number between 0 and 2")
