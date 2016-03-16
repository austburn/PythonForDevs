f = open('/home/austin/learning/PythonForDevs/LabsData/temps.dat', 'r')
o = open('/home/austin/learning/PythonForDevs/LabsData/temps_out.dat', 'w')

for l in f:
    try:
        farenheit = float(l)
    except ValueError:
        o.write('{} was not a float.\n'.format(l.rstrip()))
        continue

    centigrade = (5.0/9.0)*(farenheit - 32)

    o.write('{:.1f}F is {:.1f}C.\n'.format(farenheit, centigrade))

f.close()
o.close()
