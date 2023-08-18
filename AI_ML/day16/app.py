import tkinter as ttk
from tkinter import font
from attendance import attendance
from registration_face import register
from clear_data import clear_data

app=ttk.Tk()
app.geometry('400x400')
app.title('Attendance System')
font_=font.Font(size=10)
#main code is hear

ttk.Label(app,text='Face Recognition System',font=font_).pack()

def registration():
    app.destroy()
    with open('opr','w')as f:
        f.write('register')
    import login_admin
    

def attendance():
    print("Attendance")
    import attendance
    attendance.attendance()

def clear_data():
    app.destroy()
    with open('opr','w')as f:
        f.write('clear')
    import login_admin 

ttk.Button(app,text='Registration', command=registration, font=font_ , height=1,width=10,bg='#3498DB', fg='#E5E4E2' ).pack(expand=True)
ttk.Button(app,text='Attendance',command=attendance,font=font_ , height=1,width=10,bg='#3498DB', fg='#E5E4E2').pack(expand=True)
ttk.Button(app,text='Clear Data',command=clear_data,font=font_ , height=1,width=10,bg='#3498DB', fg='#E5E4E2').pack(expand=True)

# end the main code and run the main code
app.mainloop()