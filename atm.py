import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class atm():
    def __init__(self,root):
        self.root = root
        self.root.title("Atm Machine Management")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title = tk.Label(self.root, text="Atm Machine Management System", bd=4, relief="groove", bg="light gray", font=("Arial", 50, "bold"))
        title.pack(side="top", fill="x")

        #option frame

        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(160,200,250))
        optFrame.place(width=self.width/3 ,height=self.height-180 ,x=70 ,y=100 )

        atmLbl = tk.Label(optFrame, text="Atm_Card:", bg=self.clr(160,200,250), font=("Arial", 15, "bold"))
        atmLbl.grid(row=0, column=0, padx=20, pady=30)
        self.atm = tk.Entry(optFrame, width=20, font=("Arial",15), bd=2)
        self.atm.grid(row=0, column=1, padx=10, pady=20)

        pwLbl = tk.Label(optFrame, text="Password:", bg=self.clr(160,200,250), font=("Arial",15,"bold"))
        pwLbl.grid(row=1, column=0, padx=20, pady=30)
        self.pw = tk.Entry(optFrame, width=20, font=("Arial",15), bd=2)
        self.pw.grid(row=1, column=1, padx=20, pady=30)

        inqLbl = tk.Label(optFrame, text="Balance Inquiry:", bg=self.clr(160,200,250), font=("Arial",12,"bold"))
        inqLbl.grid(row=2, column=0, padx=20, pady=30)
        inqBtn = tk.Button(optFrame, text="Enter", width=8, bd=2, relief="raised", font=("Arial",15,"bold"))
        inqBtn.grid(row=2, column=1, padx=10, pady=30)

        wdLbl = tk.Label(optFrame, text="Cash Withdraw:", bg=self.clr(160,200,250), font=("Arial",12,"bold"))
        wdLbl.grid(row=3, column=0, padx=20, pady=30)
        wdBtn = tk.Button(optFrame, text="Enter", width=8, bd=2, relief="raised", font=("Arial",15,"bold"))
        wdBtn.grid(row=3, column=1, padx=10, pady=30)

        transLbl = tk.Label(optFrame, text="Transaction:", bg=self.clr(160,200,250), font=("Arial",12,"bold"))
        transLbl.grid(row=4, column=0, padx=20, pady=30)
        transBtn = tk.Button(optFrame, text="Enter", width=8, bd=2, relief="raised", font=("Arial",15,"bold"))
        transBtn.grid(row=4, column=1, padx=10, pady=30)


        #detail frame

        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(240,180,150))
        self.detFrame.place(width=self.width/2 ,height=self.height-180 ,x=self.width/3+140 ,y=100 )

        lbl = tk.Label(self.detFrame, text="Account Details", bd=3, font=("Arial",30,"bold"), bg=self.clr(240,210,150))
        lbl.pack(side="top", fill="x")
        self.tabFun()

    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/2-40, height=self.height-270, x=17, y=70)

        x_scrol = tk.Scrollbar(tabFrame, orient="horizontal")
        x_scrol.pack(side="bottom", fill="x")

        y_scrol = tk.Scrollbar(tabFrame, orient="vertical")
        y_scrol.pack(side="right", fill="y")

        self.table = ttk.Treeview(tabFrame, xscrollcommand=x_scrol.set, yscrollcommand=y_scrol.set,
                                  columns=("ac","name","bal"))
        
        x_scrol.config(command=self.table.xview)
        y_scrol.config(command=self.table.yview)
        
        self.table.heading("ac", text="Account_No")
        self.table.heading("name", text="User_Name")
        self.table.heading("bal", text="Balance")
        self.table["show" ] = "headings"

        self.table.pack(fill="both", expand=1)

    def inqFun(self):
        atm = self.atm.get()
        p = self.pw.get()

        if atm and p:
            atmNo = int(atm)
            pw = int(p)

        else:
            tk.messagebox.showerror("Error", "Please Fill All Input Fields.")



    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
        
        

root = tk.Tk()
obj = atm(root)
root.mainloop()