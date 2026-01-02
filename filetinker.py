import os
import shutil
from customtkinter import *

class Objects:
    def __init__(self,root):
        self.root = root

        self.first_list = os.path.expanduser("~/Desktop")


        self.labe1 = CTkLabel(root,text="Folder Name",height=36,width=200,font=("Arial",34))
        self.labe1.place(x=10,y=30)
        self.e1 = CTkEntry(root,width=340,height=36,font=("Arial",34),placeholder_text="")
        self.e1.place(x=10,y=80)

        self.labe2 = CTkLabel(root,text="File Name",height=36,width=200,font=("Arial",34))
        self.labe2.place(x=10,y=200)
        self.e2 = CTkEntry(root,width=340,height=36,font=("Arial",34),placeholder_text="")
        self.e2.place(x=10,y=260)



        self.button_accept = CTkButton(root,fg_color="Green",text_color="White",hover_color="Green",
                width=130,height=40,text="+", command=self.create)
        self.button_accept.place(x=40,y=335)

        self.remove_file = CTkButton(root,text="X",text_color="White",fg_color="Red",hover_color="Red",width=130,height=40,command=self.deletion)
        self.remove_file.place(x=180,y=335)




    def create(self):
        self.parent = self.first_list
        self.folder_kid = self.e1.get()
        self.file_kid = self.e2.get()
        r = os.path.join(self.parent, self.folder_kid)
        os.makedirs(r,exist_ok=True)
        v = os.path.join(r,self.file_kid)
        try:
            with open(v,"x") as f:
                pass
        except FileExistsError:
            pass


    def deletion(self):
        self.parent = self.first_list
        self.folder_kid = self.e1.get()
        self.file_kid = self.e2.get()
        try:
            r = os.path.join(self.parent,self.folder_kid)
            v = os.path.join(r,self.file_kid)
            if not self.file_kid:
                shutil.rmtree(r)
            elif not self.file_kid and not self.folder_kid:
                self.e1.configure(placeholder_text="Dumbass!!!")
                self.e2.configure(placeholder_text="Dumbass!!!")
            else:
                os.remove(v)
        except FileNotFoundError:
            self.e1.configure(placeholdertext="NotFound")

            
        
    


    
        


root = CTk()
root.geometry("360x570")
root.resizable(False,False)

app = Objects(root)

app.create

root.mainloop()