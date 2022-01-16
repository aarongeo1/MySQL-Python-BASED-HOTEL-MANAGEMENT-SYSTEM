
import mysql.connector
from tabulate import tabulate
import getpass
def MAINMENU():
    
    print("\t1.login")
    print("\t2.sign up")
    success=0
    while success==0:
        s=eval(input("Enter (1/2)"))

        if s==2:
            
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
            if mydb.is_connected()==False:
                print("error connecting to MySQL database")
            mycursor=mydb.cursor()
            usr=input("enter your new username: ")
            pswd=eval(("enter your new password: "))
            q1="insert into user values('{}','{}')".format(usr,pswd)
            mycursor.execute(q1)
            print("succesfully logged in")
            success=1
            mydb.commit()
            mydb.close()
            break
        elif s==1:
            
            mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
            if mydb.is_connected()==False:
                print("error connecting to MySQL database")
            mycursor=mydb.cursor()
            usr=input("enter your username: ")
            pswd=eval(input("enter your password: "))
            q2="select count(*) from user where username ='{}' and passwd='{}'".format(usr,pswd)
            mycursor.execute(q2)
            result=mycursor.fetchone()
            if result[0]==1:
                print("logged in")
                success=1
                mydb.commit()
                mydb.close()
                break
            else:
                print("error not found")
        else:
            print("not a valid option")
            
            A=1
        
   
    
mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")

def MAINMENUadmin():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
    if mydb.is_connected()==False:
        print("error connecting to MySQL database")
    while True:
        mycursor=mydb.cursor()
        pswd=input("ENTER THE PASSWORD  : ")
        q2="select count(*) from admin where password='{}'".format(pswd)
        mycursor.execute(q2)
        result=mycursor.fetchone()
        if result[0]==1:
            print("logged in")
            mydb.commit()
            
            break
        else:
            print("error not found")
    



xyz=1
while xyz==1:
    print("-----------------------------------------------------------")
    print("\tMAINMENU\t")
    print("-----------------------------------------------------------")
    print("\t1.ADMIN\n\t2.USER\n\t3.EXIT")
    qwt=eval(input("ENTER YOUR OPTION  :  "))
    if qwt==2:
        MAINMENU()
        xyp=1
        while xyp==1:
            print("\nWelcome to A&A hotels\n")
            print("-----------------------------------------------------------")
            print("\tUSERMENU\t")
            print("-----------------------------------------------------------")
            
            
            print("WOULD YOU LIKE TO  :\n\t1.BOOK A ROOM\n\t2.MANAGE YOUR RESERVATION\n\t3.BACK")
            l=eval(input("enter your option"))
            if l==1:
                
                            
                mydb=mysql.connector.connect(host="localhost",user="root", passwd="aaron", database="hotelmanagement" , charset="utf8")
                if mydb.is_connected()==False:
                    print("error connecting to mysql database")
                mycursor=mydb.cursor()
                mycursor.execute("select id,type , price from rooms where bkno=1 ")
                rec=mycursor.fetchall()
                if rec!=[]:
                    print (rec)
                    for i in rec:
                        print(" {:<4}  {:>8}  {:>15} ".format(i[0],i[1],i[2]))
                    
                        
                    t=tabulate(rec, headers=["ROOM NO","ROOM TYPE","PRICE"],tablefmt="psql")
                    print(t)
                else:
                    print("NO RECORD FOUND")
                

                k=input("\nWould you like to book one of these rooms?(y/n)  :  ")
                if k=="y" or k=="Y":
                    
                    import mysql.connector
                            
                            
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                    if mydb.is_connected()==False:
                        print("error connecting to MySQL database")
                    mycursor=mydb.cursor()
                    i=eval(input("\nEnter the room no which you want to book  : "))
                    
                    mycursor.execute("update rooms set bkno=0 where id='{}'".format(i))

                    print("SUCCESSFUL")
                                
                    mydb.commit()
                    
            if l==2:
                k=input("\nWould you like to cancel your reservation?(y/n) : ")
                if k=="y" or k=="Y":
                    
                            
                            
                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                    if mydb.is_connected()==False:
                        print("error connecting to MySQL database")
                    mycursor=mydb.cursor()
                    i=eval(input("\nEnter the room no which you booked  : "))
                    
                    mycursor.execute("update rooms set bkno=1 where id='{}'".format(i))

                    print("SUCCESSFUL")
                                
                    mydb.commit()
                    
            if l==3:
                break
                
    elif qwt==1:
        MAINMENUadmin()
        print("\n")
        xyu=1
        while xyu==1:
            
            print("-----------------------------------------------------------")
            print("\tADMIN MENU\t","\n")
            print("-----------------------------------------------------------")

            print("\t1.ROOM\n\t2.EMPLOYEES\n\t3.BACK")
            n=eval(input("\nENTER YOUR OPTION (1/2/3)  :  "))
            if n==1 :
                
                    xye=1
                    while xye==1:
                        print("-----------------------------------------------------------")
                        print("\tROOM MENU\t","\n")
                        print("\t1.ADD ROOM DETAILS\n\t2.DISPLAY ROOM DETAILS\n\t3.SEARCH FOR A ROOM\n\t4.DELETE A ROOM\n\t5.MODIFY ROOM DETAIL\n\t6.BACK")
                        m=eval(input("ENTER YOUR OPTION (1/2/3/4/5/6)  : "))
                        if m==1:
                            ans="y"
                            while ans=="y" or ans=="Y":

                                
                            
                            
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                i=eval(input("ENTER THE ROOM NO  : "))
                                typ=input("ENTER THE TYPE (single/double)  : ")
                                pric=eval(input("ENTER THE PRICE  : "))
                                if typ=="single" or typ=="double":
                                
                                    q1="insert into rooms values('{}','{}','{}',1)".format(i,typ,pric)
                                    mycursor.execute(q1)
                                    print("succesful")
                                    print("\n Do you want to add more? (y/n)  : ")
                                    ans=input()
                                else:
                                    print("PLEASE ENTER A VALID TYPE")
                                mydb.commit()
                                
                                
                                
                        elif m==2:
                            
                            
                            mydb=mysql.connector.connect(host="localhost",user="root", passwd="aaron", database="hotelmanagement" , charset="utf8")
                            if mydb.is_connected()==False:
                                print("error connecting to mysql database")
                            mycursor=mydb.cursor()

                            mycursor.execute("select* from rooms ")
                            rec=mycursor.fetchall()
                            if rec!=[]:
                                t=tabulate(rec,headers=["room no","type","price","availability"],tablefmt="psql")
                                print(t)            
                            else:
                                print("NO RECORD FOUND")
                            
                            
                        elif m==3:
                            
                            mydb=mysql.connector.connect(host="localhost",user="root", passwd="aaron", database="hotelmanagement" , charset="utf8")
                            if mydb.is_connected()==False:
                                print("error connecting to mysql database")
                            mycursor=mydb.cursor()
                            no=eval(input("ENTER THE ROOM N.O.  : "))
                            typ=input("ENTER THE TYPE OF ROOM(single/double)  : ")
                            if typ=="single" or typ=="double":
                                mycursor.execute("select* from rooms where id='{}' and type='{}'".format(no,typ))
                                rec=mycursor.fetchall()
                                if rec!=[]:
                                    t=tabulate(rec,headers=["room no","type","price","availability"],tablefmt="psql")
                                    print(t)
                                else:
                                    print("NO RECORD FOUND")
                            else:
                                print("PLEASE ENTER A VALID OPTION FOR TYPE")
                            
                            
                        elif m==4:
                            ans="y"
                            while ans=="y" or ans=="Y":

                                
                            
                            
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER THE ROOMNO  : "))
                                
                                mycursor.execute("delete from rooms where id='{}'".format(no))
                                
                                print("succesful")
                                print("\n Do you want to delete more? (y/n)  : ")
                                mydb.commit()
                                
                                ans=input()
                            
                        elif m==5:
                            cvy=1
                            while cvy==1:
                                print("-----------------------------------------------------------")
                                print("\tMODIFY MENU\t")
                                print("-----------------------------------------------------------")
                                print("What would you wish to change  :\n1.ROOM N.O.\n2.TYPE\n3.PRICE\n4.AVAILABILITY\n5.BACK")
                                k=eval(input("\nENTER YOUR OPTION (1/2/3/4/5)  : "))
                                if k==1:
                                    

                                    
                                    
                                    
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                    if mydb.is_connected()==False:
                                        print("error connecting to MySQL database")
                                    mycursor=mydb.cursor()
                                    i=eval(input("ENTER THE ROOM N.O. IN WHICH YOU WISH TO CHANGE  : "))
                                    prc=input("ENTER THE NEW ROOM N.O.  : ")
                                    mycursor.execute("update rooms set id='{}' where id='{}'".format(prc,i))
                                    mydb.commit()
                                    
                                elif k==2:
                                    
                                    
                                    
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                    if mydb.is_connected()==False:
                                        print("error connecting to MySQL database")
                                    mycursor=mydb.cursor()
                                    i=eval(input("ENTER THE ROOM N.O. IN WHICH YOU WISH TO CHANGE  : "))
                                    prc=input("ENTER THE NEW TYPE (single/double)  : ")
                                    if prc=="single" or prc=="double":
                                        mycursor.execute("update rooms set type='{}' where id='{}'".format(prc,i))
                                    else:
                                        print("PLEASE ENTER A VALID OPTION")

                                    print("\nSUCCESSFUL\n")
                                        
                                    mydb.commit()
                                elif k==3:
                                    
                                    
                                    
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                    if mydb.is_connected()==False:
                                        print("error connecting to MySQL database")
                                    mycursor=mydb.cursor()
                                    i=eval(input("ENTER THE ROOM N.O. IN WHICH YOU WISH TO CHANGE  : "))
                                    prc=eval(input("ENTER THE NEW PRICE  : "))
                                    
                                    mycursor.execute("update rooms set price='{}' where id='{}'".format(prc,i))
                                    

                                    print("\nSUCCESSFUL\n")
                                        
                                    mydb.commit()
                                elif k==4:
                                    
                                    
                                    
                                    mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                    if mydb.is_connected()==False:
                                        print("error connecting to MySQL database")
                                    mycursor=mydb.cursor()
                                    i=eval(input("ENTER THE ROOM N.O. IN WHICH YOU WISH TO CHANGE  : "))
                                    prc=input("IS IT BOOKED? (y/n)  : ")
                                    if prc=="y" or prc=="Y":
                                        mycursor.execute("update rooms set bkno='0' where id='{}'".format(i))
                                        mydb.commit()
                                    if prc=="n" or prc=="N":
                                        mycursor.execute("update rooms set bkno='1' where id='{}'".format(i))
                                        mydb.commit()
                                        
                                    
                                    
                                    

                                    print("\nSUCCESSFUL\n")
                                        
                                    
                                elif k==5:
                                    break
                                else:
                                    print("\nENTER A VALID OPTION\n")
                            

                                
                                
                        elif m==6:
                            break
                        else:
                            print("\nENTER A VALID OPTION\n")
            elif n==2:
                bvb=1
                while bvb==1:
                    
             
                    print("-----------------------------------------------------------")
                    print("EMPLOYEE MENU","\n")
                    print("\t1.ADD EMPLOYEE DETAILS\n\t2.DISPLAY EMPLOYEE DETAILS\n\t3.SEARCH FOR AN EMPLOYEE\n\t4.DELETE EMPLOYEE DETAILS\n\t5.MODIFY EMPLOYEE DETAIL\n\t6.BACK")
                    m=eval(input("ENTER YOUR OPTION  : "))
                    if m==1:
                        ans="y"
                        while ans=="y" or ans=="Y":

                            
                        
                        
                            mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                            if mydb.is_connected()==False:
                                print("error connecting to MySQL database")
                            mycursor=mydb.cursor()
                            i=eval(input("Enter employee id  : "))
                            na=input("Enter employee name  : ")
                            sal=eval(input("Enter employee salary  : "))
                            jo=input("Enter employee's job name  : ")
                            dept=input("Enter employee department  :")
                            gen=input("Enter employee gender (M/F)  :")
                            dog=input("Enter date of joining for employee  : ")
                            ag=input("Enter age of employee  : ")
                            q1="insert into empl values('{}','{}','{}','{}','{}','{}','{}','{}')".format(i,na,sal,jo,dept,gen,dog,ag)
                            mycursor.execute(q1)
                            print("succesful")
                            print("\n do you want to add more? (y/n)")
                            mydb.commit()
                            
                            ans=input()
                            
                    elif m==2:
                        
                        
                        
                        mydb=mysql.connector.connect(host="localhost",user="root", passwd="aaron", database="hotelmanagement" , charset="utf8")
                        if mydb.is_connected()==False:
                            print("error connecting to mysql database")
                        mycursor=mydb.cursor()

                        mycursor.execute("select* from empl ")
                        rec=mycursor.fetchall()
                        if rec!=[]:
                            t=tabulate(rec,headers=["id","name","salary","job","dept","gender","doj","age"],tablefmt='psql')
                            print(t)            
                        else:
                            print("no record found")
                        
                        
                    elif m==3:
                        
                        mydb=mysql.connector.connect(host="localhost",user="root", passwd="aaron", database="hotelmanagement" , charset="utf8")
                        if mydb.is_connected()==False:
                            print("error connecting to mysql database")
                        mycursor=mydb.cursor()
                        no=eval(input("enter the EMPLOYEE id"))
                        na=input("enter the name of EMPLOYEE")
                        mycursor.execute("select* from empl where id='{}' and name='{}'".format(no,na))
                        rec=mycursor.fetchall()
                        if rec!=[]:
                            t=tabulate(rec,headers=["id","name","salary","job","dept","gender","doj","age"],tablefmt='psql')
                            print(t)
                        else:
                            print("NO RECORD FOUND")
                        
                        
                    elif m==4:
                        ans="y"
                        while ans=="y" or ans=="Y":

                            
                        
                        
                            mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                            if mydb.is_connected()==False:
                                print("error connecting to MySQL database")
                            mycursor=mydb.cursor()
                            no=eval(input("ENTER EMPLOYEE ID  : "))
                            
                            mycursor.execute("delete from empl where id='{}'".format(no))
                            
                            print("SUCCESSFUL")
                            print("\n Do you want to delete more? (y/n)  : ")
                            mydb.commit()
                            
                            ans=input()
                        
                    elif m==5:
                    
                        cvb=1
                        while cvb==1:
                            x=eval(input("\nWHAT DO YOU WISH TO CHANGE?\n1.ID\n2.NAME\n3.SALARY\n4.JOB\n5.DEPT\n6.GENDER\n7.DATE OF JOINING\n8.AGE\n9.back\n"))
                            if x==1:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=eval(input("ENTER NEW EMPLOYEE ID  : "))
                                
                                mycursor.execute("update empl set id='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==2:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE NAME  : ")
                                
                                mycursor.execute("update empl set name='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==3:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=eval(input("ENTER NEW EMPLOYEE SALARY  : "))
                                
                                mycursor.execute("update empl set salary='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==4:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE JOB  : ")
                                
                                mycursor.execute("update empl set job='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==5:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE DEPT  : ")
                                
                                mycursor.execute("update empl set dept='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==6:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE GENDER (M/F) : ")
                                if on=="M" or on=="F":
                                
                                    mycursor.execute("update empl set gender='{}' where id='{}'".format(on,no))
                                else:
                                    print("There is a mistake in gender ,write in capital letters, please write M or F and try again.")
                                
                                
                                
                                mydb.commit()
                            elif x==7:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE DATE OF JOINING (yyyy-mm-dd)  : ")
                                
                                mycursor.execute("update empl set doj='{}' where id='{}'".format(on,no))
                                
                                
                                mydb.commit()
                            elif x==8:
                                mydb=mysql.connector.connect(host="localhost",user="root",passwd="aaron",database="hotelmanagement")
                                if mydb.is_connected()==False:
                                    print("error connecting to MySQL database")
                                mycursor=mydb.cursor()
                                no=eval(input("ENTER EMPLOYEE ID  : "))
                                on=input("ENTER NEW EMPLOYEE AGE  : ")
                                
                                mycursor.execute("update empl set age='{}' where id='{}'".format(on,no))
                                
                                
                                
                                mydb.commit()
                            elif x==9:
                                break
                            else:
                                print("\nENTER A VALID OPTION AND TRY AGAIN\n")
                            
                          
                                
                                
                        
                        
                        
                    elif m==6:
                        break
                    else:
                        print("\nENTER A VALID OPTION AND TRY AGAIN\n") 
                        
                        

                            
                            
                  
            elif n==3:
                    break

            else:
                print("\nPLEASE ENTER A VALID OPTION\n")
        
            
                
                    
                    
            
        
    elif qwt==3:
        print("-----------------------------------------------------------")
        print("\tLEAVING PAGE\t")
        print("\tGOODBYE AND COME AGAIN SOON\t")
        print("-----------------------------------------------------------")
        break
    else:
        
        print("\nPLEASE ENTER A VALID OPTION\n")
mydb.close()












    

    
              
        
    

    
    
