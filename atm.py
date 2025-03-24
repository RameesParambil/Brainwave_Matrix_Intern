import tkinter as tk

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

        acLbl = tk.Label(optFrame, text="Account_No:", bg=self.clr(160,200,250), font=("Arial", 15, "bold"))
        acLbl.grid(row=0, column=0, padx=20, pady=30)

        #detail frame

        detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg=self.clr(240,180,150))
        detFrame.place(width=self.width/2 ,height=self.height-180 ,x=self.width/3+140 ,y=100 )

    def clr(self, r,g,b):
        return f"#{r:02x}{g:02x}{b:02x}"
        
        
        

root = tk.Tk()
obj = atm(root)
root.mainloop()