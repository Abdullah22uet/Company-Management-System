import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector as sql

class Employee:
    def __init__(self):
        self.db = sql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="company")
        self.cur = self.db.cursor()

    def password(self , com_code , password):
        query = f"select * from passwords where company_code='{com_code}' and password='{password}'"
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            check = 1
        if check==0:
            print("Invalid company code or password")
        else:
            month = int(input("Enter month : "))
            year = int(input("Enter year : "))
            check2 = 0
            if month>=1 and month<=12:
                if len(str(year))==4:
                    check2 = 1
                else:
                    print("Year value must consist of (4) digits.Try again!")
            else:
                print("Month value is wrong. It should be from (01) to (12).Try again!")

            if check2==1:
                query = f"select * from montly_manufacturing where month={month} and year={year} and company_code='{com_code}'"
                self.cur.execute(query)
                for row in self.cur:
                    print("")
                    print(f"Company code : {row[2]}")
                    print(f"Working : {row[3]}")
                    print(f"Total Salary : {row[4]}")

                sure = input("Are you want to see graphical representation? (Y/N) : ")
                if sure=="Y":
                    # query = 
                    df = pd.read_sql_query(f"select * from montly_manufacturing where year={year} and company_code='{com_code}' order by month asc" , self.db)
                    a = sns.barplot(x="month",y="work",data=df,palette="rainbow_r")
                    for bar in a.containers:
                        a.bar_label(bar)
                    plt.title(f"Year({year}) Performance of Employee({com_code})")
                    plt.show()



