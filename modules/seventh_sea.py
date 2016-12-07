from random import randint

def name() : return "7th Sea"

def roll(dices = 6):
  values = []
  for i in range(dices):
    values.append(randint(1,10))
  return values

def roll_easy():
  return 1 if roll(7) > 10 else 0

def roll_average():
  return 1 if roll(7) > 15 else 0

def roll_hard():
  return 1 if roll(7) > 20 else 0


def success(values):
  values.sort()

  result = []
  high = 0
  while len(values) != 0:
    high = values.pop(len(values)-1)

    if high == 10:
      result.append(high)
      continue

    accum = [high]

    while sum(accum) < 10 and len(values) != 0:
      tempHigh = 0
      j = 0
      found = False
      for j, tempHigh in enumerate(values):
        if sum(accum) + tempHigh >= 10:
          accum.append(values.pop(j))
          found = True
          break

      if not found:
          accum.append(values.pop(j))

      if sum(accum) >= 10:
        result.append(accum)

  return result
