import string

with open('/home/austin/learning/PythonForDevs/LabsData/alice_in_wonderland.dat') as f:
    aiw = f.read()
    total_chars = 0
    es = 0

    for char in aiw:
        if char in string.letters:
            total_chars += 1

        if char == 'e':
            es +=1

    print '{0:.0%}'.format(float(es)/float(total_chars))
