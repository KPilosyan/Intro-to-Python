import matplotlib.pyplot as p
import pandas as pd

s = pd.read_csv('anomalies.csv')
y = s[s['value']>6] 
x = y.index[0]

p.plot(s, color = "blue")
p.scatter(x,y, color = "red")
p.show()