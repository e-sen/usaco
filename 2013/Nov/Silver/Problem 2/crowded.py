with open('crowded.in') as fw:
    sample = fw.read()
    lines = map(lambda x: map(lambda y: int(y), x.split(' ')), sample.split('\n'))
    N = lines[0][0]
    D = lines[0][1]
    lineSlice = slice(1, 1 + N)
    cows = sorted(lines[lineSlice], key=lambda x: x[0])

    # 2..1+N
    for cow in cows:
        xi = cow[0]
        hi = cow[1]
        print "xi:", xi, "hi:", hi

    # input format finished.
