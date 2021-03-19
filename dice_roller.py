import random

def main():
    dice_roll = 10
    sum_roll = 0
    for i in range(0, dice_roll):    
        roll = random.randint(1,6)
        sum_roll += roll
        print(f'You random {roll}')
    print(f'Sum: {sum_roll}')

if __name__== "__main__":
  main()

