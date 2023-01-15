import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy.fftpack

# pandas offical documentation : https://pandas.pydata.org/docs/
# get your data with the correct function pd.read_format_file("absolute/path/to/your/file", sep= "<separator used in file>)
# note tabular file sep = "\t"
data = pd.read_csv("test\Values.csv", sep=",")
# print your data cause why not, use head() for begin only
print(data)

# in case of a multiple column csv change the name of your x variable and add in the list the data you want to draw in function of x: 
# data.plot(x="Distance_(pixels)",y=["Gray_Value"])
# plt.show()

# manipulate data ex : inverse FFT 
x = data["Distance_(pixels)"]
N = len(x)
value = np.array(data["Gray_Value"])
T = 1
fft_data = scipy.fftpack.fft(value)
fft_norm = abs(fft_data)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
# add a new column in dataframe
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * fft_norm[:N//2])
plt.show()
data["fft"] = fft_norm

print(data)