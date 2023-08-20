import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector as sql

# owner verification class is here =======================================================================
class Owner_verification:
    def __init__(self):
        self.db = sql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="company")
        self.cur = self.db.cursor()
# add data verification ===========================================================
    def add_data_v(self,com_code,name,cnic,status,age,contact,address):
        if len(com_code.strip())==0 or len(name.strip())==0 or len(cnic.strip())==0 or len(age.strip())==0 or len(contact.strip())==0 or len(address.strip())==0:
            print("ERROR ::: Empty field")
            return False
        elif len(cnic.strip())!=13:
            print("ERROR ::: ID card number must consist of 13 digits")
            return False
        elif status != "employee" and status != "manager":
            print("ERROR ::: Wrong status")
            return False
        elif len(age.strip())>2 or int(age.strip())<0:
            print("ERROR ::: Age should be correct")
            return False 
        elif len(contact.strip())!=11:
            print("ERROR ::: Contact should consist of 11 numbers")
            return False
        else:
            return True
# search data verification =========================================================
    def search_data_v(self,com_code,status):
        if len(com_code.strip())==0 or len(status.strip())==0:
            print("ERROR ::: Empty field")
            return False
        elif status!="employee" and status!="manager":
            print("ERROR ::: Wrong status")
            return False
        else:
            return True
# show data for avoid repetition ===================================================
    def show_data_avoid(self,status):
        query = f"select * from employee_manager_data where status='{status}' order by company_code asc"
        self.cur.execute(query)
        move = 0
        a = 1
        print("(Sr #),(Company code),(Name),(CNIC),(Status),(Age),(Contact),(Address)")
        for row in self.cur:
            print(f"{a}.... {row[0]} , {row[1]} , {row[2]} , {row[3]} , {row[4]} , {row[5]} , {row[6]}")
            a += 1
            move = 1
        if move==0:
            print(f"No {status} exist.Make sure you put right information.Try again!")
# update data verification ==========================================================
    def update_data(self,com_code,status):
        if com_code.strip() == "" and status.strip() == "":
            print("ERROR ::: Empty field")
            return False
        elif status.strip()!= "employee" and status.strip()!="manager":
            print("ERROR ::: Wrong status")
            return False
        else:
            return True
# update particular record - avoid repetition ==========================================
    def update_particular(self,com_code,status,field,new_value):
        query = f"update employee_manager_data set {field}='{new_value}' where company_code='{com_code}' and status='{status}'"
        self.cur.execute(query)
        self.db.commit()
        print("Record successfully updated")
        print("Which must need to restart execution of program for accessing updated data")

owner_v = Owner_verification()








# owner class is here =======================================================================================
class Owner:
    def __init__(self):
        self.db = sql.connect(host="localhost",port="3306",user="root",password="admin1234#",database="company")
        self.cur = self.db.cursor()
# add data =========================================================================
    def add_data(self):
        com_code = input("Enter company code : ")
        name = input("Enter name : ")
        cnic = input("Enter Id number : ")
        status = input("Enter status (employee or manager) : ")
        age = input("Enter age : ")
        contact = input("Enter contact : ")
        address = input("Enter address : ")
        check = owner_v.add_data_v(com_code,name,cnic,status,age,contact,address)
        if check==True:
            query = f"insert into employee_manager_data values ('{com_code}','{name.upper()}','{cnic}','{status}','{age}','{contact}','{address}')"
            self.cur.execute(query)
            self.db.commit()
            print(f"{status} : {name} successfully added")

# search data =====================================================================
    def search_data(self):
        comp_code = input("Enter company code : ")
        Status = input("Enter status : ")
        check_data = owner_v.search_data_v(comp_code,Status)
        if check_data == True:
            query = f"select * from employee_manager_data where company_code='{comp_code}' and status='{Status}'"
            self.cur.execute(query)
            move = 0
            for row in self.cur:
                print(f"Details of {Status} :--")
                print(f"\t Name : {row[1]}")
                print(f"\t CNIC : {row[2]}")
                print(f"\t Age : {row[4]}")
                print(f"\t Contact : {row[5]}")
                print(f"\t Address : {row[6]}")
                move = 1
            if move==0:
                print(f"This {Status} actually not exist.Make sure you put right information.Try again!")

# show data =========================================================================
    def show_data(self):
        status = input("Enter status : ")
        if len(status.strip())==0:
            print("ERROR ::: Empty field")
        elif status!="employee" and status!="manager":
            print("ERROR ::: Wrong status")
        else:
            if status.strip() == "employee":
                owner_v.show_data_avoid("employee")
            else:
                owner_v.show_data_avoid("manager")

# update data whole=======================================================================
    def update_data_whole(self):
        com_code = input("Enter company code : ")
        status = input("Enter status : ")
        check = owner_v.update_data(com_code,status)
        if check == True:
            query = f"select * from employee_manager_data where company_code='{com_code}' and status='{status}'"
            move = False
            self.cur.execute(query)
            for row in self.cur:
                print(f"Details of {status} are:---")
                print(f"\tName : {row[1]}")
                print(f"\tCNIC : {row[2]}")
                print(f"\tStatus : {row[3]}")
                print(f"\tAge : {row[4]}")
                print(f"\tContact : {row[5]}")
                print(f"\tAddress : {row[6]}")
                move = True
            if move == False:
                print(f"Hello sir, there is no {status} with company code {com_code} exist.Make sure you put right information.Try again!")
            else:
                print("New detalis:---")
                name = input("Enter name : ")
                cnic = input("Enter cnic : ")
                age = input("Enter age : ")
                contact = input("Enter contact : ")
                address = input("Enter address : ")
                if name.strip()=="" and age.strip()=="" and contact.strip()=="" and address.strip()=="" and cnic.strip()=="":
                    print("ERROR ::: Empty field.Make sure all fields are filled")
                elif len(cnic.strip())!=13:
                    print("ERROR ::: CNIC number must consist of 13 numbers")
                elif len(age.strip())!=2:
                    print("ERROR ::: Wrong age it should be consist of 2 digits")
                elif len(contact.strip())!=11:
                    print("ERROR ::: Contact must consist of 11 numbers")
                else:
                    query = f"update employee_manager_data set name='{name.upper()}',cnic='{cnic}',age='{age}',contact='{contact}',address='{address}' where company_code='{com_code}' and status='{status}'"
                    self.cur.execute(query)
                    self.db.commit()
                    print(f"{status} : {name} successfully updated")

# update data particular ==========================================================
    def update_data_particular(self):
        com_code = input("Enter company code : ")
        status = input("Enter status : ")
        check = owner_v.update_data(com_code,status)
        if check == True:
            query = f"select * from employee_manager_data where company_code='{com_code}' and status='{status}'"
            move = False
            self.cur.execute(query)
            for row in self.cur:
                print(f"Details of {status} are:---")
                print(f"\tName : {row[1]}")
                print(f"\tCNIC : {row[2]}")
                print(f"\tStatus : {row[3]}")
                print(f"\tAge : {row[4]}")
                print(f"\tContact : {row[5]}")
                print(f"\tAddress : {row[6]}")
                move = True
            if move == False:
                print(f"Hello sir, there is no {status} with company code {com_code} exist.Make sure you put right information.Try again!")
            else:
                print("Which field you want to update?")
                print("1. Company code")
                print("2. Name")
                print("3. CNIC number")
                print("4. Status")
                print("5. Age")
                print("6. Contact")
                print("7. Address")
                ch = int(input("Enter decision : "))
                if ch==1:
                    new_comp_code = input("Enter new company code : ")
                    if com_code.strip()=="":
                        print("ERROR ::: Empty field")
                    else:
                        owner_v.update_particular(com_code,status,"company_code",new_comp_code)
                elif ch==2:
                    name = input("Enter new name : ")
                    new_name = name.upper()
                    if new_name.strip()=="":
                        print("ERROR ::: empty field")
                    else:
                        owner_v.update_particular(com_code,status,"name",new_name)
                elif ch==3:
                    new_cnic = input("Enter new CNIC number : ")
                    if new_cnic.strip()=="":
                        print("ERROR ::: Empty field")
                    elif len(new_cnic.strip())!=13:
                        print("ERROR ::: CNIC number must consist of 13 numbers don't include any space")
                    else:
                        owner_v.update_particular(com_code,status,"cnic",new_cnic)
                elif ch==4:
                    new_status = input("Enter new status : ")
                    if new_status.strip()=="":
                        print("ERROR ::: Empty field")
                    elif new_status.strip()!="employee" and new_status.strip()!="manager":
                        print("ERROR ::: wrong status")
                    else:
                        owner_v.update_particular(com_code,status,"status",new_status)
                elif ch==5:
                    new_age = input("Enter new age : ")
                    if new_age.strip()=="":
                        print("ERROR ::: Empty field")
                    elif len(new_age.strip())!=2:
                        print("ERROR ::: Wrong age")
                    else:
                        owner_v.update_particular(com_code,status,"age",new_age)
                elif ch==6:
                    new_contact = input("Enter new contact : ")
                    if new_contact.strip()=="":
                        print("ERROR ::: Empty field")
                    elif len(new_contact.strip())!=11:
                        print("ERROR ::: Phone number must consist of 11 digits")
                    else:
                        owner_v.update_particular(com_code,status,"contact",new_contact)
                elif ch==7:
                    new_address = input("Enter new address : ")
                    if new_address.strip()=="":
                        print("ERROR ::: Empty field")
                    else:
                        owner_v.update_particular(com_code,status,"address",new_address)
                else:
                    print("ERROR ::: Invalid choice.Try again!")                        
                        
# delete data =======================================================================
    def delete_data(self):
        com_code = input("Enter company code : ")
        status = input("Enter status : ")
        if com_code.strip()=="" and status.strip()=="":
            print("ERROR ::: Empty field")
        elif status.strip()!="employee" and status.strip!="manager":
            print("ERROR ::: Wrong status")
        else:
            query = f"select * from employee_manager_data where company_code='{com_code}' and status='{status}'"
            self.cur.execute(query)
            check = 0
            for row in self.cur:
                print(f"Detalis of {status} :-----")
                print(f"\tCompany code : {row[0]}")
                print(f"\tName : {row[1]}")
                print(f"\tCNIC : {row[2]}")
                print(f"\tStatus : {row[3]}")
                print(f"\tAge : {row[4]}")
                print(f"\tContact : {row[5]}")
                print(f"\tAddress : {row[6]}")
                check = 1
            if check==1:
                print(f"You want to delete the record of {status} : {com_code}.Are you sure(y or n)",end="")
                what = input()
                if what.strip()=="y":
                    query = f"delete from employee_manager_data where company_code='{com_code}' and status='{status}'"
                    self.cur.execute(query)
                    self.db.commit()
                    print(f"{status} with company code {com_code} successfully deleted")
                elif what.strip()=="n":
                    print(f"Ok sir, record of {status} : {com_code} not deleted")
                else:
                    print("ERROR ::: Make sure you enter (y or n) 'y' for 'yes' and 'n' for 'no'.Try again")
            else:
                print(f"{status} with company code {com_code} not found.Make sure you enter right information.Try again!")


# montly_manufacturing_employee ===========================================
    def montly_manufacturing_employee(self):
        month = int(input("Enter month : "))
        year = int(input("Enter year : "))
        comp_code = input("Enter company code : ")
        check1 = 0
        check2 = 0
        check3 = 0
        # varify month
        if month>=1 and month<=12:
            if len(str(year))==4:
                check1 = 1
            else:
                print("ERROR ::: Year value should be in the form of 4 digits like (2020).Try Again!")
        else:
            print("ERROR ::: You enter wrong month value. It should be between (01) to (12).Try again!")
        # if month is correct
        if check1==1:
            query = f"select * from employee_manager_data where company_code='{comp_code}'"
            self.cur.execute(query)
            for row in self.cur:
                print(f"Employee name is : ({row[1]})")
                print(f"Age : ({row[4]})")
                check2 = 1
            # verify employee in the company
            if check2==0:
                print(f"Employee with company_code ({comp_code}) not exist in the company.")
            else:
                query = f"select * from montly_manufacturing where month={month} and year={year} and company_code='{comp_code}'"
                self.cur.execute(query)
                for row in self.cur:
                    check3=1
                if check3==1:
                    print(f"ERROR ::: Employee with company code ({comp_code}) performance already found in record.")
                else:
                    salary = int(input("Salary per product : "))
                    query = f"select * from today_manufacturing where month={month} and company_code='{comp_code}' order by day asc"
                    self.cur.execute(query)
                    a = 1
                    sum = 0
                    money = 0
                    print(f"(Sr#) .... (Day) .... (Month) .... (Work)")
                    for row in self.cur:
                        print(f"{a} .... {row[0]} .... {row[1]} .... {row[3]}")
                        sum += int(row[3])
                        money = sum*salary
                    query = f"insert into montly_manufacturing values ({month},{year},'{comp_code}',{sum},{money})"
                    self.cur.execute(query)
                    self.db.commit()
                    print(f"Employee montly performence successfully added in the record")


# see_montly_manufacturing_employee =================================================
    def see_montly_manufacturing_employee(self):
        month = int(input("Enter month : "))
        year = int(input("Enter year : "))
        check_point = 0
        if month>=1 and month<=12:
            if len(str(year))==4:
                check_point = 1
            else:
                print("ERROR ::: Year value should be 4 digits.Try again!")
        else:
            print("ERROR ::: You put wrong month value.It should be from (01) to (12)")
        
        # verification
        if check_point==1:
            query = f"select * from montly_manufacturing where month={month} and year={year}"
            self.cur.execute(query)
            check = 0
            a = 1
            print(f"(sr#) .... (Month) .... (Year) .... (Company code) .... (Work) .... (Salary)")
            for row in self.cur:
                print(f"{a} .... {row[0]} .... {row[1]} .... {row[2]} .... {row[3]} .... {row[4]}")
                check = 1
            if check == 1:
                print("")
                print("Are you want to see graphical representation? (Y/N)",end="")
                sure = input("")
                if sure=="Y":
                    df = pd.read_sql_query(f"select * from montly_manufacturing where month={month} and year={year}",self.db)
                    # print(df)
                    a = sns.barplot(x="company_code",y="work",data=df,palette="rainbow_r")
                    for bar in a.containers:
                        a.bar_label(bar)
                    plt.title(f"Month({month}) : Year({year}) Employees Performance")
                    plt.show()
            else:
                print(f"No record exist according to month ({month}) and ({year}). Whether you don't put record about this month.Try again! and make it sure you put right information.")


# montly_manufacturing company ===================================================
    def montly_manufacturing_company(self):
        month = int(input("Enter month : "))
        year = int(input("Enter year : "))
        check_point = 0
        check_point2 = 0
        if month>=1 and month<=12:
            if len(str(year))==4:
                check_point = 1
            else:
                print("ERROR ::: Year value should be 4 digits.Try again!")
        else:
            print("ERROR ::: You put wrong month value.It should be from (01) to (12)")

        if check_point==1:
            query = f"select * from montly_manufacturing_company where month={month} and year={year}"
            self.cur.execute(query)
            for row in self.cur:
                check_point2=1
            if check_point2==1:
                print(f"You already put record of month({month}) : year({year}) in database")
            else:
                query = f"select * from montly_manufacturing where month={month} and year={year}"
                self.cur.execute(query)
                check = 0
                a = 0
                work = 0
                total_salary = 0
                print(f"(sr#) ..... (Month) ..... (Year) .... (Company Code) .... (Work) .... (Salary)")
                for row in self.cur:
                    print(f"{a} .... {row[0]} .... {row[1]} .... {row[2]} .... {row[3]} .... {row[4]}")
                    work += int(row[3])
                    total_salary += int(row[4])
                    check = 1
                if check == 0:
                    print(f"No performance of employees in month({month}) and year({year}) stored in the database")
                else:
                    query = f"insert into montly_manufacturing_company values ({month},{year},{work},{total_salary})"
                    self.cur.execute(query)
                    self.db.commit()
                    print("Record of company performance successfully added")


# see_montly_manufacturing_company  =============================================
    def see_montly_manufacturing_company(self):
        month = int(input("Enter month : "))
        year = int(input("Enter year : "))
        check_point = 0
        if month>=1 and month<=12:
            if len(str(year))==4:
                check_point = 1
            else:
                print("ERROR ::: Year value should be 4 digits.Try again!")
        else:
            print("ERROR ::: You put wrong month value.It should be from (01) to (12)")
        
        # verification
        if check_point==1:
            query = f"select * from montly_manufacturing_company where month={month} and year={year}"
            self.cur.execute(query)
            check = 0
            a = 1
            print(f"(sr#) .... (Month) .... (Year) .... (Work) .... (Total_employees_salary)")
            for row in self.cur:
                print(f"{a} .... {row[0]} .... {row[1]} .... {row[2]} .... {row[3]}")
                check = 1
            if check == 1:
                print("")
                print("Are you want to see graphical representation? (Y/N)",end="")
                sure = input("")
                if sure=="Y":
                    df = pd.read_sql_query(f"select * from montly_manufacturing_company where year={year} order by month asc",self.db)
                    a = sns.barplot(x="month",y="work",data=df,palette="rainbow_r")
                    for bar in a.containers:
                        a.bar_label(bar)
                    plt.title(f"Year({year}) Company Performance")
                    plt.show()

            else:
                print(f"No record exist according to month ({month}) and ({year}). Whether you don't put record about this month.Try again! and make it sure you put right information.")


# create_password ================================================
    def create_password(self):
        comp_code = input("Enter company code : ")
        password = input("Enter password : ")        
        query = f"select * from employee_manager_data where company_code='{comp_code}'"
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            print(f"Employee name : {row[1]}")
            check = 1
        
        if check==0:
            print("ERROR ::: Employee not exist in the company.Try again!")
        else:
            if len(password)==5:
                query = f"insert into passwords values ('{comp_code}','{password}')"
                self.cur.execute(query)
                self.db.commit()
                print(f"Password successfully set for employee having company code ({comp_code})")
            else:
                print("Password length must be 5 digits long.Try again!")
    
# update_password =============================================
    def update_password(self):
        comp_code = input("Enter company code : ")
        query = f"select * from passwords where company_code='{comp_code}'"
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            print(f"Password : {row[1]}")
            check=1
        if check==0:
            print(f"ERROR ::: Employee having company code ({comp_code}) not exist in passwords section. So, first you need to create password then you can update it.")
        else:
            password = input("Enter new password : ")
            if len(password)==5:
                query = f"update passwords set password='{password}' where company_code='{comp_code}'"
                self.cur.execute(query)
                self.db.commit()
                print(f"Password of employee having company code ({comp_code}) successfully updated")
            else:
                print("ERROR ::: Password length must be consist of (5) digits.Try again!")

# search_password =====================================================
    def search_password(self):
        comp_code = input("Enter company code : ")
        query = f"select * from passwords where company_code='{comp_code}'"
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            print(f"Password : {row[1]}")
            check=1
        if check==0:
            print(f"ERROR ::: Employee having company code ({comp_code}) not exist in passwords section.")

# delete_password========================================================
    def delete_password(self):
        comp_code = input("Enter company code : ")
        query = f"select * from passwords where company_code='{comp_code}'"
        self.cur.execute(query)
        check = 0
        for row in self.cur:
            print(f"Password : {row[1]}")
            check=1
        if check==0:
            print(f"ERROR ::: Employee having company code ({comp_code}) not exist in passwords section.")
        else:
            query = f"delete from passwords where company_code='{comp_code}'"
            self.cur.execute(query)
            self.db.commit()
            print("Employee password successfully deleted from database.")





