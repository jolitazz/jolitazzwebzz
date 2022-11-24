import random


def rock_paper_scissors():

print("Lets play Rock Paper Scissors")

r= "rock"
p= "paper"
s= "scissors"
all_choices = [r,p,s]
user= input(f"Enter a choice ({r}, {p}, {s}: ")

if user not in all_choices:
    print("Invalid choice")
    return
computer = random.choices(all_choices)

print(f"User chose{user}, computer chose {computer}"

      # r>s, p>r, s>p

if user == computer
      print("Tie")