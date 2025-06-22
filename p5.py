from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *
import re
import pandas as pd
import matplotlib.pyplot as plt


mw=Tk()
mw.geometry("600x600+300+50")
mw.title("Employee Management system")
mw .configure(bg="beige")
mw.iconbitmap("employee.ico")


#Defining all the commands

def go_add():
	aw.deiconify()
	mw.withdraw()

def add_back():
	mw.deiconify()
	aw.withdraw()	

#View Emploee records
def go_view():
	vw.deiconify()
	mw.withdraw()
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["emp_22june25"]
		coll=db["employee"]
		vw_st_view.delete(1.0,END)
		data=coll.find()
		for d in data:
			record=f"Emp ID: {d['_id']}\nName: {d['name']}\nEmail: {d['email']}\nPosition: {d['position']}\nSalary: {d['salary']}\n{'-'*65}\n"
			vw_st_view.insert(END, record)
		

	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
	

def view_back():
	mw.deiconify()
	vw.withdraw()

def go_update():
	uw.deiconify()
	mw.withdraw()

def update_back():
	mw.deiconify()
	uw.withdraw()

def go_delete():
	dw.deiconify()
	mw.withdraw()

def delete_back():
	mw.deiconify()
	dw.withdraw()

# Save Employee Records
def save_emp():
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["emp_22june25"]
		coll=db["employee"]
		
		id=aw_ent_id.get()
		if not id:
			showwarning("Warning","ID should not be Empty")
			aw_ent_id.delete(0, END)
			aw_ent_id.focus()
			return

		if not id.isdigit():
			showwarning("Invalid ID","Employee ID must be an Integer")
			aw_ent_id.delete(0, END)
			aw_ent_id.focus()
			return

		if coll.find_one({"_id":int(id)}):
			showwarning("Duplicate ID","This Employee ID already exists")
			aw_ent_id.delete(0, END)
			aw_ent_id.focus()
			return

		name=aw_ent_name.get()
		if not name:
			showwarning("Warning","Name should not be Empty")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return

		email=aw_ent_email.get()
		if not email:
			showwarning("Warning","Email should not be Empty")
			aw_ent_email.delete(0, END)
			aw_ent_email.focus()
			return
				
		email_regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in|org)$'
		if not re.match(email_regex,email):
			showwarning("Invalid Email","Please enter the valid email address")
			aw_ent_email.delete(0, END)
			aw_ent_email.focus()
			return
			
		position=aw_ent_position.get()
		if not position:
			showwarning("Warning","Position should not be Empty")
			aw_ent_position.delete(0, END)
			aw_ent_position.focus()
			return

		salary=aw_ent_salary.get()
		if not salary:
			showwarning("Warning","Salary should not be Empty")
			aw_ent_salary.delete(0, END)
			aw_ent_salary.focus()
			return

		salary_val=float(salary)
		if salary_val<=0:
			showwarning("Invalid Salary","Salary must be greateer than 0")
			aw_ent_salary.delete(0, END)
			aw_ent_salary.focus()
			return

		info={"_id": int(id), "name":name, "email":email, "position":position, "salary":float(salary)}
		coll.insert_one(info)
		showinfo("Success","Employee Record Created")
		aw_ent_id.delete(0,END)
		aw_ent_name.delete(0,END)
		aw_ent_email.delete(0,END)
		aw_ent_position.delete(0,END)
		aw_ent_salary.delete(0,END)
		aw_ent_id.focus()	
	except Exception as e:
		showerror("Issue",e)
	finally:	
		if con is not None:
			con.close()

#Delete employee records
def delete_emp():
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["emp_22june25"]
		coll=db["employee"]

		id=dw_ent_id.get()
		if not id:
			showwarning("Warning","ID should not be Empty")
			dw_ent_id.delete(0, END)
			dw_ent_id.focus()
			return

		if not id.isdigit():
			showwarning("Invalid ID","Employee ID must be an Integer")
			dw_ent_id.delete(0, END)
			dw_ent_id.focus()
			return
		
		id=int(id)
		result=coll.delete_one({"_id":id})
		if result.deleted_count==1:
			showinfo("Success",f"Employee with ID {id} is deleted Successfully")
			dw_ent_id.delete(0,END)
			dw_ent_id.focus()
		else:
			showwarning("Not Found",f"No Employee found with ID {id}")
			dw_ent_id.delete(0,END)
			dw_ent_id.focus()
			return			


	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

		
# Updte employee records
def update_emp():
	con=None
	try:
		con=MongoClient("localhost",27017)
		db=con["emp_22june25"]
		coll=db["employee"]

		id=uw_ent_id.get()
		if not id:
			showwarning("Warning","ID should not be Empty")
			uw_ent_id.delete(0, END)
			uw_ent_id.focus()
			return

		if not id.isdigit():
			showwarning("Invalid ID","Employee ID must be an Integer")
			uw_ent_id.delete(0, END)
			uw_ent_id.focus()
			return

		if not coll.find_one({"_id":int(id)}):
			showwarning("Not Found","No Employee with this ID")
			uw_ent_id.delete(0, END)
			uw_ent_id.focus()
			return

		name=uw_ent_name.get()
		if not name:
			showwarning("Warning","Name should not be Empty")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return

		email=uw_ent_email.get()
		if not email:
			showwarning("Warning","Email should not be Empty")
			uw_ent_email.delete(0, END)
			uw_ent_email.focus()
			return
				
		email_regex= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|in|org)$'
		if not re.match(email_regex,email):
			showwarning("Invalid Email","Please enter the valid email address")
			uw_ent_email.delete(0, END)
			uw_ent_email.focus()
			return
			
		position=uw_ent_position.get()
		if not position:
			showwarning("Warning","Position should not be Empty")
			uw_ent_position.delete(0, END)
			uw_ent_position.focus()
			return

		salary=uw_ent_salary.get()
		if not salary:
			showwarning("Warning","Salary should not be Empty")
			uw_ent_salary.delete(0, END)
			uw_ent_salary.focus()
			return

		salary_val=float(salary)
		if salary_val<=0:
			showwarning("Invalid Salary","Salary must be greateer than 0")
			uw_ent_salary.delete(0, END)
			uw_ent_salary.focus()
			return	

		#Updated records in mongoDB
		updated_data={
			"name": name,
			"email": email,
			"position": position,
			"salary": float(salary)
		}
		coll.update_one({"_id":int(id)}, {"$set":updated_data})	
		showinfo("Success",f"Employee with ID {id} is updated successfully")
		uw_ent_id.delete(0,END)
		uw_ent_name.delete(0,END)
		uw_ent_email.delete(0,END)
		uw_ent_position.delete(0,END)
		uw_ent_salary.delete(0,END)
		uw_ent_id.focus()

	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def go_chart():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["emp_22june25"]
        coll = db["employee"]

        data = list(coll.find({}, {"_id": 0, "name": 1, "salary": 1}))
        if not data:
            showwarning("No Data", "No employee records to show.")
            return

        # Convert to DataFrame
        df = pd.DataFrame(data)
        df["salary"] = df["salary"].astype(float)

        # Get top 5 salaries
        top5 = df.sort_values(by="salary", ascending=False).head(5)

        # Plot with full bar height comparison
        plt.figure(figsize=(10,6))
        bars = plt.bar(top5["name"], top5["salary"], color=["red", "blue", "green", "purple", "orange"])
        plt.title("Top 5 Highest Salaried Employees", fontsize=16)
        plt.xlabel("Employee Name")
        plt.ylabel("Salary (₹)", fontsize=12)
        plt.xticks(rotation=15)

        # Show value on top of bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:,.0f}', va='bottom', ha='center', fontsize=12)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        showerror("Issue", str(e))
    finally:
        if con is not None:
            con.close()





#main window
lab_title=Label(mw,text="Employee Managment system",font=("Arila",25,"bold","italic"),bg="black",fg="beige")
lab_title.pack(fill=X)
btn_add=Button(mw,text="Add Emp",font=("Arila",20,"bold"),bg="black",fg="beige",width=10,command=go_add)
btn_add.pack(pady=20)
btn_view =Button(mw,text="View  Emp",font=("Arila",20,"bold"),bg="black",fg="beige",width=10,command=go_view)
btn_view .pack(pady=20)
btn_update=Button(mw,text="Update Emp",font=("Arila",20,"bold"),bg="black",fg="beige",width=10,command=go_update)
btn_update.pack(pady=20)
btn_delete=Button(mw,text="Delete Emp",font=("Arila",20,"bold"),bg="black",fg="beige",width=10,command=go_delete)
btn_delete.pack(pady=20)
btn_chart=Button(mw,text="Charts",font=("Arila",20,"bold"),bg="black",fg="beige",width=10,command=go_chart)
btn_chart.pack(pady=20)

#Add window
aw=Toplevel(mw)
aw.geometry("800x720+300+50")
aw.title("Employee Management system")
aw .configure(bg="beige")
aw.iconbitmap("employee.ico")

aw_lab_title=Label(aw,text="Add Employee Information",font=("Arila",25,"bold","italic"),bg="black",fg="beige")
aw_lab_title.pack(fill=X)

aw_lab_id=Label(aw,text="Enter Id",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
aw_lab_id.place(x=30,y=70)

aw_ent_id=Entry(aw,font=("Arila",25,"bold"))
aw_ent_id.place(x=300,y=70)

aw_lab_name=Label(aw,text="Enter name",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
aw_lab_name.place(x=30,y=170)

aw_ent_name=Entry(aw,font=("Arila",25,"bold"))
aw_ent_name.place(x=300,y=170)

aw_lab_email=Label(aw,text="Enter Email",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
aw_lab_email.place(x=30,y=270)

aw_ent_email=Entry(aw,font=("Arila",25,"bold"))
aw_ent_email.place(x=300,y=270)

aw_lab_position=Label(aw,text="Enter position",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
aw_lab_position.place(x=30,y=370)

aw_ent_position=Entry(aw,font=("Arila",25,"bold"))
aw_ent_position.place(x=300,y=370)

aw_lab_salary=Label(aw,text="Enter salary",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
aw_lab_salary.place(x=30,y=470)

aw_ent_salary=Entry(aw,font=("Arila",25,"bold"))
aw_ent_salary.place(x=300,y=470)

aw_btn_back=Button(aw,text="Back",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=add_back)
aw_btn_back.place(x=190,y=600)
aw_btn_save=Button(aw,text="Save",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=save_emp)
aw_btn_save.place(x=480,y=600)

aw.withdraw()

#View Window

vw=Toplevel(mw)
vw.geometry("800x720+300+50")
vw.title("Employee Management system")
vw .configure(bg="beige")
vw.iconbitmap("employee.ico")

vw_lab_title=Label(vw,text="View Employee Information",font=("Arila",25,"bold","italic"),bg="black",fg="beige")
vw_lab_title.pack(fill=X)

vw_st_view=ScrolledText(vw,font=("Arila",25,"bold","italic"),width=40,height=12)
vw_st_view.pack(pady=20)
vw_btn_back=Button(vw,text="Back",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=view_back)
vw_btn_back.pack(pady=20)

vw.withdraw()

#Update window

uw=Toplevel(mw)
uw.geometry("800x720+300+50")
uw.title("Employee Management system")
uw .configure(bg="beige")
uw.iconbitmap("employee.ico")

uw_lab_title=Label(uw,text="Update Employee Information",font=("Arila",25,"bold","italic"),bg="black",fg="beige")
uw_lab_title.pack(fill=X)

uw_lab_id=Label(uw,text="Enter Id",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
uw_lab_id.place(x=30,y=70)

uw_ent_id=Entry(uw,font=("Arila",25,"bold"))
uw_ent_id.place(x=300,y=70)

uw_lab_name=Label(uw,text="Enter name",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
uw_lab_name.place(x=30,y=170)

uw_ent_name=Entry(uw,font=("Arila",25,"bold"))
uw_ent_name.place(x=300,y=170)

uw_lab_email=Label(uw,text="Enter Email",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
uw_lab_email.place(x=30,y=270)

uw_ent_email=Entry(uw,font=("Arila",25,"bold"))
uw_ent_email.place(x=300,y=270)

uw_lab_position=Label(uw,text="Enter position",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
uw_lab_position.place(x=30,y=370)

uw_ent_position=Entry(uw,font=("Arila",25,"bold"))
uw_ent_position.place(x=300,y=370)

uw_lab_salary=Label(uw,text="Enter salary",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
uw_lab_salary.place(x=30,y=470)

uw_ent_salary=Entry(uw,font=("Arila",25,"bold"))
uw_ent_salary.place(x=300,y=470)

uw_btn_back=Button(uw,text="Back",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=update_back)
uw_btn_back.place(x=190,y=600)
uw_btn_update=Button(uw,text="Update",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=update_emp)
uw_btn_update.place(x=480,y=600)

uw.withdraw()

#Delete Window
dw=Toplevel(mw)
dw.geometry("800x720+300+50")
dw.title("Employee Management system")
dw .configure(bg="beige")
dw.iconbitmap("employee.ico")

dw_lab_title=Label(dw,text="Delete Employee Information",font=("Arila",25,"bold","italic"),bg="black",fg="beige")
dw_lab_title.pack(fill=X)

dw_lab_id=Label(dw,text="Enter Id",font=("Arila",25,"bold","italic"),bg="beige",fg="black")
dw_lab_id.place(x=60,y=100)

dw_ent_id=Entry(dw,font=("Arila",25,"bold"))
dw_ent_id.place(x=300,y=100)

dw_btn_back=Button(dw,text="Back",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=delete_back)
dw_btn_back.place(x=190,y=200)
dw_btn_delete=Button(dw,text="Delete",font=("Arila",25,"bold","italic"),bg="black",fg="beige",width=8,command=delete_emp)
dw_btn_delete.place(x=480,y=200)

dw.withdraw()







def on_closing():
	if askyesno("close","Close window"):
		mw.destroy()
aw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)





mw.mainloop()