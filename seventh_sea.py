from random import randint


values = []
for i in range(10):
  values.append(randint(1,10))

print(values)
values.sort()
print(values)

result = []

for i, high in enumerate(values[::-1]):
  print(i, high)
  values.pop(i)

  if high == 10: result.append(high)
  for j, low in enumerate(values):
    if high + low >= 10:
      values.pop(j)
      result.append([high, low])
      break

print(result)