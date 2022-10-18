import pyrebase
import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

config = {
    "apiKey": "AIzaSyAYFuYoE2-8V6xxbm_ba0zwVfBCEv25KBQ",
    "authDomain": "arduino-1e690.firebaseapp.com",
    "databaseURL": "https://arduino-1e690-default-rtdb.firebaseio.com",
    "projectId": "arduino-1e690",
    "storageBucket": "arduino-1e690.appspot.com",
    "messagingSenderId": "815555517433",
    "appId": "1:815555517433:web:571b3378353cf1bf963b28",
    "measurementId": "G-S18583XP4C"
}


def retrivedata():

    # DOC DU LIEU TU CLOUD
    data = db.child("SOUND").get()
    # print(data.val())
    return data
    # GHI DU LIEU LEN CLOUD
    # db.update({"SOUND": 10})


def senddata(data):
    db.update({"SOUND": int(data)})


if __name__ == "__main__":
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    root = tk.Tk()
    canvas = tk.Canvas(root, width=600, height=600)
    canvas.grid(columnspan=3,rowspan=2)
    label = tk.Label(root, text="Cường Độ Âm Thanh Đang Là:" + str(retrivedata().val()), font=("Arial", 30))
    label.grid(column=0, row=0)

    t = tk.Text(root, height=1, width=20, font=("Arial", 30))
    t.grid(column=1, row=1)

    label2 = tk.Label(root, text="Cường Độ Gửi Đến FireBase:", font=("Arial", 30))
    label2.grid(column=0, row=1)

    b=tk.Button(root,text="Cập Nhật Dữ Liệu",command=lambda: senddata(t.get("1.0","end-1c")),font=("Arial",30))

    b.grid(column=0,row=2,columnspan=2)

    def update():
        print(retrivedata().val())
        label.config(text="Cường Độ Âm Thanh Đang Là:" + str(retrivedata().val()))
        root.after(1000, update)


    update()

    root.mainloop()
