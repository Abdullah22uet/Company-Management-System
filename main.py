import mysql.connector as sql
db = sql.connect(host = "localhost",port = "3306",user = "root",password = "admin1234#",database = "company")

# employee file
from employee import Employee
employee = Employee()

# owner file
from owner import Owner,Owner_verification
owner = Owner()
owner_v = Owner_verification()

# manager file
from manager import Manager
manager = Manager()


# main file 
if __name__ == "__main__":
    while 1:
        print("***************** Company Management System *****************")
        print("1. Interface")
        print("2. exit")
        try:
            d = int(input())
            if d == 1:
                code = input("Type code : ")
                # manager login ===========================================================================
                if code == "m":
                    print("********** Manager login **********")
                    while 1: 
                        print("1. Enter today manufacturing")
                        print("2. See today manufacturing")
                        print("3. Edit work")
                        print("4. Exit")
                        dec = int(input("Enter decision : "))
                        if dec == 1:
                            manager.enter_data()
                        elif dec == 2:
                            manager.see_data()
                        elif dec == 3: 
                            manager.edit_data()
                        elif dec == 4:
                            print("Successfully exit from manager section")
                            break
                        else:
                            print("ERROR ::: Wrong choice")
                        
                # employee login ==========================================================================
                elif code == "e":
                    print("********** Employee login **********")
                    comp_code = input("Enter company code : ")
                    password = input("Enter password : ")
                    employee.password(comp_code , password)

                # owner login =============================================================================
                elif code == "o":
                    print("********** Owner login **********")
                    while 1:
                        print("1. Add,search,update,delete data")
                        print("2. Montly Employee Manufacturing")
                        print("3. Montly Company Manufacturing")
                        print("4. Manage Passwords")
                        print("5. Exit")
                        choice = int(input("Enter your decision: "))
                        if choice==1:
                            print("1. Add data")
                            print("2. Search data")
                            print("3. Show data")
                            print("4. Update data")
                            print("5. Delete record")
                            print("6. exit")
                            dec = int(input())
                            if dec == 1:
                                owner.add_data()
                            elif dec == 2:
                                owner.search_data()
                            elif dec == 3:
                                owner.show_data()
                            elif dec == 4:
                                while 1:
                                    print("1. Update whole record")
                                    print("2. Update particular field of record")
                                    print("3. exit")
                                    choice = int(input("Enter decision : "))
                                    if choice == 1:
                                        owner.update_data_whole()
                                    elif choice == 2:
                                        owner.update_data_particular()
                                    elif choice == 3:
                                        print("Successfully exit from update section")
                                        break
                                    else:
                                        print("ERROR ::: Wrong choice sir")
                            elif dec == 5:
                                owner.delete_data()
                            elif dec == 6:
                                print("successfully exit from owner section")
                                break
                            else:
                                print("ERROR ::: Wrong choice")
                        elif choice==2:
                            while 1:
                                print("1. Enter record for this month")
                                print("2. See monthly manufacturing and also graphical representation")
                                print("3. Exit")
                                dec = int(input("Enter decision : "))
                                if dec==1:
                                    owner.montly_manufacturing_employee()
                                elif dec==2:
                                    owner.see_montly_manufacturing_employee()
                                elif dec==3:
                                    print("Successfully exit")
                                    break
                                else:
                                    print("ERROR ::: You enter wrong decision.Try again!")
                        elif choice==3:
                            while 1:
                                print("1. Enter record for this month")
                                print("2. See monthly manufacturing and also graphical representation")
                                print("3. Exit")
                                dec = int(input("Enter decision : "))
                                if dec==1:
                                    owner.montly_manufacturing_company()
                                elif dec==2:
                                    owner.see_montly_manufacturing_company()
                                elif dec==3:
                                    print("Successfully exit")
                                    break
                                else:
                                    print("ERROR ::: You enter wrong decision.Try again!")
                        elif choice==4:
                            while 1:
                                print("1. Create password")
                                print("2. Update password")
                                print("3. Search password")
                                print("4. Delete password")
                                print("5. Exit")
                                dec = int(input("Enter decision : "))
                                if dec==1:
                                    owner.create_password()
                                elif dec==2:
                                    owner.update_password()
                                elif dec==3:
                                    owner.search_password()
                                elif dec==4:
                                    owner.delete_password()
                                elif dec==5:
                                    print("successfully exit")
                                    break
                                else:
                                    print("ERROR :::: Wrong decision")
                        elif choice==5:
                            print("Successfully exit from owner section")
                            break
                        else:
                            print("ERROR ::: Wrong choice")

                # false case ==============================================================================
                else:
                    print("You can't proceed further")
            elif d == 2:
                print("Exit from system")
                break
            else:
                print("ERROR ::: Wrong choice")
        except ValueError:
            print("Warning ::: It seems whether you don't enter any decision or you enter wrong choice")
# end of code