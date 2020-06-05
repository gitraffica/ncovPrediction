import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import *
import pandas as pd 
import DataPrepare as DP

#筛选数据
def FiltData(oridata):
    ptr1,ptr2 = 0,0
    while ptr2 < oridata.__len__():
        if oridata[ptr2][-2].ConfirmedData >= 500:
            oridata[ptr1] = oridata[ptr2]
            ptr1 = ptr1 + 1
        ptr2 = ptr2 + 1
    return oridata[0:ptr1]


def GetCF(data) :
    res = []
    for i in data:
        res.append(i.ConfirmedData)
    return res

def GetRe(data) :
    res = []
    for i in data:
        res.append(i.RecoverData)
    return res

def GetDe(data) :
    res = []
    for i in data:
        res.append(i.DeathData)
    return res


def SplineData(DiltedData, times = 2) -> list:
    res = []
    for i in range(DiltedData.__len__()) :
        conf = GetCF(DiltedData[i])
        rec  = GetRe(DiltedData[i])
        dea  = GetDe(DiltedData[i])
        datal = conf.__len__()
        base = np.linspace(0,datal+1,datal+2)
        splc = BSpline(base,conf,times)
        splr = BSpline(base,rec,times)
        spld = BSpline(base,dea,times)
        base2 = np.linspace(1,datal-1,datal*10)
        conf_,rec_,dea_ = splc(base2),splr(base2),spld(base2)
        ret = []
        for j in range(0,conf_.__len__()):
            x = DP.Data()
            x.ConfirmedData = conf_[j]
            x.RecoverData   = rec_[j]
            x.DeathData     = dea_[j]
            x.AreaName      = DiltedData[i][0].AreaName
            ret.append(x)
        res.append(ret)
    return res

if __name__ == '__main__':
    data = DP.LoadData('data.csv')
    data = FiltData(data)
    Sdata = SplineData(data)
    print(Sdata[0][1040].RecoverData)