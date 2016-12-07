from random import randint

def name() : return "D20"

def roll(mod = 0):
  return randint(1,20)+mod

def roll_easy():
  return 1 if roll(7) > 10 else 0

def roll_average():
  return 1 if roll(7) > 15 else 0

def roll_hard():
  return 1 if roll(7) > 20 else 0