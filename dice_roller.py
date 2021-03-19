import random

def main():
    dice_roll = int(input('How many dice? '))
    dice_size = int(input('Dice size? '))
    sum_roll = 0
    for i in range(0, dice_roll):    
        roll = random.randint(1,dice_size)
        sum_roll += roll
        print(f'You random {roll}')
        if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
        else:
          print(f'You rolled a {roll}')
          print(f'Sum: {sum_roll}')

if __name__== "__main__":
  main()

