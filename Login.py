from customtkinter import *
from PIL import Image
from tkinter import messagebox



#create a function
def login():
    if userentry.get()=="" or passwordentry.get()=="":
        messagebox.showerror("Error","all fields are required")
    elif userentry.get()=="Simran" and passwordentry.get()=="1234": 
        messagebox.showinfo("Success","You are successfully login")
        root.destroy()  
        # Close the login window
        import ems
        open_ems_interface() 
    else:
        messagebox.showerror("Error","wrong Credentials")

        
root=CTk()
root.geometry('860x605')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('ll.jpg'),size=(860,605))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text="Employee Management System",text_color="dark blue",bg_color="#FAFAFA",font=("Arial",16,'bold'))
headinglabel.place(x=20,y=100) 
userentry=CTkEntry(root,placeholder_text="Enter your Username",bg_color="#000000",text_color="#FFFFFF",width=180)
userentry.place(x=50,y=150)
passwordentry=CTkEntry(root,placeholder_text="Enter your Password",bg_color="#000000",text_color="#FFFFFF",width=180,show='*')
passwordentry.place(x=50,y=200)




loginButton=CTkButton(root,text="LOGIN",cursor="hand2",command=login)
loginButton.place(x=50,y=260)


root.mainloop() 

