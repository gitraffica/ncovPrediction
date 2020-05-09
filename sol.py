import DataPrepare as DP
import NN
import matplotlib.pyplot as plt

data = DP.LoadData('data.csv')

size = 30

confirmed = DP.GetConfirmed(data, size)
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
confirmedNN.train()
validation = confirmedRate[30]
x = confirmedNN.predict([validation])
validation.append(x)
plt.plot(validation)
plt.show()