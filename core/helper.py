def reader(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            url = line.strip('\r').strip('\n')
            if not url:
                continue
            data.append(url)

    return data