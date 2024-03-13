import pandas as pd

nba_df = pd.read_csv("../../parte_DSI/Aula_3_introducao_pandas/nba.csv")

# dataframe withou NaN values
df_no_NaN = nba_df.dropna()

# change NaN in given column with given value
nba_df["College"] = nba_df["College"].fillna("not available")

print(nba_df[nba_df["College"] == "not available"])
print(nba_df[nba_df["Weight"] > 270])

print("ENTRIES BY TEAM", nba_df['Team'].value_counts())

# sort by team and name
print("SORT BY TEAM(DESCENDING) AND NAME (ASECENDING)", nba_df.sort_values(["Team", "Name"], ascending=[0,1]))

# two conditions
print("TWO CONDITIONS", nba_df[(nba_df["Team"] == "Los Angeles Lakers") | (nba_df["Team"] == "Los Angeles Clippers")])
print("FIRST 20 ENTRIES", nba_df["College"][1:20:4])


# see difference with groupby
print("THE MEAN")
print(nba_df["Salary"].mean())
print(nba_df.groupby("Salary").mean())


print("COUNT NULL ELEMENTS BY COLUMN", nba_df.isnull().sum())
