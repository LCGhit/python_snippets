import pandas as pd

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
    return table

def menu(table):
    menuChoice = ""
    while (menuChoice != "4"):
        menuChoice = input("What woud you like to do?\n1 New entry\n2 Show expenses\n3 Current month's total\n4 Exit\n=>")
        match menuChoice:
            case "1":
                currentTable_df = newEntry(table)
            case "2":
                try:
                    print("Current expenses", table)
                except:
                    print("No expenses yet")
            case "3":
                total = 0
                dataframeColList = list(table[table["month"] == last_entry_month]["amount"])
                for i in dataframeColList:
                    total += int(i*100)
                    print(total/100)
            case "4":
                print("Exited\n")
            case _:
                print("Invalid input\n=>")


try:
    currentTable_df = pd.read_csv("exp.csv", index_col=[0])
    currentTable_df = pd.DataFrame(currentTable_df)
    last_entry_month = currentTable_df["month"].max()
    last_entry_year = currentTable_df["year"].max()
    menu(currentTable_df)
except:
    currentTable_df = pd.DataFrame
