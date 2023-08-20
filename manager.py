import mysql.connector as sql
    
class Manager:
    def __init__(self):
        self.db = sql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="company")
        self.cur = self.db.cursor()

    # enter data of today manufacturing =========================================================
    def enter_data(self):
        try:
            day = int(input("Enter date: "))
            month = int(input("Enter month: "))
            com_code = input("Enter company code: ")
            # verify day and month
            go = 0
            if day>=1 and day<=31:
                if month>=1 and month<=12:
                    go = 1
                else:
                    print("Sir, you enter wrong month number.It should be from (01) to (12)")
            else:
                print("Sir, you enter wrong day number.It should be from (01) to (31)")
            # if day and month correct then enter in this if statement
            if go==1:
                # verify that employee exist in company or not
                query = f"select * from employee_manager_data where company_code='{com_code}'"
                self.cur.execute(query)
                check = 0
                for row in self.cur:
                    print(f"Name of employee : {row[1]} ___ ",end="")
                    check = 1
                # if employee not exist in company
                if check==0:
                    print("")
                    print(f"Employee with company code ({com_code}) not exist in company.Try again!")
                # if employee exist in company
                else:
                    work = int(input())
                    # now verify that data should not be duplicated 
                    query = f"select * from today_manufacturing where day={day} and month={month} and company_code='{com_code}'"
                    check2 = 0
                    self.cur.execute(query)
                    for row in self.cur:
                        check2 = 1
                    # if data duplicate
                    if check2==1:
                        print(f"ERROR ::: You already enter today work of Employee ({com_code}).If you enter wrong data then use option 2 to edit the data.")
                    # if data not duplicate
                    else:
                        query = f"insert into today_manufacturing values ({day},{month},'{com_code}','{work}')"
                        self.cur.execute(query)
                        self.db.commit()
                        print("Data successfully added")
            
        except ValueError:
            print("ERROR ::: It seems you enter alphabet instead of number or may be that you leave the field empty")

    # see today enter data =====================================================================
    def see_data(self):
        day = int(input("Enter day : "))
        month = int(input("Enter month : "))
        go = 0
        if day>=1 and day<=31:
            if month>=1 and month<=12:
                go = 1
            else:
                print("Sir, you enter wrong month number.It should be from (01) to (12)")
        else:
            print("Sir, you enter wrong day number.It should be from (01) to (31)")
        if go==1:
            query = f"select * from today_manufacturing where day={day} and month={month}"
            self.cur.execute(query)
            a = 1
            print(f"Sr# ... Day ... Month ... Company_code ... Work")
            for row in self.cur:
                print(f"{a} ... {row[0]} ... {row[1]} ... {row[2]} ... {row[3]}")
                a += 1
            print(f"\nYou put data of {a-1} employee in this day({day}) of month({month})\n")

    # edit data for today manufacturing =========================================================
    def edit_data(self):
        try:
            print("You can only edit work of employee")
            # input company code
            print("Enter company code of employee: ",end="")
            com_code = input("")
            check = 0
            # check whether employee exist in company or not
            query = f"select * from employee_manager_data where company_code='{com_code}'"
            self.cur.execute(query)
            for row in self.cur:
                print(f"Name of employee is : ({row[1]})")
                check = 1
            # if employee exist in company
            if check == 1:
                a = 1
                dictionary = dict()
                query = f"select * from today_manufacturing where company_code='{com_code}'"
                self.cur.execute(query)
                print("Sr# ... Day ... Month ... Work")
                see = False
                for row in self.cur:
                    dictionary[f"{a}"] = f"{row[0]},{row[1]},{row[2]},{row[3]}"
                    print(f"{a} .... {row[0]} ... {row[1]} ... {row[3]}")
                    a+=1
                    see = True
                # if serial number is correct
                if see==True:
                    print("Enter the (serial number) of row which you want to edit : ")
                    num = input("")
                    for i in dictionary:
                        if num==i:
                            day = int(input("Enter day : "))
                            month = int(input("Enter month : "))
                            work = int(input("Enter work : "))
                            go = 0
                            if day>=1 and day<=31:
                                if month>=1 and month<=12:
                                    go = 1
                                else:
                                    print("Sir, you enter wrong month number.It should be from (01) to (12)")
                            else:
                                print("Sir, you enter wrong day number.It should be from (01) to (31)")
                            if go==1:
                                find = dictionary[i]
                                individual = find.split(",")
                                # updating data
                                query = f"update today_manufacturing set day={day},month={month},work='{work}' where day={int(individual[0])} and month={int(individual[1])} and company_code='{individual[2]}' and work='{individual[3]}'"
                                self.cur.execute(query)
                                self.db.commit()
                                print("Record successfully updated")
                # if serial number is wrong
                else:
                    print("ERROR ::: You enter wrong serial number.Try again with correct information!")
            # if employee not exist in compny
            else:
                print("ERROR ::: You cannot edit data because employee not exist in company. Make sure you put right")
        except ValueError:
            print("ERROR ::: It seems you enter alphabet instead of number or may be that you leave the field empty")

