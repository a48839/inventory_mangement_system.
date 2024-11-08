from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class productclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System By Raynox")
        self.root.config(bg="white")
        self.root.focus_force()

        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,width=420,height=480)


        #=======variable===
        self.var_Searchby=StringVar()
        self.var_Searchtxt=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()
        self.var_cat=StringVar()

        title=Label(product_frame,text="product Details",font=("goudy old style",18),bg="#0f4d7d",fg="white",).pack(side=TOP,fill=X)
        lbl_cat=Label(self.root,text="Category ",font=("goudy old style",15),bg="white").place(x=30,y=60)
        lbl_supplier=Label(self.root,text="supplier ",font=("goudy old style",15),bg="white").place(x=30,y=110)
        lbl_product=Label(self.root,text="Product Name ",font=("goudy old style",15),bg="white").place(x=30,y=160)
        lbl_price=Label(self.root,text="price ",font=("goudy old style",15),bg="white").place(x=30,y=210)
        lbl_quantity=Label(self.root,text="quantity ",font=("goudy old style",15),bg="white").place(x=30,y=260)
        lbl_status=Label(self.root,text="status ",font=("goudy old style",15),bg="white").place(x=30,y=310)


        # Search Options
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=160,y=60,width=200)
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=160,y=100,width=200)
        cmb_sup.current(0)

        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=160,y=150,width=200)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=160,y=200,width=200)
        txt_quantity=Entry(product_frame,textvariable=self.var_quantity,font=("goudy old style",15),bg="lightyellow").place(x=160,y=250,width=200)
        

        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("select","Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=160,y=300,width=200)
        cmb_status.current(0)


        # Buttons
        btn_add=Button( product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="darkblue",fg="white",cursor="hand2").place(x=10,y=400,width=110,height=28)
        btn_update=Button( product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=120,y=400,width=110,height=28)
        btn_delete=Button( product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=230,y=400,width=110,height=28)
        btn_clear=Button( product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=340,y=400,width=110,height=28)



        # Search Frame
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)

        # Search Options
        cmb_Search=ttk.Combobox(SearchFrame,textvariable=self.var_Searchby,values=("select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_Search.place(x=10,y=10,width=180)
        cmb_Search.current(0)

        txt_Search=Entry(SearchFrame,textvariable=self.var_Searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_Search=Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=30)


        # Product Details Table
        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(p_frame,columns=('pid','Supplier','Category','name','price','quantity','status'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.config(command=self.productTable.yview)
        scrollx.config(command=self.productTable.xview)

        self.productTable.heading('pid',text="Product ID")
        self.productTable.heading('Category',text="Category")
        self.productTable.heading('Supplier',text="Supplier")
        self.productTable.heading('name',text="Name")
        self.productTable.heading('price',text="Price")
        self.productTable.heading('quantity',text="Quantity")
        self.productTable.heading('status',text="Status")
       
        self.productTable["show"]="headings"

        self.productTable.column('pid',width=100)
        self.productTable.column('Category',width=100)
        self.productTable.column('Supplier',width=100)
        self.productTable.column('name',width=100)
        self.productTable.column('price',width=100)
        self.productTable.column('quantity',width=100)
        self.productTable.column('status',width=100)
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        


#===============================
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * from category")
            cat=cur.fetchall()
            
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            
            cur.execute("SELECT * from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
            
            #print(sup)
            

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        finally:
            con.close()    


    def add(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select"  or self.var_cat.get()=="empty" or self.var_sup.get()=="Select"  or self.var_name.get()=="name":
                messagebox.showerror("Error","All feilds are required",parent=self.root)
            else:
                cur.execute("SELECT * from product where name=? ",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product is already Present",parent=self.root)
                else:
                    cur.execute("INSERT into product(pid,Supplier,Category,name,price,quantity,status) values(?,?,?,?,?,?,?)",(
                           self.var_cat.get(),
                           self.var_sup.get(),
                           self.var_name.get(),
                           self.var_price.get(),
                           self.var_quantity.get(),
                           self.var_status.get(),
                           
                    )) 
                    con.commit()
                    messagebox.showinfo("Success","Product added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        finally:
            con.close()
    def show(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    def get_data(self, ev):
        f = self.productTable.focus()
        content = self.productTable.item(f)
        row = content['values']
        if row:
            self.var_pid.get()
            self.var_cat.get()
            self.var_sup.get()
            self.var_name.get()
            self.var_price.get()
            self.var_quantity.get()
            self.var_status.get()

    def update(self):
        con=sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("SELECT * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parent=self.root)
                else:
                    cur.execute("update product set Category=?,Supplier=?,name=?,price=?,quantity=?,status=? where pid=?",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.setget(),
                        self.var_pid.get(),


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
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)    



if __name__=="__main__":
    root=Tk()
    obj=productclass(root)
    root.mainloop()        