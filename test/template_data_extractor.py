import pandas as pd 

# get your data with the correct function pd.read_format_file("absolute/path/to/your/file", sep= "<separator used in file>)
# note tabular file sep = "\t"
data = pd.read_csv("test\Values.csv", sep=",")
# print your data cause why not, use head() for begin only
print(data)
