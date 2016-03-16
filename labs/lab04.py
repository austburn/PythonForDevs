"""
Print a multiplication table
"""

print 'multiplication table'

for x in range(1, 11):
    for y in range(1, 11):
        val = x * y
        print '{:2}'.format(val),
    print ''
