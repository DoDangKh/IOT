import pyrebase
import  tkinter as tk
#import tkinter as tk
import PyPDF2
import PIL
import matplotlib.pyplot as pyplot
import random
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
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

# def millitime()
#    return round(time.time()*1000)

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

    # t = tk.Text(root, height=1, width=20, font=("Arial", 30))
    # t.grid(column=1, row=1)

    # label2 = tk.Label(root, text="Cường Độ Gửi Đến FireBase:", font=("Arial", 30))
    # label2.grid(column=0, row=1)

    b=tk.Button(root,text="Cập Nhật Dữ Liệu",command=lambda: senddata(t.get("1.0","end-1c")),font=("Arial",30))

    b.grid(column=0,row=2,columnspan=2)
    y=0
    x_values = []
    y_values = []
    figure = pyplot.figure()
    def update():


        x = random.randint(0, 10);
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-3]
        x_values.append(x)
        y_values.append(current_time)
        global  y
        y += 1
        print(y)

        figure.add_subplot().plot(y_values, x_values)
        chart = FigureCanvasTkAgg(figure, root)
        chart.get_tk_widget().grid(row=1, column=0)
        pyplot.grid()
        pyplot.xlim(y-5,y)
        pyplot.ylim(0,10)
        print(retrivedata().val())
        label.config(text="Cường Độ Âm Thanh Đang Là:" + str(retrivedata().val()))
        root.after(500, update)
    # y=0
    # x_values = [0]
    # y_values = [0]
    # x=0
    # figure=pyplot.figure()

    # while(y<100):
    #     x=random.randint(0 , 10)
    #     x_values.append(x)
    #     y_values.append(y)
    #     y+=1
    #     figure.add_subplot().plot(y_values,x_values)
    #     pyplot.xlim(y-10,y)
    #
    #     pyplot.pause(0.01)
    #
    # pyplot.show()



    update()




    root.mainloop()



