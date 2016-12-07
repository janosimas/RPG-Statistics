from random import randint

def name() : return "FATE"

def roll(mod = 0):
  accum = 0
  for i in range(0, 4):
    accum += randint(-1,1)
  return accum+mod

def roll_easy():
  return 1 if roll(4) > 2 else 0

def roll_average():
  return 1 if roll(4) > 3 else 0

def roll_hard():
  return 1 if roll(4) > 4 else 0

