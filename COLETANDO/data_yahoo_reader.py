from pandas_datareader import data
from datetime import datetime
import matplotlib.pyplot as plt

lista = ["IBOV", "BVMF3"]
startDate = datetime(2017,11,1)
endDate = datetime(2018,10,15)

instrument = data.DataReader(lista, 'yahoo', startDate, endDate)
close = instrument['Adj Close']

print(close)

#plt.bar(close)
#plt.show()