from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System By Raynox")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_Searchby=StringVar()
        self.var_Searchtxt=StringVar()
        self.var_name=StringVar()
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_address=StringVar()
        self.var_salary=StringVar()

        # Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        # Search Options
        cmb_Search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_Search.place(x=10,y=10,width=180)
        cmb_Search.current(0)

        txt_Search=Entry(SearchFrame,textvariable=self.var_Searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_Search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)

        # Title
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="blue",fg="white",).place(x=50,y=100,width=1000,height=30)

        # Employee Details Form
        # Row 1
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white",fg="black",).place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white",fg="black",).place(x=375,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white",fg="black",).place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=850,y=150,width=180)

        # Row 2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white",fg="black",).place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white",fg="black",).place(x=375,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white",fg="black",).place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=850,y=190,width=180)

        # Row 3
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white",fg="black",).place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white",fg="black",).place(x=375,y=230)
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white",fg="black",).place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        # Row 4
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white",fg="black",).place(x=50,y=280)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white",fg="black",).place(x=500,y=280)

        self.txt_address=Entry(self.root,textvariable=self.var_address,font=("goudy old style",15),bg="lightyellow",fg="black",)
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow",fg="black",).place(x=600,y=280,width=180)

        # Buttons
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="darkblue",fg="white",cursor="hand2").place(x=480,y=320,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=600,y=320,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=720,y=320,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=840,y=320,width=110,height=28)

        # Employee Details Table
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=370,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=('eid','name','email','gender','contact','dob','doj','pass','utype','address','salary'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.config(command=self.EmployeeTable.yview)
        scrollx.config(command=self.EmployeeTable.xview)

        self.EmployeeTable.heading('eid',text="EMP ID")
        self.EmployeeTable.heading('name',text="NAME")
        self.EmployeeTable.heading('email',text="EMAIL")
        self.EmployeeTable.heading('gender',text="GENDER")
        self.EmployeeTable.heading('contact',text="CONTACT")
        self.EmployeeTable.heading('dob',text="D.O.B")
        self.EmployeeTable.heading('doj',text="D.O.J")
        self.EmployeeTable.heading('pass',text="PASSWORD")
        self.EmployeeTable.heading('utype',text="USER TYPE")
        self.EmployeeTable.heading('address',text="ADDRESS")
        self.EmployeeTable.heading('salary',text="SALARY")
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column('eid',width=100)
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('email',width=100)
        self.EmployeeTable.column('gender',width=100)
        self.EmployeeTable.column('contact',width=100)
        self.EmployeeTable.column('dob',width=100)
        self.EmployeeTable.column('doj',width=100)
        self.EmployeeTable.column('pass',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('address',width=100)
        self.EmployeeTable.column('salary',width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    def add(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID is already assigned",parent=self.root)
                else:
                    cur.execute("INSERT into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                           self.var_emp_id.get(),
                           self.var_name.get(),
                           self.var_email.get(),
                           self.var_gender.get(),
                           self.var_contact.get(),
                           self.var_dob.get(),
                           self.var_doj.get(),
                           self.var_pass.get(),
                           self.var_utype.get(),
                           self.txt_address.get(),
                           self.var_salary.get()
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        finally:
            con.close()
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    def get_data(self, ev) :
        f=self.EmployeeTable.focus()
        content= (self.EmployeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete(END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])
    def update(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Emoployee ID",parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                           self.var_name.get(),
                           self.var_email.get(),
                           self.var_gender.get(),
                           self.var_contact.get(),
                           self.var_dob.get(),
                           self.var_doj.get(),
                           self.var_pass.get(),
                           self.var_utype.get(),
                           self.txt_address.get(),
                           self.var_salary.get(),
                           self.var_emp_id.get()
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","update successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        finally:
            con.close()        
    def delete(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Emoployee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("CONFIRM","Do you really want to continue",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE","Deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        finally:
            con.close()
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete(END),
        self.var_Searchby.set("Select"),
        self.var_Searchtxt.set(""),
        self.show()
    def search(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_Searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_Searchby.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:      
                cur.execute(
    f"SELECT * from employee where {self.var_Searchby.get()} LIKE '%{self.var_Searchtxt.get()}%'"
)
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()
