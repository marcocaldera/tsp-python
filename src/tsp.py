class Tsp:

    def __init__(self):
        with open("./assets/a280.tsp", 'r') as f:
            data = f.read().split('\n')
        data = data[data.index('NODE_COORD_SECTION') + 1: data.index('EOF')]

        for d in data:
            if d is "EOF":
                break
            else:
                print d

        # for line in f:
        #     # print line
        #     if "NAME : " in line:
        #         print line.strip('NAME : ')


if __name__ == '__main__':
    Tsp()
