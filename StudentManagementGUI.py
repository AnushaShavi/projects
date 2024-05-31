
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector 
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Dummy authentication - Replace with actual authentication logic
    if username == "Anu" and password == "Anu@123":
         messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid username or password")

def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Login System")
root.geometry("500x500")

# Create labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create buttons for login and clear
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()



class Ruas:
    def __init__(self,root):
        self.root=root
        self.root.title("RUAS Student management system")
        self.root.geometry("1540x800+0+0")

        self.FullName=StringVar()
        self.StudentID=StringVar()
        self.MothersName=StringVar()
        self.FathersName=StringVar()
        self.MobileNo=StringVar()
        self.Email=StringVar()
        self.gender=StringVar()

        self.BranchID=StringVar()
        self.BranchName=StringVar()
        self.Department=StringVar()
        self.HOD=StringVar()
        self.Phone=StringVar()
        self.Dept_Email=StringVar()
        self.location=StringVar()

        self.PaymentID=StringVar()
        self.PaymentMethod=StringVar()
        self.Amountpaid=StringVar()
        self.Paymentdate=StringVar()
        self.Fineifany=StringVar()
        self.FeeType=StringVar()
        self.RecieptNumber=StringVar()

        self.Sem=StringVar()
        self.SGPA=StringVar()
        self.PassORFail=StringVar()
        self.EvenORodd=StringVar()
        self.Percentage=StringVar()
        self.CGPA=StringVar()
        self.Batch=StringVar()


        #label title
        lbtitle=Label(self.root,bd=20,relief=RIDGE,text="RUAS Student Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)

        #______________________________Data frame_____________________
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=100,width=1400,height=400)

        #Student details dataframe
        df1=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("arial",20,"bold"),text="Student Details")
        df1.place(x=0,y=5,width=320,height=300)


        #Branch details dataframe
        df2=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("arial",20,"bold"),text="Branch Details")
        df2.place(x=330,y=5,width=300,height=300)


        #Fee payment dataframe
        df3=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("arial",20,"bold"),text="Fee Payment Details")
        df3.place(x=630,y=5,width=350,height=300)

        #Exam results
        df4=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,
                                       font=("arial",20,"bold"),text="Exam Results")
        df4.place(x=960,y=5,width=360,height=300)

        #______________________________________________________________Button frames__________________________________________________
        buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        buttonframe.place(x=0,y=450,width=1400,height=70)

        #_______________________________________________________________CRUD frame___________________________________________________
        dbframe=Frame(self.root,bd=20,relief=RIDGE)
        dbframe.place(x=0,y=500,width=1350,height=190)

        #_________________________________________________Inserting attributes in first dataframe________________________________________________
        
        #Attribute1:::Full Name 
        labelFullName=Label(df1,font=("arial",12,"bold"),text="Full Name",padx=2,pady=6)
        labelFullName.grid(row=0,column=0,sticky=W)
        txtFullName=Entry(df1,font=("arial",12,"bold"),textvariable=self.FullName,width=35)
        txtFullName.grid(row=0,column=1)

        #Attribute2:::Mother name
        labelmother=Label(df1,font=("arial",12,"bold"),text="Mother Name",padx=2,pady=6)
        labelmother.grid(row=3,column=0,sticky=W)
        txtmother=Entry(df1,font=("arial",12,"bold"),textvariable=self.MothersName,width=35)
        txtmother.grid(row=3,column=1)

        #Attribute3:::Father Name
        labelFather=Label(df1,font=("arial",12,"bold"),text="Father Name",padx=2,pady=6)
        labelFather.grid(row=2,column=0,sticky=W)
        txtFather=Entry(df1,font=("arial",12,"bold"),textvariable=self.FathersName,width=35)
        txtFather.grid(row=2,column=1)

    
        #Attribute4:::Email
        labelemail=Label(df1,font=("arial",12,"bold"),text="Email",padx=2,pady=6)
        labelemail.grid(row=6,column=0,sticky=W)
        txtemail=Entry(df1,font=("arial",12,"bold"),textvariable=self.Email,width=35)
        txtemail.grid(row=6,column=1)

        #Attribute5:::Mobile No
        labelmn=Label(df1,font=("arial",12,"bold"),text="Mobile No",padx=2,pady=6)
        labelmn.grid(row=4,column=0,sticky=W)
        txtmn=Entry(df1,font=("arial",12,"bold"),textvariable=self.MobileNo,width=35)
        txtmn.grid(row=4,column=1)

  
        #Attribute6:::Gender
        labelg=Label(df1,font=("arial",12,"bold"),text="Gender",padx=2,pady=6)
        labelg.grid(row=5,column=0,sticky=W)
        txtg=Entry(df1,font=("arial",12,"bold"),textvariable=self.gender,width=35)
        txtg.grid(row=5,column=1)

        

        #Attribute7:::Student ID
        labelsid=Label(df1,font=("arial",12,"bold"),text="Student ID",padx=2,pady=6)
        labelsid.grid(row=1,column=0,sticky=W)
        txtsid=Entry(df1,font=("arial",12,"bold"),textvariable=self.StudentID,width=35)
        txtsid.grid(row=1,column=1)

        


         #_________________________________________________Inserting attributes in second dataframe(Branch details)_____________________________________________
        #Attribute1:::Branch ID
        labelbid=Label(df2,font=("arial",12,"bold"),text="Branch ID",padx=2,pady=6)
        labelbid.grid(row=0,column=2,sticky=W)
        txtbid=Entry(df2,font=("arial",12,"bold"),textvariable=self.BranchID,width=35)
        txtbid.grid(row=0,column=3)

        

        #Attribute2:::Branch name
        labelbname=Label(df2,font=("arial",12,"bold"),text="Branch Name",padx=2,pady=6)
        labelbname.grid(row=1,column=2,sticky=W)
        txtbname=Entry(df2,font=("arial",12,"bold"),textvariable=self.BranchName,width=35)
        txtbname.grid(row=1,column=3)

        
        #Attribute3:::dept
        labeldept=Label(df2,font=("arial",12,"bold"),text="Department",padx=2,pady=6)
        labeldept.grid(row=2,column=2,sticky=W)
        txtdept=Entry(df2,font=("arial",12,"bold"),textvariable=self.Department,width=35)
        txtdept.grid(row=2,column=3)

        

        #Attribute4:::HOD
        labelhod=Label(df2,font=("arial",12,"bold"),text="HOD",padx=2,pady=6)
        labelhod.grid(row=3,column=2,sticky=W)
        txthod=Entry(df2,font=("arial",12,"bold"),textvariable=self.HOD,width=35)
        txthod.grid(row=3,column=3)

        

        #Attribute 4:Phone
        labelphone=Label(df2,font=("arial",12,"bold"),text="Phone",padx=2,pady=6)
        labelphone.grid(row=4,column=2,sticky=W)
        txtphone=Entry(df2,font=("arial",12,"bold"),textvariable=self.Phone,width=35)
        txtphone.grid(row=4,column=3)

        #Attribute 5:Email
        labele=Label(df2,font=("arial",12,"bold"),text="Dept_Email",padx=2,pady=6)
        labele.grid(row=5,column=2,sticky=W)
        txte=Entry(df2,font=("arial",12,"bold"),textvariable=self.Dept_Email,width=35)
        txte.grid(row=5,column=3)


        #Attribute 6:location
        labell=Label(df2,font=("arial",12,"bold"),text="Location",padx=2,pady=6)
        labell.grid(row=6,column=2,sticky=W)
        txtl=Entry(df2,font=("arial",12,"bold"),textvariable=self.location,width=35)
        txtl.grid(row=6,column=3)


       


        #__________________________________________________Inserting attributes in 3rd frame(Fee payment)_____________________________________
        #Attribute1:::payment ID
        labelpid=Label(df3,font=("arial",12,"bold"),text="Payment ID",padx=2,pady=6)
        labelpid.grid(row=0,column=3,sticky=W)
        txtpid=Entry(df3,font=("arial",12,"bold"),textvariable=self.PaymentID,width=35)
        txtpid.grid(row=0,column=4)

        

        #Attribute2:::Fine
        labelfine=Label(df3,font=("arial",12,"bold"),text="Fine",padx=2,pady=6)
        labelfine.grid(row=4,column=3,sticky=W)
        txtfine=Entry(df3,font=("arial",12,"bold"),textvariable=self.Fineifany,width=35)
        txtfine.grid(row=4,column=4)

        

        #Attribute3:::Amount paid
        labelamt=Label(df3,font=("arial",12,"bold"),text="Amount paid",padx=2,pady=6)
        labelamt.grid(row=2,column=3,sticky=W)
        txtamt=Entry(df3,font=("arial",12,"bold"),textvariable=self.Amountpaid,width=35)
        txtamt.grid(row=2,column=4)

        
        
        #Attribute4:::date
        labeld=Label(df3,font=("arial",12,"bold"),text="Date of payment",padx=2,pady=6)
        labeld.grid(row=3,column=3,sticky=W)
        txtd=Entry(df3,font=("arial",12,"bold"),textvariable=self.Paymentdate,width=35)
        txtd.grid(row=3,column=4)

        

        #Attribute5:::Payment Method
        labelpm=Label(df3,font=("arial",12,"bold"),text="Payment method",padx=2,pady=6)
        labelpm.grid(row=1,column=3,sticky=W)
        txtpm=Entry(df3,font=("arial",12,"bold"),textvariable=self.PaymentMethod,width=35)
        txtpm.grid(row=1,column=4)

        

        #attribute 6:Fee type
        labelft=Label(df3,font=("arial",12,"bold"),text="Fee Type",padx=2,pady=6)
        labelft.grid(row=6,column=3,sticky=W)
        txtft=Entry(df3,font=("arial",12,"bold"),textvariable=self.FeeType,width=35)
        txtft.grid(row=6,column=4)

        #attribute 7:Reciept Number
        labelr=Label(df3,font=("arial",12,"bold"),text="Reciept Number",padx=2,pady=6)
        labelr.grid(row=7,column=3,sticky=W)
        txtr=Entry(df3,font=("arial",12,"bold"),textvariable=self.RecieptNumber,width=35)
        txtr.grid(row=7,column=4)


        #__________________________________________________Inserting attributes in 4th frame(Exam results)______________________________________
        #Attribute1:::SEMESTER
        labelsem=Label(df4,font=("arial",12,"bold"),text="Semester",padx=2,pady=6)
        labelsem.grid(row=0,column=5,sticky=W)
        txtsem=Entry(df4,font=("arial",12,"bold"),textvariable=self.Sem,width=35)
        txtsem.grid(row=0,column=6)

        

        #Attribute2:::SGPA
        labelcgpa=Label(df4,font=("arial",12,"bold"),text="SGPA",padx=2,pady=6)
        labelcgpa.grid(row=1,column=5,sticky=W)
        txtcgpa=Entry(df4,font=("arial",12,"bold"),textvariable=self.SGPA,width=35)
        txtcgpa.grid(row=1,column=6)


        

        #Attribute3:::Pass/Fail
        labelPF=Label(df4,font=("arial",12,"bold"),text="Pass or Fail",padx=2,pady=6)
        labelPF.grid(row=2,column=5,sticky=W)
        txtPF=Entry(df4,font=("arial",12,"bold"),textvariable=self.PassORFail,width=35)
        txtPF.grid(row=2,column=6)


        

        #attribute 4:Even/odd semester
        labeleo=Label(df4,font=("arial",12,"bold"),text="Even OR odd",padx=2,pady=6)
        labeleo.grid(row=4,column=5,sticky=W)
        txteo=Entry(df4,font=("arial",12,"bold"),textvariable=self.EvenORodd,width=35)
        txteo.grid(row=4,column=6)

        #attribute 5:percentage
        labelP=Label(df4,font=("arial",12,"bold"),text="Percentage",padx=2,pady=6)
        labelP.grid(row=5,column=5,sticky=W)
        txtP=Entry(df4,font=("arial",12,"bold"),textvariable=self.Percentage,width=35)
        txtP.grid(row=5,column=6)

        #attribute 6:CGPA
        labelb=Label(df4,font=("arial",12,"bold"),text="CGPA",padx=2,pady=6)
        labelb.grid(row=6,column=5,sticky=W)
        txtb=Entry(df4,font=("arial",12,"bold"),textvariable=self.CGPA,width=35)
        txtb.grid(row=6,column=6)

        #Attribute 7:Batch
        labelba=Label(df4,font=("arial",12,"bold"),text="Batch",padx=2,pady=6)
        labelba.grid(row=7,column=5,sticky=W)
        txtba=Entry(df4,font=("arial",12,"bold"),textvariable=self.Batch,width=35)
        txtba.grid(row=7,column=6)

        #___________________________________________________________-Buttons________________________________________________

        #INSERT button
        btnInsert=Button(buttonframe,command=self.insert_data,text="INSERT",bg="green",fg="white",font=("times new roman",12,"bold"),width=28)
        btnInsert.grid(row=0,column=0)

        #UPDATE button
        btnUpdate=Button(buttonframe,command=self.update,text="UPDATE",bg="green",fg="white",font=("times new roman",12,"bold"),width=28)
        btnUpdate.grid(row=0,column=1)

        #DELETE button
        btndel=Button(buttonframe,command=self.delete,text="DELETE",bg="green",fg="white",font=("times new roman",12,"bold"),width=28)
        btndel.grid(row=0,column=2)

        #CLEAR button
        btnCL=Button(buttonframe,command=self.clear,text="CLEAR",bg="green",fg="white",font=("times new roman",12,"bold"),width=28)
        btnCL.grid(row=0,column=3)

        #EXIT button
        btnexit=Button(buttonframe,command=self.exit,text="EXIT",bg="green",fg="white",font=("times new roman",12,"bold"),width=28)
        btnexit.grid(row=0,column=4)


        #__________________________________________________________-Scroll Bar for X n Y axis__________________________________________________
        scroll_x=ttk.Scrollbar(dbframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dbframe,orient=VERTICAL)
        self.RUAS_table=ttk.Treeview(dbframe,column=("Full Name","Student ID","Father's Name","Mother's Name","Mobile No","Gender","Email","Branch ID",
                                                     "Branch Name","Department","HOD","Phone","Dept_Email","Location","Payment ID","Payment Method","Amount paid","Payment date",
                                                     "Fine if any","Fee Type","Reciept Number","Sem","SGPA","Pass/Fail","Even OR odd","Percentage","CGPA","Batch"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.RUAS_table.xview)
        scroll_y=ttk.Scrollbar(command=self.RUAS_table.yview)

        self.RUAS_table.heading("Full Name",text="Full Name")
        self.RUAS_table.heading("Student ID",text="Student ID")
        self.RUAS_table.heading("Mother's Name",text="Mother's Name")
        self.RUAS_table.heading("Father's Name",text="Father's Name")
        self.RUAS_table.heading("Mobile No",text="Mobile No")
        self.RUAS_table.heading("Email",text="Email")
        self.RUAS_table.heading("Gender",text="Gender")

        self.RUAS_table.heading("Branch ID",text="Branch ID")
        self.RUAS_table.heading("Branch Name",text="Branch Name")
        self.RUAS_table.heading("Department",text="Department")
        self.RUAS_table.heading("HOD",text="HOD")
        self.RUAS_table.heading("Phone",text="Phone")
        self.RUAS_table.heading("Dept_Email",text="Dept_Email")
        self.RUAS_table.heading("Location",text="Location")

        self.RUAS_table.heading("Payment ID",text="Payment ID")
        self.RUAS_table.heading("Payment Method",text="Payment Method")
        self.RUAS_table.heading("Amount paid",text="Amount paid")
        self.RUAS_table.heading("Payment date",text="Payment date")
        self.RUAS_table.heading("Fine if any",text="Fine if any")
        self.RUAS_table.heading("Fee Type",text="Fee Type")
        self.RUAS_table.heading("Reciept Number",text="Reciept Number")

        self.RUAS_table.heading("Sem",text="Sem")
        self.RUAS_table.heading("SGPA",text="SGPA")
        self.RUAS_table.heading("Pass/Fail",text="Pass/Fail")
        self.RUAS_table.heading("Even OR odd",text="Even OR odd")
        self.RUAS_table.heading("Percentage",text="Percentage")
        self.RUAS_table.heading("CGPA",text="CGPA")        
        self.RUAS_table.heading("Batch",text="Batch")


        self.RUAS_table["show"]="headings"

        self.RUAS_table.column("Full Name",width=100)
        self.RUAS_table.column("Student ID",width=100)
        self.RUAS_table.column("Mother's Name",width=100)
        self.RUAS_table.column("Father's Name",width=100)
        self.RUAS_table.column("Mobile No",width=100)
        self.RUAS_table.column("Gender",width=100)
        self.RUAS_table.column("Email",width=100)
        
       

        self.RUAS_table.column("Branch ID",width=100)
        self.RUAS_table.column("Branch Name",width=100)
        self.RUAS_table.column("Department",width=100)
        self.RUAS_table.column("HOD",width=100)
        self.RUAS_table.column("Phone",width=100)
        self.RUAS_table.column("Dept_Email",width=100)
        self.RUAS_table.column("Location",width=100)

        self.RUAS_table.column("Payment ID",width=100)
        self.RUAS_table.column("Payment Method",width=100)
        self.RUAS_table.column("Amount paid",width=100)
        self.RUAS_table.column("Payment date",width=100)
        self.RUAS_table.column("Fine if any",width=100)
        self.RUAS_table.column("Fee Type",width=100)
        self.RUAS_table.column("Reciept Number",width=100)


        self.RUAS_table.column("Sem",width=100)
        self.RUAS_table.column("SGPA",width=100)
        self.RUAS_table.column("Pass/Fail",width=100)
        self.RUAS_table.column("Even OR odd",width=100)
        self.RUAS_table.column("Percentage",width=100)     
        self.RUAS_table.column("CGPA",width=100)
        self.RUAS_table.column("Batch",width=100)


        self.RUAS_table.pack(fill=BOTH,expand=1)
        self.RUAS_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

    #________________________functionality declaration______________________________________
    # def insert_data(self):
    #     if (self.FullName.get().strip() == ""):  # Check if any field is empty
    #          messagebox.showerror("Error", "All fields are required")

    #     else:
    #         try:
    #           conn = mysql.connector.connect(host="localhost", username="root", password="Chaithra@123", database="ruas")
    #           my_cursor = conn.cursor()

    #         # Insert data into student_details table
    #           my_cursor.execute("INSERT INTO student_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
    #                           (self.FullName.get(), self.StudentID.get(), self.FathersName.get(),
    #                            self.MothersName.get(), self.MobileNo.get(), self.gender.get(), self.Email.get()))

    #         # Insert data into branch_details table
    #           my_cursor.execute("INSERT INTO branch_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
    #                           (self.BranchID.get(), self.BranchName.get(), self.Department.get(),
    #                            self.HOD.get(), self.Phone.get(), self.Dept_Email.get(), self.location.get()))

    #         # Insert data into fee_payment_details table
    #           my_cursor.execute("INSERT INTO fee_payment_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
    #                           (self.PaymentID.get(), self.PaymentMethod.get(), self.Amountpaid.get(),
    #                            self.Paymentdate.get(), self.Fineifany.get(), self.FeeType.get(),
    #                            self.RecieptNumber.get()))

    #         # Insert data into exam_results table
    #           my_cursor.execute("INSERT INTO exam_results VALUES (%s,%s,%s,%s,%s,%s,%s)",
    #                           (self.Sem.get(), self.SGPA.get(), self.PassORFail.get(), self.EvenORodd.get(),
    #                            self.Percentage.get(), self.CGPA.get(), self.Batch.get()))
            

    #           conn.commit()
    #           self.fetch_data()  # Refresh the displayed data after insertion
    #           conn.close()
    #           messagebox.showinfo("Success", "Data has been inserted successfully", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    def insert_data(self):
      try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Chaithra@123", database="ruas")
        my_cursor = conn.cursor()

        # Start a transaction
        conn.start_transaction()

        # Insert data into student_details table
        my_cursor.execute("INSERT INTO student_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
                          (self.FullName.get(), self.StudentID.get(), self.FathersName.get(),
                           self.MothersName.get(), self.MobileNo.get(), self.gender.get(), self.Email.get()))

        # Insert data into branch_details table
        my_cursor.execute("INSERT INTO branch_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
                          (self.BranchID.get(), self.BranchName.get(), self.Department.get(),
                           self.HOD.get(), self.Phone.get(), self.Dept_Email.get(), self.location.get()))

        # Insert data into fee_payment_details table
        my_cursor.execute("INSERT INTO fee_payment_details VALUES (%s,%s,%s,%s,%s,%s,%s)",
                          (self.PaymentID.get(), self.PaymentMethod.get(), self.Amountpaid.get(),
                           self.Paymentdate.get(), self.Fineifany.get(), self.FeeType.get(),
                           self.RecieptNumber.get()))

        # Insert data into exam_results table
        my_cursor.execute("INSERT INTO exam_results VALUES (%s,%s,%s,%s,%s,%s,%s)",
                          (self.Sem.get(), self.SGPA.get(), self.PassORFail.get(), self.EvenORodd.get(),
                           self.Percentage.get(), self.CGPA.get(), self.Batch.get()))

        # Commit the transaction if all inserts succeed
        conn.commit()
        self.fetch_data()  # Refresh the displayed data after insertion
        conn.close()
        messagebox.showinfo("Success", "Data has been inserted successfully", parent=self.root)

      except Exception as es:
        conn.rollback()  # Rollback the transaction if any insert fails
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


        
    # def fetch_data(self):
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Chaithra@123",database="ruas")
    #     my_cursor=conn.cursor()
    #     my_cursor.execute("SELECT * FROM student_details,branch_details,fee_payment_details,exam_results")
        
    #     rows=my_cursor.fetchall()
    #     if len(rows)!=0:
    #         self.RUAS_table.delete(*self.RUAS_table.get_children())
    #         for i in rows:
    #             self.RUAS_table.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()
    def fetch_data(self):
      try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Chaithra@123", database="ruas")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student_details, branch_details, fee_payment_details, exam_results")
        rows = my_cursor.fetchall()

        # Clearing existing data in the table
        self.RUAS_table.delete(*self.RUAS_table.get_children())

        for row in rows:
            # Check if the row is already present in the table
            present = False
            for item in self.RUAS_table.get_children():
                if self.RUAS_table.item(item, 'values') == row:
                    present = True
                    break

            # If the row is not present, insert it into the table
            if not present:
                self.RUAS_table.insert("", END, values=row)

        conn.close()
      except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch data: {str(e)}", parent=self.root)

                
  
    
    def get_cursor(self, event=""):
      try:
        cursor_row = self.RUAS_table.focus()
        content = self.RUAS_table.item(cursor_row)
        row = content["values"]
        self.FullName.set(row[0])
        self.StudentID.set(row[1])
        self.FathersName.set(row[2])
        self.MothersName.set(row[3])
        self.MobileNo.set(row[4])
        self.gender.set(row[5])
        self.Email.set(row[6])
        self.BranchID.set(row[7])
        self.BranchName.set(row[8])
        self.Department.set(row[9])
        self.HOD.set(row[10])
        self.Phone.set(row[11])
        self.Dept_Email.set(row[12])
        self.location.set(row[13])
        self.PaymentID.set(row[14])
        self.PaymentMethod.set(row[15])
        self.Amountpaid.set(row[16])
        self.Paymentdate.set(row[17])
        self.Fineifany.set(row[18])
        self.FeeType.set(row[19])
        self.RecieptNumber.set(row[20])
        self.Sem.set(row[21]) # Correct index for Sem
        self.SGPA.set(row[22]) # Correct index for SGPA
        self.PassORFail.set(row[23]) # Correct index for PassORFail
        self.EvenORodd.set(row[24]) # Correct index for EvenORodd
        self.Percentage.set(row[25]) # Correct index for Percentage
        self.CGPA.set(row[26]) # Correct index for CGPA
        self.Batch.set(row[27]) # Correct index for Batch
      except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    
    
    def update(self):
      try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Chaithra@123", database="ruas")
        my_cursor = conn.cursor()

        # Update student_details table
        my_cursor.execute("UPDATE student_details SET Full_Name=%s, Father_Name=%s, Mother_Name=%s, Mobile_NO=%s, Gender=%s, Email=%s WHERE Student_ID=%s", (
            self.FullName.get(), self.FathersName.get(), self.MothersName.get(), self.MobileNo.get(), self.gender.get(), self.Email.get(), self.StudentID.get()))

        # Update branch_details table
        my_cursor.execute("UPDATE branch_details SET Branch_Name=%s, Department=%s, HOD=%s, Phone=%s, Dept_Email=%s, Location=%s WHERE Branch_ID=%s", (
            self.BranchName.get(), self.Department.get(), self.HOD.get(), self.Phone.get(), self.Dept_Email.get(), self.location.get(), self.BranchID.get()))

        # Update fee_payment_details table
        my_cursor.execute("UPDATE fee_payment_details SET Payment_Method=%s, Amount_paid=%s, date_of_payment=%s, Fine=%s, Fee_Type=%s, Reciept_Number=%s WHERE Payment_ID=%s", (
            self.PaymentMethod.get(), self.Amountpaid.get(), self.Paymentdate.get(), self.Fineifany.get(), self.FeeType.get(), self.RecieptNumber.get(), self.PaymentID.get()))

        # Update exam_results table
        my_cursor.execute("UPDATE exam_results SET Semester=%s, Pass_or_fail=%s, EvenOrOdd=%s, Percentage=%s, CGPA=%s, Batch=%s WHERE SGPA=%s", (
            self.Sem.get(), self.PassORFail.get(), self.EvenORodd.get(), self.Percentage.get(), self.CGPA.get(), self.Batch.get(), self.SGPA.get()))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Record has been updated successfully")
      except Exception as es:
        messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    
    def delete(self): 
        
         conn=mysql.connector.connect(host="localhost",username="root",password="Chaithra@123",database="ruas")
         my_cursor=conn.cursor()

         query1="DELETE FROM student_details WHERE Student_ID=%s" 
         value1=(self.StudentID.get(),)
         my_cursor.execute(query1,value1)

         query2="DELETE FROM branch_details WHERE Branch_ID=%s"
         value2=(self.BranchID.get(),)
         my_cursor.execute(query2,value2)

         query3="DELETE FROM fee_payment_details WHERE Payment_ID=%s"
         value3=(self.PaymentID.get(),)
         my_cursor.execute(query3,value3)

         query4="DELETE FROM exam_results WHERE Semester=%s"
         value4=(self.Sem.get(),)
         my_cursor.execute(query4,value4)



         conn.commit()
         self.fetch_data()
         conn.close()
         
         messagebox.showinfo("Delete","Data has been deleted successfully")
        

    def clear(self):
           self.FullName.set("")
           self.StudentID.set("")
           self.MothersName.set("")
           self.FathersName.set("")
           self.MobileNo.set("")
           self.Email.set("")
           self.gender.set("")

           self.BranchID.set("")
           self.BranchName.set("")
           self.Department.set("")
           self.HOD.set("")
           self.Phone.set("")
           self.Dept_Email.set("")
           self.location.set("")

           self.PaymentID.set("")
           self.PaymentMethod.set("")
           self.Amountpaid.set("")
           self.Paymentdate.set("")
           self.Fineifany.set("")
           self.FeeType.set("")
           self.RecieptNumber.set("")

           self.Sem.set("")
           self.SGPA.set("")
           self.PassORFail.set("")
           self.EvenORodd.set("")
           self.Percentage.set("")
           self.CGPA.set("")
           self.Batch.set("")
    def exit(self):
         exit=messagebox.askyesno("RUAS Student Management System","Confirm if you want to exit")
         if exit>0:
              root.destroy()
              return

                                                                                                           
if __name__=="__main__": 
    root=Tk()
    ob=Ruas(root)
    root.mainloop()  


 
