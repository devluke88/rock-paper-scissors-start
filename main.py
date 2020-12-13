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

human_choice = input("Provide a answer. ").lower()
game_list = ['rock', 'paper', 'scissors']
human_num = game_list.index(human_choice)
lista = [rock, paper, scissors]
print(f"Human choice is: {lista[game_list.index(human_choice)]}")
computer_num = random.randint(0,2)
print(f"Computer choice is: {lista[computer_num]}")
if human_num == 0 and computer_num == 2:
  print("you win!")
elif human_num == 1 and computer_num == 0:
  print("you win!")
elif human_num == 2 and computer_num == 1:
  print("you win!")
elif human_num == computer_num:
  print("draw")
else:
  print("you loose!")