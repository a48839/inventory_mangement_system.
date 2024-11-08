from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class categoryclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System By Raynox")
        self.root.config(bg="white")
        self.root.focus_force()

        #variable=====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        # title=====

        lbl_title=Label(self.root,text="Manage Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_name=Label(self.root,text="Category Name ",font=("goudy old style",30),bg="white",fg="black").place(x=50,y=100)
        lbl_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)


        #===== category detail=========

        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=700, y=120,width=380, height=100)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame, columns=('cid', 'name'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.categoryTable.yview)
        scrollx.config(command=self.categoryTable.xview)

        self.categoryTable.heading('cid', text="C ID")
        self.categoryTable.heading('name', text="Name")
        
        
        self.categoryTable["show"] = "headings"

        self.categoryTable.column('cid', width=100)
        self.categoryTable.column('name', width=100)
        
        
        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        #images=======
        

        self.im1 = Image.open("IMS/cat2.jpg")
        self.im1 = self.im1.resize((300, 200), Image.Resampling.LANCZOS)  # Use LANCZOS for better quality
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.lbl_im1 = Label(self.root, image=self.im1)
        self.lbl_im1.place(x=50, y=220)

        self.show()



    def add(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "category name must be required", parent=self.root)
            else:
                cur.execute("SELECT * from category where name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Category is already present", parent=self.root)
                else:
                    cur.execute("INSERT into category(name) values(?)", (
                        self.var_name.get(),
                        
                    )) 
                    con.commit()
                    messagebox.showinfo("Success", "category added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()        


    def get_data(self, ev):
        try:
            f = self.categoryTable.focus()
            content = self.categoryTable.item(f)
            row = content.get('values', [])

            if row:  # Check if the row has data
                self.var_cat_id.set(row[0])  # Assuming row[0] is always present
                if len(row) > 1:
                    self.var_name.set(row[1])  # Set name only if it exists in the row
                else:
                    self.var_name.set("")  # Clear the variable if no name is present
            else:
                self.var_cat_id.set("")
                self.var_name.set("")
        except IndexError as e:
            messagebox.showerror("Error", f"Data could not be retrieved: {str(e)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid category name", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFIRM", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE from category where cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE", "category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = categoryclass(root)
    root.mainloop()
