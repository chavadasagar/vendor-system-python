import mysql.connector
import re

class vendor: # oop concept

    mydb = mysql.connector.connect(
            host = "localhost",
            user = 'root',
            password = "",
            database='vendor',
            port="3308"
        )
    cur = mydb.cursor() # loc
    def is_email_true(this,email):
        #use regular expresion
        match = re.match("[a-zA-Z0-9]+@[a-zA-Z]+[.]+[a-zA-Z]",email)

        if match:
            return True
        else:
            return False
    def add_new_vendor(this):

        
        name = input("Enter Name :")
        ct = input("Enter city :")
        email = input("Enter email :")
        phno = input("enter phone no :")

        if(this.is_email_true(email)):
            data = (name,ct,email,phno)
            this.cur.execute("insert into info(name,ct,email,phno) values(%s,%s,%s,%s)",data)
            this.mydb.commit()
            print("register successfuly  "+name)    
        else:
            print("email is wrong tray again")
            this.add_new_vendor() # recursion
        

        
        
    def update_vendor(this):
        no = input("Enter id :")
        confirm = input("do you want to update name :?y/n")        
        if(confirm == "y"):
            name = input("Enter Name :")
            this.cur.execute("update info set name='"+name+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("do you want to update ct :?y/n")
        if(confirm == "y"):
            ct = input("Enter city :")
            this.cur.execute("update info set ct='"+ct+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("do you want to update email :?y/n")
        if(confirm == "y"):
            email = input("Enter email :")
            this.cur.execute("update info set email='"+email+"' where id='"+no+"'")
            this.mydb.commit()
        confirm = input("do you want to update phone no :?y/n")
        if(confirm == "y"):
            phno = input("enter phone no :")
            this.cur.execute("update info set phno='"+phno+"' where id='"+no+"'")
            this.mydb.commit()


        print("update record ",no)
    def delete_vendor(this):
        no = int(input("Enter Id :"))
        
        this.cur.execute(f"delete from info where id={no}") # use f string
        this.mydb.commit();

        print("delete successsfuly id is ",no)
    def show_vendor(this):
        cur = this.mydb.cursor()
        cur.execute("select * from info")
        
        print("id\tname\tcity\temail\t\tphoneno")
        for rec in cur:
            print(rec[0],"\t",rec[1],"\t",rec[2],"\t",rec[3],"\t",rec[4])
    
    def show_specific_rec(this):
        no = input("Enter id :")
        cur = this.mydb.cursor()
        cur.execute("select * from info where id = '"+no+"'")
        print("id\tname\tcity\temail\temail\tphoneno")
        for rec in cur:
            print(rec[0],"\t",rec[1],"\t",rec[2],"\t",rec[3],"\t",rec[4])
        
        
    def show_option(this):
        print("1.add new vendor")
        print("2.delete vendor")
        print("3.show vendor")
        print("4.update vendor")
        print("5.display specific vendor")
        print("6.exit")


'''
class admin(vendor):
    def login(this):
        username = input("Username :")
        password = input("Password :")
        cur = super().mydb.cursor()

        usr = cur.execute("select * from admin")

        
        for x in cur:
            if(x[0]==username and x[1]==password):
                return True
            else:
                return False                       

        super().mydb.commit()
    


obj = admin()
'''
ven = vendor() # create obj

#if obj.login():
while True:
    ven.show_option()
    op = int(input("select :"))
    if(op == 1):
        ven.add_new_vendor()
        input()
    if(op == 2):
        ven.delete_vendor()
        input()
    if(op == 3):
        ven.show_vendor()
        input()
    if(op == 4):
        ven.update_vendor()
        input()
    if(op == 5):
        ven.show_specific_rec();
    if(op == 6):
        break
