print '/home/austin/learning/PythonForDevs/LabsData/tmpprecip2012.dat'
print '*' * 60

with open('/home/austin/learning/PythonForDevs/LabsData/tmpprecip2012.dat') as f:
    data = {}
    for data_point in f:
        month = data_point[0:2]
        temp = data_point[13:16]

        try:
            month = int(month)
        except ValueError:
            print 'Bad month:', month
            continue

        try:
            temp = int(temp)
        except ValueError:
            print 'Bad temp:', temp
            continue

        if month not in data:
            data[month] = []

        data[month].append(temp)

    for m, temps in data.iteritems():
        print '{:2d} {:4f} {:4d} {:4d}'.format(m, float(sum(temps))/len(temps), max(temps), min(temps))

print '\n'
print '/home/austin/learning/PythonForDevs/LabsData/tmpprecip.dat'
print '*' * 60
with open('/home/austin/learning/PythonForDevs/LabsData/tmpprecip.dat') as f:
    data = {}
    for data_point in f:
        month = data_point[0:2]
        temp = data_point[13:16]

        try:
            month = int(month)
        except ValueError:
            print 'Bad month:', month
            continue

        try:
            temp = int(temp)
        except ValueError:
            print 'Bad temp:', temp
            continue

        if month not in data:
            data[month] = []

        data[month].append(temp)

    for m, temps in data.iteritems():
        print '{:2d} {:4f} {:4d} {:4d}'.format(m, float(sum(temps))/len(temps), max(temps), min(temps))
