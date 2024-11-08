from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class supplierclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System By Raynox")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables
        self.var_Searchtxt = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Supplier", bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Search Options
        lbl_search = Label(SearchFrame, text="Search by Invoice No", font=("goudy old style", 15))
        lbl_search.place(x=0, y=10)

        txt_Search = Entry(SearchFrame, textvariable=self.var_Searchtxt, font=("goudy old style", 15), bg="lightyellow")
        txt_Search.place(x=200, y=10)
        btn_Search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="green", fg="white", cursor="hand2")
        btn_Search.place(x=410, y=10, width=150, height=30)

        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 15), bg="blue", fg="white")
        title.place(x=50, y=100, width=1000, height=30)

        # Supplier Details Form
        lbl_supplier_invoice = Label(self.root, text="Invoice No", font=("goudy old style", 15), bg="white", fg="black")
        lbl_supplier_invoice.place(x=50, y=150)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow", fg="black")
        txt_supplier_invoice.place(x=200, y=150, width=180)

        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white", fg="black")
        lbl_name.place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow", fg="black")
        txt_name.place(x=200, y=190, width=180)

        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white", fg="black")
        lbl_contact.place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow", fg="black")
        txt_contact.place(x=200, y=230, width=180)

        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white", fg="black")
        lbl_desc.place(x=50, y=280)
        self.txt_desc = Entry(self.root, font=("goudy old style", 15), bg="lightyellow", fg="black")
        self.txt_desc.place(x=200, y=270, width=300, height=60)

        # Buttons
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="darkblue", fg="white", cursor="hand2")
        btn_add.place(x=480, y=320, width=110, height=28)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="green", fg="white", cursor="hand2")
        btn_update.place(x=600, y=320, width=110, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="red", fg="white", cursor="hand2")
        btn_delete.place(x=720, y=320, width=110, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="grey", fg="white", cursor="hand2")
        btn_clear.place(x=840, y=320, width=110, height=28)

        # Supplier Details Table
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=370, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=('invoice', 'name', 'contact', 'desc'), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.config(command=self.supplierTable.yview)
        scrollx.config(command=self.supplierTable.xview)

        self.supplierTable.heading('invoice', text="Invoice")
        self.supplierTable.heading('name', text="Name")
        self.supplierTable.heading('contact', text="Contact")
        self.supplierTable.heading('desc', text="Description")
        self.supplierTable["show"] = "headings"

        self.supplierTable.column('invoice', width=100)
        self.supplierTable.column('name', width=100)
        self.supplierTable.column('contact', width=100)
        self.supplierTable.column('desc', width=100)
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    def add(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice number must be required", parent=self.root)
            else:
                cur.execute("SELECT * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Invoice number is already assigned", parent=self.root)
                else:
                    cur.execute("INSERT into supplier(invoice, name, contact, desc) values(?, ?, ?, ?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get(),
                    )) 
                    con.commit()
                    messagebox.showinfo("Success", "Supplier added successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * from supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete(0, END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice number must be required", parent=self.root)
            else:
                cur.execute("SELECT * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid invoice number", parent=self.root)
                else:
                    cur.execute("UPDATE supplier set name=?, contact=?, desc=? where invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get(),
                        self.var_sup_invoice.get(),
                    )) 
                    con.commit()
                    messagebox.showinfo("Success", "Supplier updated successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r"C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice number must be required", parent=self.root)
            else:
                cur.execute("SELECT * from supplier where invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid supplier invoice", parent=self.root)
                else:
                    op = messagebox.askyesno("CONFIRM", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE from supplier where invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("DELETE", "Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete(0, END)
        self.var_Searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r"VS CODE/C:\Users\james\OneDrive\Desktop\iventory management system\ims.db")
        cur = con.cursor()
        try:
            if self.var_Searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice number should be required", parent=self.root)
            else:
                cur.execute("SELECT * from supplier where invoice=?", (self.var_Searchtxt.get(),))
                row = cur.fetchone()
                if row != None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = supplierclass(root)
    root.mainloop()
