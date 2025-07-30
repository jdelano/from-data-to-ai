import pandas as pd
df = pd.read_csv(
	"data.csv",
	sep=";",
	usecols=["Date", "Sales", "Region"],
	parse_dates=["Date"]
)