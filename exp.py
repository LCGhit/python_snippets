import pandas as pd

try:
    currentTable_df = pd.read_csv("exp.csv", index_col=[0])
except:
    currentTable_df = ""

currentTable_df = pd.DataFrame(currentTable_df)
last_entry_month = currentTable_df["month"].max()
last_entry_year = currentTable_df["year"].max()
def newEntry(table):
    addEntry = "y"
    while addEntry == "y":
        newEntry = {"year":input("what's the year(Press ENTER for " + str(last_entry_year) + ")\n=>"), "month":input("what's the month?(Press ENTER for " + str(last_entry_month) + ")\n=>"), "category":input("what's the category\n=>"), "amount":input("=>what's the amount\n=>")}
        newEntry["year"] = last_entry_year if newEntry["year"] == "" else newEntry["year"]
        newEntry["month"] = last_entry_month if newEntry["month"] == "" else newEntry["month"]

        newEntry_df = pd.DataFrame([newEntry])
        print(newEntry_df)
        if input("\nIs this correct? (y/n) =>") == "y":
            if isinstance(table, pd.DataFrame):
                newTable_df = pd.concat([newEntry_df, table], ignore_index=True)
                print("the new table\n",newTable_df)
                newTable_df.to_csv("exp.csv")
                table = pd.read_csv("exp.csv", index_col=[0])
                addEntry = input("Another entry?(y/n) =>\n")
            else:
                newEntry_df.to_csv("exp.csv")
                table = pd.read_csv("exp.csv", index_col=[0])
                addEntry = input("Another entry?(y/n) =>\n")
        else:
            print("Operation cancelled")
            addEntry = input("Another entry?(y/n) =>\n")
            if addEntry == "y":
                continue
            elif addEntry == "n":
                break
            else:
                print("invalid input")
    return table

menuChoice = ""
while (menuChoice != "4"):
    menuChoice = input("What woud you like to do?\n1 Show current expenses\n2 New entry\n3 Current month's total\n4 Exit\n=>")
    match menuChoice:
        case "1":
            try:
                print("Current expenses", currentTable_df)
            except:
                print("No expenses yet")
        case "2":
            currentTable_df = newEntry(currentTable_df)
        case "3":
            total = 0
            dataframeColList = list(currentTable_df[currentTable_df["month"] == last_entry_month]["amount"])
            for i in dataframeColList:
                total += float(i)
            print(total)
        case "4":
            print("Exited\n")
        case _:
            print("Invalid input\n=>")
