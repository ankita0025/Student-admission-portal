from tkinter import *
import time
from tkinter import messagebox,Toplevel,ttk,filedialog
from tkinter.ttk import Treeview
import pymysql
import pandas


#---------------------------functionality of data entery buttons-----------------
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        phone = phoneval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,phone,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name), parent = addroot)
            if(res==True): #here if we are choosing the  yes option, that means we want the clear form next time..so we need all the values set null for that
                idval.set('')
                nameval.set('')
                phoneval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.title("Student Admission portal")
    addroot.grab_set() #this method will disable all functionality of gui while this popup is open
    addroot.geometry("300x360+220+200")
    addroot.iconbitmap('logo.ico')   #for adding icon,we need .ico images for this function.
    addroot.resizable(False,False)
    addroot.config(bg = "white")
    #---------------------------add student labels--------------
    registration_no = Label(addroot, text= "REGISTRATION NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    registration_no.place(x= 10, y =10)

    name = Label(addroot, text= "NAME",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    name.place(x= 10, y =45)

    phone = Label(addroot, text= "CONTACT NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    phone.place(x= 10, y =80)

    email = Label(addroot, text= "EMAIL ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    email.place(x= 10, y =115)

    address = Label(addroot, text= "ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    address.place(x= 10, y =150)

    gender = Label(addroot, text= "GENDER",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    gender.place(x= 10, y =185)

    dob = Label(addroot, text= "DATE OF BIRTH",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    dob.place(x= 10, y =220)
    #---------------------------------add student entries----------------
    idval = StringVar()
    nameval = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    registration_no = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5, textvariable =idval)
    registration_no.place(x= 150, y =10)
    name = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =nameval)
    name.place(x= 150, y =45)
    phone = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =phoneval)
    phone.place(x= 150, y =80)
    email = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =emailval)
    email.place(x= 150, y =115)
    address = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =addressval)
    address.place(x= 150, y =150)
    gender = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =genderval)
    gender.place(x= 150, y =185)
    dob = Entry(addroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =dobval)
    dob.place(x= 150, y =220)
    #submit button
    submitadd_button = Button(addroot, text="SUBMIT",relief= RAISED,font = ("Comic Sans MS", "10"),bg="yellow",
                            activebackground= "blue",command = submitadd)
    submitadd_button.place(x= 115, y= 300)
    addroot.mainloop()
def searchstudent():
    def submitsearch():
        id = idval.get()
        name = nameval.get()
        phone = phoneval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(name != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(phone != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where phone=%s'
            mycursor.execute(strr,(phone)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(email != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(address != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(dob != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(gender != ''): #if id feild is not empty:
            strr = 'select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender)) #in this the id will go in place of above statement
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children()) #first we will clear all data in the frame
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.title("Student Admission portal")
    searchroot.grab_set() #this method will disable all functionality of gui while this popup is open
    searchroot.geometry("300x360+220+200")
    searchroot.iconbitmap('logo.ico')   #for adding icon,we need .ico images for this function.
    searchroot.resizable(False,False)
    searchroot.config(bg = "white")
    #---------------------------search student labels--------------
    registration_no = Label(searchroot, text= "REGISTRATION NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    registration_no.place(x= 10, y =10)

    name = Label(searchroot, text= "NAME",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    name.place(x= 10, y =45)

    phone = Label(searchroot, text= "CONTACT NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    phone.place(x= 10, y =80)

    email = Label(searchroot, text= "EMAIL ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    email.place(x= 10, y =115)

    address = Label(searchroot, text= "ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    address.place(x= 10, y =150)

    gender = Label(searchroot, text= "GENDER",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    gender.place(x= 10, y =185)

    dob = Label(searchroot, text= "DATE OF BIRTH",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    dob.place(x= 10, y =220)

    date = Label(searchroot, text= "SEARCH BY DATE",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    date.place(x= 10, y =255)
    #---------------------------------search student entries----------------
    idval = StringVar()
    nameval = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    registration_no = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5, textvariable =idval)
    registration_no.place(x= 150, y =10)
    name = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =nameval)
    name.place(x= 150, y =45)
    phone = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =phoneval)
    phone.place(x= 150, y =80)
    email = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =emailval)
    email.place(x= 150, y =115)
    address = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =addressval)
    address.place(x= 150, y =150)
    gender = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =genderval)
    gender.place(x= 150, y =185)
    dob = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =dobval)
    dob.place(x= 150, y =220)
    date = Entry(searchroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =dateval)
    date.place(x= 150, y =255)
    #submit button
    submitsearch_button = Button(searchroot, text="SUBMIT",relief= RAISED,font = ("Comic Sans MS", "10"),bg="yellow",
                            activebackground= "blue", command = submitsearch)
    submitsearch_button.place(x= 115, y= 300)
    searchroot.mainloop()
def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def updatestudent():
    def submitupdate():
        id = idval.get()
        name = nameval.get()
        phone = phoneval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()


        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s where id=%s'
        mycursor.execute(strr,(name, phone,email,address,gender,dob,date,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.title("Student Admission Portal")
    updateroot.grab_set() #this method will disable all functionality of gui while this popup is open
    updateroot.geometry("300x360+220+200")
    updateroot.iconbitmap('logo.ico')   #for adding icon,we need .ico images for this function.
    updateroot.resizable(False,False)
    updateroot.config(bg = "white")
    #---------------------------search student labels--------------
    registration_no = Label(updateroot, text= "REGISTRATION NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    registration_no.place(x= 10, y =10)

    name = Label(updateroot, text= "NAME",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    name.place(x= 10, y =45)

    phone = Label(updateroot, text= "CONTACT NO.",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    phone.place(x= 10, y =80)

    email = Label(updateroot, text= "EMAIL ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    email.place(x= 10, y =115)

    address = Label(updateroot, text= "ADDRESS",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    address.place(x= 10, y =150)

    gender = Label(updateroot, text= "GENDER",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    gender.place(x= 10, y =185)

    dob = Label(updateroot, text= "DATE OF BIRTH",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    dob.place(x= 10, y =220)

    date = Label(updateroot, text= "DATE",bg ="#B5EAD7" ,font=("Comic Sans MS", "8") , relief= RAISED,height= 1)
    date.place(x= 10, y =255)



    #---------------------------------search student entries----------------
    idval = StringVar()
    nameval = StringVar()
    phoneval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()



    registration_no = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5, textvariable =idval)
    registration_no.place(x= 150, y =10)
    name = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =nameval)
    name.place(x= 150, y =45)
    phone = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =phoneval)
    phone.place(x= 150, y =80)
    email = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =emailval)
    email.place(x= 150, y =115)
    address = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =addressval)
    address.place(x= 150, y =150)
    gender = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =genderval)
    gender.place(x= 150, y =185)
    dob = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =dobval)
    dob.place(x= 150, y =220)
    date = Entry(updateroot,font=("Comic Sans MS", "8") ,bd=5,textvariable =dateval)
    date.place(x= 150, y =255)

    #submit button
    updatesubmit_button = Button(updateroot, text="SUBMIT",relief= RAISED,font = ("Comic Sans MS", "10"),bg="yellow",
                                 activebackground= "blue", command = submitupdate)
    updatesubmit_button.place(x= 115, y= 300)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        phoneval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
    updateroot.mainloop()
def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,phone,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),phone.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,phone,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

def quit():
    ask = messagebox.askokcancel("confirm", "DO YOU WANT TO EXIT?")
    if (ask == True):
        root.destroy()





#-----------------------connection of database-------------------
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),contact varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr ="alter table studentdata1 modify column id int not null"
            mycursor.execute(strr)
            strr = "alter table studentdata1 modify column id int primary key"
            mycursor.execute(strr)
            strr ="alter table studentdata1 modify column id int not null"
            mycursor.execute(strr)
            strr = "alter table studentdata1 modify column id int primary key"
            mycursor.execute(strr)
            messagebox.showinfo('Notification','DATABASE CREATED',parent=dbroot)


        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)

            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel() #toplevel function is used to display a pop up widget in tkinter
    dbroot.title("Student admission portal")
    dbroot.grab_set() #this method will disable all functionality of gui while this popup is open
    dbroot.geometry("480x240")
    dbroot.iconbitmap('logo.ico')   #for adding icon,we need .ico images for this function.
    dbroot.resizable(False,False)
    dbroot.config(bg = "#CAA7BD")
    #--------------------lables-------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostLabel = Label(dbroot, text= "Enter Host:",bg ="#FFB9C4" ,font=("MS Serif", "18") , relief= RAISED,height= 1, width= 13, borderwidth= 3)
    hostLabel.place(x= 10, y =10)

    userLabel = Label(dbroot, text= "Enter User:",font=("MS Serif", "18") , relief= RAISED,bg="#FFB9C4",height= 1, width= 13, borderwidth= 3)
    userLabel.place(x=10 , y = 55)

    passwordLAbel = Label(dbroot, text= "Enter Password:",font=("MS Serif", "18") , relief= RAISED,bg="#FFB9C4",height= 1, width= 13, borderwidth= 3)
    passwordLAbel.place(x= 10, y = 100)

    #--------------------connectdb entries--------------
    hostentry = Entry(dbroot,font=("MS Serif", "18") ,bd=5, textvariable = hostval)
    hostentry.place(x= 250, y =10)

    userentry = Entry(dbroot,font=("MS Serif", "18"),bd=5, textvariable =userval )
    userentry.place(x= 250, y =55)

    passwordentry = Entry(dbroot,bd=5,font=("MS Serif", "18"), textvariable = passwordval)
    passwordentry.place(x= 250, y =100)

    #submit button
    connect_button = Button(dbroot, text="SUBMIT",relief= RAISED,font = ("Comic Sans MS", "20"),bg="#E0FEFE",
                            activebackground= "#B5EAD7", command = submitdb)
    connect_button.place(x= 170, y= 155)



    dbroot.mainloop()


#----------------------clock function---------------
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%y")
    clock.config(text = date_string +"\n"+ time_string)
    clock.after(1000,tick)
#-------------------------label moving function------------------
def IntroLabel():
    global count, text
    if(count>= len(ss)):
        count = 0
        text= ''
        sliderLabel.config(text=text)
    else:
        text = text+ss[count]
        sliderLabel.config(text=text)
        count += 1
    sliderLabel.after(200,IntroLabel)
#-----------------------------------------------intro------------

root = Tk()
root.title("Student Management System")
root.config(bg ="#FED8B2")
root.geometry('640x480+20+50')
root.iconbitmap('logo.ico')   #for adding icon,we need .ico images for this function.
root.resizable(False,False)   #this will remove the default option of resizing the window
#---------------------------------------frame---------------

#------frame1-------------------------------------------------------
DataEntryFrame = Frame(root, bg = "white", relief = RAISED, borderwidth= 3, cursor = "plus")
DataEntryFrame.place(x=10, y=80, width= 300, height = 390)

welcomeLabel= Label(DataEntryFrame, text= "WELCOME",font=("MS Serif", "18") )
welcomeLabel.place(x= 90, y = 5)

#_______________________buttons for data entry_____________
Add_button = Button(root, text="ADD STUDENT",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                        activebackground= "#B5EAD7", command = addstudent )
Add_button.place(x= 15, y= 125)

Search_button = Button(root, text="SEARCH STUDENT",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                    activebackground= "#B5EAD7", command = searchstudent)
Search_button.place(x= 15, y= 160)

Delete_button = Button(root, text="DELETE STUDENT RECORD",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                    activebackground= "#B5EAD7", command = deletestudent)
Delete_button.place(x= 15, y= 195)

Update_button = Button(root, text="UPDATE STUDENT RECORD",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                    activebackground= "#B5EAD7", command = updatestudent)
Update_button.place(x= 15, y= 230)

ShowRecord_button = Button(root, text="SHOW RECORDS",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                    activebackground= "#B5EAD7" , command = showstudent)
ShowRecord_button.place(x= 15, y= 265)

Export_button = Button(root, text="EXPORT RECORDS",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                           activebackground= "#B5EAD7", command = exportstudent)
Export_button.place(x= 15, y= 300)

Quit_button = Button(root, text="QUIT",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                           activebackground= "#B5EAD7", command = quit)
Quit_button.place(x= 15, y= 335)

#------frame2-------------------------------------------------
showDataFrame = Frame(root, bg = "white", relief = RAISED, borderwidth= 3)
showDataFrame.place(x=320, y=80, width= 300, height = 390)

style = ttk.Style()
style.configure("Treeview.Heading",  foreground= "blue")
style.configure("Treeview",  background = "#B5EAD7")

scroll_x = Scrollbar(showDataFrame, orient = HORIZONTAL)
scroll_y = Scrollbar(showDataFrame, orient = VERTICAL)

studenttable = Treeview(showDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
#------------in above statement, we made 9 columns and set the scrolls command in x and y direction
scroll_x.pack(side= BOTTOM, fill = X)
scroll_y.pack(side = RIGHT , fill = Y)
#-------------------------in above statements , we are packing the xscrolls in bottom and right and we are making them fill in whole axis
scroll_x.config(command = studenttable.xview)
scroll_y.config(command = studenttable.yview)
#--------------here we are connecting the scrolls to the student table so that when we make scrolls move, whole view move in desired direction
#here we are naming the columns we made above
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)

#-------------------------------------slider-----------------
ss= "WELCOME TO STUDENT ADMISSION PORTAL"
count= 0
text = ''

sliderLabel = Label(root, text= ss,font=("MS Serif", "18") , relief= RAISED,bg="#FF9AA2",height= 1, width= 40, borderwidth= 5)
sliderLabel.place(x= 90, y = 5)

IntroLabel()
#--------------------------------------clock
clock = Label(root,font=("Comic Sans MS", "10") , relief= RAISED,bg="#FFFFD8",height= 2, borderwidth= 3)
clock.place(x=0, y=0)
tick()
#------------------------------------connect to button-------
connect_button = Button(root, text="Connect To Database",relief= RAISED,font = ("Comic Sans MS", "8"),bg="#E0FEFE",
                        activebackground= "#B5EAD7", command = Connectdb)
connect_button.place(x= 0, y= 50)



root.mainloop()
