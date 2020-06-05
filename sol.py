import DataPrepare as DP
import NN
import matplotlib.pyplot as plt
import numpy as np
import spliner as sp

data = DP.LoadData('data.csv')
data = sp.SplineData(data, 3)

size = 700

confirmed = np.array(DP.GetConfirmed(data, size))
#confirmed = np.array(DP.GetDeath(data, size))
confirmedRate = DP.GetRate(confirmed, size)
plt.plot(confirmed[800])
plt.plot(np.array(confirmedRate[800]) * 50)
plt.show()

confirmedNN = NN.NN(confirmedRate, Units = 256)
#confirmedNN.load('Deathmodel.300-0.01.h5')
confirmedNN.load('model.300-0.03.h5')
#confirmedNN.train()
confirmedRate = np.array(confirmedRate)

ncovdata = DP.LoadData('datancov.csv')
ncovdata = sp.SplineData(ncovdata, 1)
ncovconfirmed = np.array(DP.GetDeath(ncovdata, size))
ncovRate = np.array(DP.GetRate(ncovconfirmed, size))
validation = np.array([ncovRate[0, :-1]])
result = validation
curve = np.array([ncovconfirmed[660, :-1]])[-1]
plt.plot(curve)
plt.show()
for i in range(8000):
    validation = np.reshape(validation, (validation.shape[0], 1, validation.shape[1]))
    x = confirmedNN.predict(validation)
    result = np.append(result, x)
    validation = np.array([result[-(size - 4):]])
    curveNow = (result[-1] * curve[-2] - 4 * curve[-1] + 2 * curve[-2]) / (result[-1] - 2)
    #curveNow = 2 * result[-1] * curve[-1] + curve[-2]
    #print(result, curveNow)
    curve = np.append(curve, curveNow)
    if curveNow < 0:
        break
print(curve)
print(result)
#plt.plot(range(1, 401))
plt.xticks(np.arange(0, 4000, step=200), np.arange(0, 400, step=20))
plt.plot(result * 5000)
plt.plot(curve)
plt.show()