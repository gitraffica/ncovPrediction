import DataPrepare as DP
import NN
import matplotlib.pyplot as plt
import numpy as np

data = DP.LoadData('data.csv')

size = 30

confirmed = np.array(DP.GetConfirmed(data, size))
confirmedRate = DP.GetRate(confirmed, size)
'''
for i in range(len(confirmedRate)):
    plt.plot(confirmedRate[i])
    plt.show()
plt.plot(confirmed)
plt.show()
print(confirmedRate)
'''
confirmedNN = NN.NN(confirmedRate)
confirmedNN.load('model.10000-0.07.h5')
#confirmedNN.train()
confirmedRate = np.array(confirmedRate)
validation = np.array([confirmedRate[30, :-1]])
result = validation
curve = np.array([confirmed[30, :-1]])[0]
for i in range(30):
    validation = np.reshape(validation, (validation.shape[0], 1, validation.shape[1]))
    x = confirmedNN.predict(validation)
    result = np.append(result, x)
    '''
    print("valid")
    print(validation)
    print("result")
    print(result)
    print(x)
    '''
    validation = np.array([result[-(size - 4):]])
    curveNow = (result[-1] * curve[-2] - 4 * curve[-1] + 2 * curve[-2]) / (result[-1] - 2)
    curve = np.append(curve, curveNow)
print(curve)
plt.plot(result * 40000)
plt.plot(curve)
plt.show()