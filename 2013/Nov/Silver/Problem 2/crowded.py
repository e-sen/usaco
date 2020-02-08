with open('crowded.in') as fw:
    sample = fw.read()
    lines = map(lambda x: x.split(' '), sample.split('\n'))
    N = int(lines[0][0])
    D = int(lines[0][1])



    # 2..1+N
    for i in range(1, 1 + N):
        print i
        xi = lines[i][0]
        hi = lines[i][1]

    # input format finished.
