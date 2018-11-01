from pandas_datareader import data
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


lista = ["NYA", "NEXA"]
startDate = datetime(2017,11,1)
endDate   = datetime(2018,10,14)

instrument = data.DataReader(lista, 'yahoo', startDate, endDate)
close = instrument['Adj Close']
print(close)

def compute_daily_returns(df):
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.iloc[0, :] = 0
    return daily_returns

dlyRtns = compute_daily_returns(close)
xPlt = dlyRtns[lista[0]]
yPlt = dlyRtns[lista[1]]

dlyRtns.plot(x=lista[0], y=lista[1], marker='o', linewidth=0)
#plt.show()

#calculate linear regression
beta_yPlt, alpha_yPlt = np.polyfit(xPlt, yPlt, 1)  # fit poly degree 1
print("Beta:" + str(beta_yPlt))
print("Alpha:" + str(alpha_yPlt))
plt.plot(xPlt, beta_yPlt * xPlt + alpha_yPlt, '-', color='red')
plt.show()