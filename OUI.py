from tkinter import *
import tkinter as tk
import tkinter.messagebox
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
global call
call=1
global take
take = 0
class oui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (f1, f2):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("f1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class f1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        header = Label(self, text='---OUI---', fg="white", bg="black", font=("Times New Roman", 40), relief=RAISED, height=5, width=10).pack(side="top", fill=X, pady=10)
        button1 = tk.Button(self, text="Next",command=lambda: controller.show_frame("f2")).pack(side="right")
        exitbutton = Button(self, text='Exit', command=quit).pack(side="left")

class f2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        userl = tk.Label(self, text='Username :').grid(row=1, column=0, padx=5, pady=5, sticky=W)
        passwordl = tk.Label(self, text='Password :').grid(row=2, column=0, padx=5, pady=5, sticky=W)
        tol = tk.Label(self, text='To :').grid(row=3, column=0, padx = 5, pady = 5, sticky = W)
        subl = tk.Label(self, text='Subject :').grid(row=4, column=0, padx = 5, pady = 5, sticky = W)
        msg = tk.Label(self, text='Message :').grid(row=5, column=0, padx=5, pady=5, sticky=W)


        global fbtext
        fbtext = StringVar()
        fbtext.set('farxmed@gmail.com')
        usere = tk.Entry(self, textvariable=fbtext, width=30, insertofftime=0).grid(row=1, column=1, padx=5, pady=5, sticky=W)

        global cbtext
        cbtext = StringVar()
        cbtext.set('0f69c9112us5_o13lY')
        passworde = tk.Entry(self, textvariable=cbtext, show='*', width=30, insertofftime=0).grid(row=2, column=1, padx=5, pady=5, sticky=W)

        global kbtext
        kbtext = StringVar()
        kbtext.set('fareed2000ahmed@gmail.com')
        toe = tk.Entry(self, textvariable=kbtext, width=30, insertofftime=0).grid(row=3, column=1, padx=5, pady=5, sticky=W)

        global sub
        sub = StringVar()
        sub.set('')
        subbox = tk.Entry(self, textvariable=sub, width = 50, insertofftime=0).grid(row=4, column=1, padx=5, pady=5, sticky=W)

        global message
        message = tk.Text(self, wrap=WORD, width=60, height=10, state=NORMAL, relief=RAISED, insertofftime=0)
        message.grid(row=5, column=1, padx=5, pady=5)

        add_button = tk.Button(self, text='Add attachments', bg='blue', command=lambda: self.add()).grid(row=6,column=1,padx=5,pady=5, sticky=N + S + E + W)

        sendbutton = tk.Button(self, text='Send', command=lambda: email()).grid(row=10, column=0, padx=5, pady=5, sticky=N + S + E + W)

        exitbutton = tk.Button(self, text='Exit', command=quit).grid(row=10, column=2, padx=5, pady=5, sticky=N + S + E + W)

    def add(self):
            global call
            call = 2
            global file_name
            file_name = tk.Label(self, text='File name : ').grid(row=8, column=0, padx=5, pady=5, sticky=W)
            file_address = tk.Label(self, text='File Address :').grid(row=7, column=0, padx=5, pady=5, sticky=W)

            global filetext
            filetext = StringVar()
            filetext.set('')
            address = tk.Entry(self, textvariable=filetext, width=80, insertofftime=0).grid(row=7, column=1, padx=5, pady=5, sticky=W)
            global filltext
            filltext = StringVar()
            filltext.set('')
            filename = tk.Entry(self, textvariable=filltext, width=80, insertofftime=0).grid(row=8, column=1, padx=5, pady=5, sticky=W)
            okbut = tk.Button(self, text='Show filename', command=lambda: get_file_name()).grid(row=7,column=2,padx=5, pady=5, sticky=N + S + E + W)

            def get_file_name():
                global fadd
                fadd = filetext.get()
                global fnam
                fnam=''

                def reverse(str):
                    string = "".join(reversed(str))
                    return string
                for i in reverse(fadd):
                    if i != "\\" and i !="/":
                        fnam += i
                    else:
                        break
                fnam = reverse(fnam)
                filltext.set(fnam)
def email():
            id = fbtext.get()
            id = id.strip()
            secret = cbtext.get()
            receiver = kbtext.get()
            subject = sub.get()
            data = message.get('1.0', 'end-1c')
            count = 0
            ref = ''
            mails = receiver.split(', ')
            for i in range(len(id)):
                if (id[i] == '@'):
                    count = 1
                    for j in range(i + 1, len(id) - 4):
                        ref += id[j]
            print(ref)

            error = 0
            if id == '@gmail.com' or id == '@yahoo.com' or id == '@outlook.com' or id == '' or id[len(id) - 1] != 'm' or id[len(id) - 2] != 'o' or id[len(id) - 3] != 'c' or id[len(id) - 4] != '.':
                tkinter.messagebox.showwarning("Warning", "Enter valid email")
                error = 1
            elif secret == '':
                tkinter.messagebox.showwarning("Warning", "Oops! Enter the password!")
                error = 1
            elif receiver == '':
                tkinter.messagebox.showerror("Error", "Please specify at least one recipient")
                error = 1

            msg = MIMEMultipart()

            msg['From'] = id
            msg['To'] = receiver
            msg['Subject'] = subject

            msg.attach(MIMEText(data, 'plain'))
            if call == 2:
              if fadd != '':
                try:
                    attachment = open(fadd, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % fnam)
                    msg.attach(part)
                except:
                    error=1
                    tkinter.messagebox.showerror("Error", "Cannot attach file")

            if error == 0:
                try:
                    if ref == 'gmail':
                        mail = smtplib.SMTP('smtp.gmail.com', 587)
                    elif ref == 'yahoo':
                        mail = smtplib.SMTP('smtp.mail.yahoo.com', 587)
                    elif ref == 'outlook':
                        mail = smtplib.SMTP('smtp.mail.outlook.com', 587)
                    else:
                        tkinter.messagebox.showwarning("Warning", "Enter valid email")
                except:
                    tkinter.messagebox.showerror("Error", "Unable to connect to the server! Please check your internet connection.")
                mail.ehlo()
                mail.starttls()
                try:
                   mail.login(id, secret)
                except:
                   tkinter.messagebox.showerror("Error", "Unable to login, Check email/password")
                   count = 2
                secret = ''
                if count != 2:
                    try:
                        text = msg.as_string()
                        mail.sendmail(id, mails, text)
                        mail.close()
                        tkinter.messagebox.showinfo("Notification", "Mail Sent")
                    except:
                        tkinter.messagebox.showerror("Error", "Unable to send email")


def check_internet():
    url = 'http://www.google.com/'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


def update():
    if check_internet():
        now = "ONLINE"
        label.configure(text=now, fg='green')
    else:
        now = "OFFLINE"
        label.configure(text=now, fg='red')
    app.after(1000, update)


if __name__ == "__main__":
    app = oui()
    label = Label(app, text="", bd=1, relief=SUNKEN, anchor=W)
    label.pack(side=BOTTOM, fill=X)
    label.grid_rowconfigure(20)
    label.grid_columnconfigure(2)
    refresh = Button(app, text="Refresh", anchor=W, command=lambda : update())
    refresh.pack(side=BOTTOM)
    refresh.grid_rowconfigure(20)
    refresh.grid_columnconfigure(2)
    update()
    app.mainloop()
