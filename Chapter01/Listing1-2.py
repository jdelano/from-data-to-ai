import pandas as pd  #Creates an alias for pandas named pd 
df = pd.read_csv("students-1252.csv", dtype={"Name":"string"}, encoding="latin1") #Reads in the file
print(df.head()) #Displays the file
df.info() #Displays the information about the file
print(df.describe()) #Displays the descriptive statistics of the file
