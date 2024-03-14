import pandas as pd
df = pd.read_csv("../../parte_DSI/Aula_3_introducao_pandas/nba.csv")

#creating new column from an existing one
df["monthlySalary"] = df["Salary"]/12
df["monthlySalary"] = round(df["monthlySalary"])

df["Test"] = 0
newdf = pd.read_csv("../../parte_DSI/Aula_3_introducao_pandas/nba.csv")

#add line
df.loc[458] = ["teste", 3, 3, 4, 5, 6, 7, 5, 7, 6, 9]
df.loc[459] = [3, 3, 3, 4, 5, 6, 7, 5, 7, 6, "teste"]
print("ADDED ROWS", df.tail())

#kill line
killed_rows_df = df.drop(index = [row for row in df.index if "teste" == str(df.loc[row, :])])
print("DELETED ROWS", killed_rows_df.tail())

#highest paid players
task1 = df[["Name", "Team", "Salary"]].nlargest(10, columns=["Salary"])
print("TASK 1", task1)

#height and weight conversion
task4 = df
task4["Height"] = task4["Height"].str.split("-")
for item in task4["Height"]:
    item[0] = float(item[0])*30.48
    item[1] = float(item[1])*2.54
    item = item[0]+item[1]
print("TASK 4", task4[["Name", "Height"]])

#median of salaries by position
task3 = df.groupby(["Position"])["Salary"].mean()
print("TASK 3", task3)
