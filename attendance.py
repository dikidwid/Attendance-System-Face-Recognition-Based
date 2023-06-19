##################################### ATTENDANCE MANAGEMENT SYSTEM ##################################

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import datetime
import time

##################################### Project Module ################################################

import show_attendance
import takeImage
import trainImage
import automaticAttendance


##################################### Text to Speech ################################################

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


########################################## Time ##########################################

def tick():
    time_string = time.strftime(' Time:%H:%M:%S ')
    clock.config(text=time_string)
    clock.after(300, tick)


########################################## Path ##########################################

haarcasecade_path = "D:\\College\\Python\\Attendance-Management-system-using-face-recognition-master\\Attendance-Management-system-using-face-recognition-master\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "D:\\College\\Python\\Attendance-Management-system-using-face-recognition-master\\Attendance-Management-system-using-face-recognition-master\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "D:\\College\\Python\\Attendance-Management-system-using-face-recognition-master\\Attendance-Management-system-using-face-recognition-master\\TrainingImage"
studentdetail_path = (
    "D:\\College\\Python\\Attendance-Management-system-using-face-recognition-master\\Attendance-Management-system-using-face-recognition-master\\StudentDetails\\studentdetails.csv"
)
attendance_path = "D:\\College\\Python\\Attendance-Management-system-using-face-recognition-master\\Attendance-Management-system-using-face-recognition-master\\Attendance"

################################################## Window Conf ###########################

window = Tk()
window.title("Attend System")
window.geometry("1280x720")
dialog_title = "QUIT"
window.configure(background="white")

########################################## Date ##########################################

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('Date: %d-%m-%Y ')
day, month, year = date.split("-")

mont = {

    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}

######################################### Error Message ############################################

# to destroy screen
def del_sc1():
    sc1.destroy()

# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="white")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="black",
        bg="white",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="black",
        bg="white",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True

####################################### FRONT END ##################################################

a = tk.Label(
    window,
    text="Welcome to the Face Recognition Based\nAttendance Management System",
    bg="white",
    fg="blue",
    bd=10,
    font=("Tahoma", 35, 'bold'),
)
a.pack()

regImg = Image.open("UI_Image/register.png")
regImg = regImg.resize((230, 230), Image.Resampling.LANCZOS)
regImg1 = ImageTk.PhotoImage(regImg)
label1 = Label(window, image=regImg1)
label1.image = regImg1
label1.place(x=188, y=270)

attImg = Image.open("UI_Image/attendance.png")
attImg = attImg.resize((230, 230), Image.Resampling.LANCZOS)
attImg1 = ImageTk.PhotoImage(attImg)
label2 = Label(window, image=attImg1)
label2.image = attImg1
label2.place(x=1000, y=270)

verImg = Image.open("UI_Image/verifyy.png")
verImg = verImg.resize((230, 230), Image.Resampling.LANCZOS)
verImg1 = ImageTk.PhotoImage(verImg)
label3 = Label(window, image=verImg1)
label3.image = verImg1
label3.place(x=600, y=270)

frame3 = tk.Frame(window, bg="white")
frame3.place(relx=0.52,
             rely=0.19,
             relwidth=0.09,
             relheight=0.07)

clock = tk.Label(frame3,
                 fg="#3d4141",
                 bg="white",
                 width=120,
                 height=1,
                 font=('candara', 14, ' bold '))
clock.pack(fill='both', expand=1)
tick()

frame4 = tk.Frame(window, bg="#E6EFF6")
frame4.place(relx=0.36,
             rely=0.19,
             relwidth=0.16,
             relheight=0.07)

datef = tk.Label(frame4,
                 text=day + "-" + mont[month] + "-" + year + "   | ",
                 fg="#3d4141",
                 bg="white",
                 width=60,
                 height=1,
                 font=('candara', 15, ' bold '))

datef.pack(fill='both', expand=1)


###################################### Take Image ###############################################

def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="white")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI,
                    bg="white",
                    relief=RIDGE,
                    bd=10,
                    font=("arial", 35))
    titl.pack(fill=X)

    # image and title
    titl = tk.Label(ImageUI,
                    text="Register Your Face",
                    bg="white",
                    fg="blue",
                    font=("arial", 30, 'bold'),
    )
    titl.place(x=200, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="white",
        fg="black",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

######################################### Train Image #############################################

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


########################################### Register Face ##############################################

r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=188, y=520)


############################################ Take Attendance ###########################################

def automatic_attendance():
    automaticAttendance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=600, y=520)


############################################## View Attendance #########################################

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=1000, y=520)

############################################ EXIT ####################################################
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=600, y=660)

############################################# WINDOW #################################################

window.attributes('-fullscreen', True)
window.mainloop()
