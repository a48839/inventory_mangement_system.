from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierclass
from category import categoryclass
from product import productclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Inventory Management System By Raynox")
        self.root.config(bg="white")
        
        self.icon_title=PhotoImage(file="")
        
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="black",fg="white").place(x=0,y=0,relwidth=1,height=70)
        lbl_footer=Label(self.root,text="IMS-Invntory Management System ",font=("times new roman",15,"bold"),bg="grey",fg="white").pack(side=BOTTOM,fill=X)
        btn_logout=Button(self.root,text="Log out",font=("times new roman",15,"bold"),bg="yellow",fg="black",cursor="hand2").place(x=1350,y=20,width=150,height=30)

        self.lbl_clock=Label(self.root,text="Welcome To this system\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:ss",font=("times new roman",15,"bold"),bg="grey",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        

        #self.MenuLogo=Image.open("images/menu_im.png")
        #self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        #self.MenuLogo=ImageTk.PhotoImage(file="D:\python\menu_im.png")


        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        #lbl_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        #lbl_MenuLogo.pack(side=TOP,fill=X)

        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="yellow",fg="black").pack(side=TOP, fill=X)
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Supplier=Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Sales=Button(LeftMenu,text="Sales",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)
        btn_Exit=Button(LeftMenu,text="Exit",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP, fill=X)



        #------content------

        self.lbl_employee=Label(self.root,text="total Employee\n [0]",bd=5,relief=RIDGE,bg="Blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)



        self.lbl_Supplier=Label(self.root,text="total Supplier\n [0]",bd=5,relief=RIDGE,bg="Blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Supplier.place(x=650,y=120,height=150,width=300)



        self.lbl_Category=Label(self.root,text="total Category\n [0]",bd=5,relief=RIDGE,bg="Blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)




        self.lbl_Sales=Label(self.root,text="total Sales\n [0]",bd=5,relief=RIDGE,bg="Blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Sales.place(x=300,y=300,height=150,width=300)




        self.lbl_Product=Label(self.root,text="total Product\n [0]",bd=5,relief=RIDGE,bg="Blue",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Product.place(x=650,y=300,height=150,width=300)


    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

                                
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)



        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()

