from random import randint

outcomes = 13 * [0]

for i in range(10000):
    die_one = randint(1, 6)
    die_two = randint(1, 6)

    outcomes[die_one + die_two] += 1

for j in outcomes:
    print '{0:.3%}'.format(float(j)/10000)
