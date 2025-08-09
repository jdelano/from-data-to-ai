import pandas as pd
df = pd.read_csv(
	"Chapter02/data.csv",
	sep=";",
	usecols=["Date", "Sales", "Region"],
	parse_dates=["Date"]
)