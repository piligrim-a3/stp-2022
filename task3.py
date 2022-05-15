import qrcode
import requests
from tkinter import *
from PIL import Image, ImageTk

count = 0

def auth():
    login = username_verify.get()
    password = password_verify.get()

    print(login, password)

    response = session.post(
        'https://bgpu.ru/campus/api/v1/auth',
        data={'login': login, "pwd": password}
    )
    if response.ok:
        data = response.json()
        name = data.get('name') + '. ' + data.get('surname')
        login_sucess()
        update_main_after_login(name)
    else:
        password_not_recognised()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def getQR():
    response = session.get(
        'https://bgpu.ru/campus/api/v1/area/qr'
    )
    return response.json()


def login():
    global login_screen

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=auth).pack()


def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def update_main_after_login(name):
    for child in main_screen.winfo_children():
        child.destroy()
    main_screen.title(name)
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()

    Button(text="Get QR code", height="2", width="30", command=show_qr_code).pack()



def show_qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    global count
    count = (count + 1) % 30

    qr.add_data(getQR()[count])
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrCode.png")
    image = ImageTk.PhotoImage(file='qrCode.png')


    qr_window = Toplevel(main_screen)
    panel = Label(qr_window, image=image)
    panel.image = image
    panel.pack()


def main_account_screen():
    global main_screen
    global session
    session = requests.Session()
    main_screen = Tk()
    main_screen.geometry("300x250")
    Label(text="").pack()
    Label(text="").pack()
    main_screen.title("Account Login")
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()

    main_screen.mainloop()

if __name__ == '__main__':
    main_account_screen()

