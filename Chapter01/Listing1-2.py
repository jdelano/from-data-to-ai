import pandas as pd  #Creates an alias for pandas named pd 
df = pd.read_csv("Chapter01/students.csv") #Reads in the file
print(df.head()) #Displays the first few lines of the file