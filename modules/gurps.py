from random import randint

def name() : return "Gurps"

def roll():
    accum = 0
    for i in range(0, 3):
        accum += randint(1,6)
    return accum

def roll_easy():
  return 1 if roll() < 15 else 0

def roll_average():
  return 1 if roll() < 13 else 0

def roll_hard():
  return 1 if roll() < 11 else 0
