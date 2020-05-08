import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Data:

    def Data(self):
        self.ConfirmedData =    []
        self.DeathData =        []
        self.RecoverData =      []
        self.AreaName =         ''

def LoadData(filename):
    df = pd.read_csv(filename, header=None)
    data = df.values
    res = Data()
    res.ConfirmedData   = data[:, 2][1:]
    res.ConfirmedData   = res.ConfirmedData.astype('float32')  # confirm the type as 'float32'
    res.DeathData       = data[:, 4][1:]
    res.DeathData       = res.DeathData.astype('float32')  # confirm the type as 'float32'
    res.RecoverData     = data[:, 6][1:]
    res.RecoverData     = res.RecoverData.astype('float32')  # confirm the type as 'float32'
    res.AreaName        = data[:,12][1:]
    plt.title('original data')
    plt.plot(res.ConfirmedData)
    plt.savefig('original data.png')
    plt.show()
    print(res.AreaName)
    '''
    result = []
    for index in range(len(data) - time_step):
        result.append(data[index:index + time_step + 1])
        '''
    return res

if __name__ == "__main__":
    LoadData('data.csv')