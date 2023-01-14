import pandas as pd 
import matplotlib.pyplot as plt


# get your data with the correct function :
# pd.read_format_file("absolute/path/to/your/file", 
#                      sep= "<separator used in file>
#                       )
# note : tabular file sep = "\t"

data = pd.read_csv("test\Values.csv", sep=",")

# print your data cause why not, use head() for begin only
print(data)

# in case of a multiple column csv change the name of your x variable and add in the list the data you want to draw in function of x: 
data.plot(x="Distance_(pixels)",y=["Gray_Value"])
plt.show()
