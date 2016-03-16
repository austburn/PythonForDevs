with open('/home/austin/learning/PythonForDevs/LabsData/trees.dat') as f:
    trees = []
    for tree in f:
        try:
            h = int(tree)
        except ValueError:
            print 'Bad Data: {}'.format(tree)
        else:
            trees.append(h)

    tallest = max(trees)
    shortest = min(trees)
    avg_height = float(sum(trees))/len(trees)

    print 'Tallest Tree: {}'.format(tallest)
    print 'Shortest Tree: {}'.format(shortest)
    print 'Avg Tree Height: {0:.2f}'.format(avg_height)
