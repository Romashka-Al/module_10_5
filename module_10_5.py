import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f1:
        for line in f1:
            all_data.append(*line.split())


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
#time_start1 = datetime.now()
#for file in files:
#    read_info(file)
time_start2 = datetime.now()
#print(time_start2 - time_start1)
#0:00:09.629370

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    print(datetime.now() - time_start2)
#0:00:03.741010