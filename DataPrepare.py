import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class AllData:

    def Data(self):
        self.ConfirmedData =    []
        self.DeathData =        []
        self.RecoverData =      []
        self.AreaName =         []

class Data:

    def Data(self):
        self.ConfirmedData =    0
        self.DeathData =        0
        self.RecoverData =      0
        self.AreaName =         ''

def LoadData(filename):
    df = pd.read_csv(filename, header=None)
    data = df.values
    res = AllData()
    res.ConfirmedData   = data[:, 2][1:]
    res.ConfirmedData   = res.ConfirmedData.astype('float32')
    res.DeathData       = data[:, 4][1:]
    res.DeathData       = res.DeathData.astype('float32')
    res.RecoverData     = data[:, 6][1:]
    res.RecoverData     = res.RecoverData.astype('float32')
    res.AreaName        = data[:,12][1:]
    arr = []
    dic = {}
    now = []
    #print(res.ConfirmedData.shape)
    for _ in range(res.ConfirmedData.shape[0]):
        if res.AreaName[_] in dic:
            x = Data()
            x.ConfirmedData = res.ConfirmedData[_]
            x.DeathData     = res.DeathData[_]
            x.RecoverData   = res.RecoverData[_]
            x.AreaName      = res.AreaName[_]
            now.append(x)
        else:
            dic[res.AreaName[_]] = 1
            if len(now) != 0:
                arr.append(now)
            now = []
    arr.append(now)
    return arr

def Patch(data, size):
    data = [0] * (size - len(data)) + data
    return data

#This will return a (size-2) shape vector, where each element is (df\dx) \ (d^2 f \ dx^2)
def GetRate(data, size):
    ret = []
    res = []
    for i in range(len(data)):
        for j in range(1, size - 2):
            deri1 = (data[i][j+1] - data[i][j-1]) / 2
            deri2 = (data[i][j+1] - data[i][j]) - (data[i][j] - data[i][j-1])
            if deri1 == 0:
                res.append(0)
            else:
                res.append(deri2 / deri1)
        ret.append(res)
        res = []
    return ret

def GetConfirmed(data, size):
    res = []
    for i in range(len(data[0])):
        res.append(data[0][i].ConfirmedData)
    ret = []
    for i in range(len(data[0]) - size):
        ret.append(Patch(res[max(0, i-size):i], size))
    return ret

if __name__ == "__main__":
    LoadData('data.csv')