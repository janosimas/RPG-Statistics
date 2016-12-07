import modules.d20 as d20
import modules.fate as fate
import modules.gurps as gurps

from scipy import stats

modules = []
modules.append(d20)
modules.append(fate)
modules.append(gurps)

for module in modules:
    print(module.name())

    rolls = []
    for i in range(0,50000):
        rolls.append(module.roll())

    print(stats.describe(rolls))

    easy = []
    for i in range(0,50000):
        easy.append(module.roll_easy())

    print(stats.describe(easy))

    average = []
    for i in range(0,50000):
        average.append(module.roll_average())

    print(stats.describe(average))

    hard = []
    for i in range(0,50000):
        hard.append(module.roll_hard())

    print(stats.describe(hard))