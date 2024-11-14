from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database



def delete_all():
    result=messagebox.askyesno("Confirm","Do you really want to delete all the records")
    if result:
         database.deleteall_records()
    else:
        pass
    


def show_all():
    treeview_data()
    SearchEntry.delete(0,END)
    SearchBox.set("Search By")




def search_employee():
    if SearchEntry.get()=="":
        messagebox.showerror("Error","Enter value to search")
    elif SearchBox.get()=="Search By":
        messagebox.showerror("Error","Please select an option")
    else:
       search_data=database.Search(SearchBox.get(),SearchEntry.get())
       tree.delete(*tree.get_children())
       for employee in search_data:
        tree.insert("",END,values=employee)
      


def delete_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select data to delete")
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror("Error","Data is deleted")


def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select data to update")
    else:
        database.update(   
            idEntry.get(),
            NameEntry.get(),
            PhoneEntry.get(),
            RoleBox.get(),
            GenderBox.get(),
            SalaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("success","Data is updated")



def selection(event):
    selected_item=tree.selection()
    if selected_item:
        clear()
        row=tree.item(selected_item)["values"]
        idEntry.insert(0,row[0])
        NameEntry.insert(0,row[1])
        PhoneEntry.insert(0,row[2]) 
        RoleBox.set(row[3])   
        GenderBox.set(row[4])
        SalaryEntry.insert(0,row[5])    


def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("",END,values=employee)


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    NameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    RoleBox.set("Administrator")
    GenderBox.set("MALE")
    SalaryEntry.delete(0, END)
    
#functions

def add_Employee():
    if idEntry.get()==" " or NameEntry.get()==" " or PhoneEntry.get()== " " or SalaryEntry.get()== " ":
        messagebox.showerror("Error","All fields are required")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror("Error","id alreaady exists")
    else:
        # Insert data into the database
        database.insert(
            idEntry.get(),
            NameEntry.get(),
            PhoneEntry.get(),
            RoleBox.get(),
            GenderBox.get(),
            SalaryEntry.get()
        )
        treeview_data()
    clear()
    messagebox.showinfo("Success","data is successfully added")   
    





#GUI part 
window=CTk()
window.geometry('1077x582+100+100')
window.title("Employee Management System")
window.resizable(0,0)
logo=CTkImage(Image.open("oo.jpg"),size=(1077,200))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)
#left frame
leftFrame=CTkFrame(window)
leftFrame.grid(row=1,column=0)
#right side frame
RightFrame=CTkFrame(window)
RightFrame.grid(row=1,column=1)
#ID Label means where the ID will be placed 
IDLabel=CTkLabel(leftFrame,text="ID",font=("Arial",18,"bold"),padx=20,pady=15)
IDLabel.grid(row=1,column=0,sticky="w")
# ID entry means where the box will ne created
idEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
idEntry.grid(row=1,column=1)
#Name Label means where the name will be placed 
NameLabel=CTkLabel(leftFrame,text="Name",font=("Arial",18,"bold"),padx=20,pady=15)
NameLabel.grid(row=2,column=0,sticky="w")
# NAME entry means where the box will ne created 
NameEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
NameEntry.grid(row=2,column=1)
#Phone Label means where the phone will be placed 
PhoneLabel=CTkLabel(leftFrame,text="Phone",font=("Arial",18,"bold"),padx=20,pady=15)
PhoneLabel.grid(row=3,column=0,sticky="w")
# Phone entry means where the box will ne created 
PhoneEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
PhoneEntry.grid(row=3,column=1)
# Role label means where the box will ne placed
RoleLabel=CTkLabel(leftFrame,text="Role",font=("Arial",18,"bold"),padx=20,pady=15)
RoleLabel.grid(row=4,column=0,sticky="w")
role_options=[
    "Administrator",
    "HR Manager",
    "Team Leader",
    "Supervisor",
    "Recruiter",
    "Payroll Specialist",
    "Employee",
    "Compliance Officer",
    "IT Support",
    "Intern",
    "Contractor",
    "Executive",
    "Data Analyst"
]
#for role box so that the options will come in which department you work
RoleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=("Arial",14,"bold"),state="readonly")
RoleBox.grid(row=4,column=1)
RoleBox.set(role_options[0])
# Role label means where the box will ne placed
GenderLabel=CTkLabel(leftFrame,text="Gender",font=("Arial",18,"bold"),padx=20,pady=15)
GenderLabel.grid(row=5,column=0,sticky="w")
Gender_options=[
"MALE",
"FEMALE",
"OTHERS"
]

#for role box so that the options will come in which department you work
GenderBox=CTkComboBox(leftFrame,values=Gender_options,width=180,font=("Arial",14,"bold"),state="readonly")
GenderBox.grid(row=5,column=1)
GenderBox.set(Gender_options[0])

SalaryLabel=CTkLabel(leftFrame,text="Salary",font=("Arial",18,"bold"),padx=20,pady=15)
SalaryLabel.grid(row=6,column=0,sticky="w")

SalaryEntry=CTkEntry(leftFrame,font=("arial",15,"bold"),width=180)
SalaryEntry.grid(row=6,column=1)


#right side frame
RightFrame=CTkFrame(window)
RightFrame.grid(row=1,column=1)

Search_options=["ID","Name","Phone","Role","Gender","Salary"]
SearchBox=CTkComboBox(RightFrame,values=Search_options,state="readonly")
SearchBox.grid(row=0,column=0)
SearchBox.set("Search By")



SearchEntry=CTkEntry(RightFrame)
SearchEntry.grid(row=0,column=1)


SearchButton=CTkButton(RightFrame,text="Search",cursor="hand2",width=100,command=search_employee)
SearchButton.grid(row=0,column=2)

ShowAllButton=CTkButton(RightFrame,text="ShowAll",cursor="hand2",width=100,command=show_all)
ShowAllButton.grid(row=0,column=3)

tree=ttk.Treeview(RightFrame,height=11)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=("ID","Name","Phone","Role","Gender","Salary")



# Configure columns and set widths
tree.column("ID", width=80)
tree.column("Name", width=150)
tree.column("Phone", width=100)
tree.column("Role", width=130)
tree.column("Gender", width=80)
tree.column("Salary", width=100)


# Configure headings
tree.heading("ID",text="ID")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")
tree.config(show="headings")


style = ttk.Style()
style.configure('Treeview.Heading', font=("Arial", 15, "bold"))
style.configure("Treeview",font=("Arial",12,"bold"),background="#161C30",foreground="white")


Scrollbar=ttk.Scrollbar(RightFrame,orient=VERTICAL)
Scrollbar.grid(row=1,column=4,sticky="ns")

ButtonFrame=CTkFrame(window,fg_color="#161C30" )
ButtonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(ButtonFrame,text="NEW EMPLOYEE",cursor="hand2",font=("arial",15,"bold"),width=160,corner_radius=12,command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

AddButton=CTkButton(ButtonFrame,text="Add EMPLOYEE",cursor="hand2",font=("arial",15,"bold"),width=160,corner_radius=12,command=add_Employee)
AddButton.grid(row=0,column=1,pady=5,padx=5)


UpdateButton=CTkButton(ButtonFrame,text="Update EMPLOYEE",cursor="hand2",font=("arial",15,"bold"),width=160,corner_radius=12,command=update_employee)
UpdateButton.grid(row=0,column=2,pady=5,padx=5)



DeleteButton=CTkButton(ButtonFrame,text="Delete EMPLOYEE",cursor="hand2",font=("arial",15,"bold"),width=160,corner_radius=12,command=delete_employee)
DeleteButton.grid(row=0,column=3,pady=5,padx=5)




DeleteAllButton=CTkButton(ButtonFrame,text="DeleteAll EMPLOYEE",cursor="hand2",font=("arial",15,"bold"),width=160,corner_radius=12,command=delete_all)
DeleteAllButton.grid(row=0,column=4,pady=5,padx=5)


treeview_data()


window.bind("<ButtonRelease>",selection)
window.mainloop()






