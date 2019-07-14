import os
import csv


class PrepareResources:
    path = './assets/'
    tsp_path = './tsp_problem/'

    def __init__(self):

        # Se non esiste la cartella in cui sto per inserire i tweet filtrati la creo
        if not os.path.exists(self.tsp_path):
            os.makedirs(self.tsp_path)

        # Per ogni file nella cartella assets/filtered-tweet
        for filename in os.listdir(self.path):
            print(filename)

            with open("./assets/" + filename, 'r') as f:
                data = f.read().split('\n')

            data = data[data.index('NODE_COORD_SECTION') + 1: data.index('EOF')]

            w = csv.writer(open(self.tsp_path + filename.split(".")[0] + ".csv", "w+"))
            for d in data:
                if d is "EOF":
                    break
                else:
                    w.writerow(d.strip(" ").split())


if __name__ == '__main__':
    PrepareResources()
