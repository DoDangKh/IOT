import pyrebase
import  tkinter as tk
#import tkinter as tk
import PyPDF2
import PIL
import matplotlib.pyplot as plt
import random
import numpy as np
from datetime import datetime
from itertools import count

from matplotlib import animation
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

import MachineLearning
import sendemail
from xls import writedata

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

def retrivedata(str):

    # DOC DU LIEU TU CLOUD
    data = db.child(str).get()
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
    frame1= tk.Frame(root)
    frame1.grid(column=0,row=0)
    frame2=tk.Frame(root)
    frame2.grid(column=0,row=1)
    frame3=tk.Frame(root)
    frame3.grid(column=0,row=2)
    label = tk.Label(frame1, text="Cường Độ Âm Thanh Đang Là:" + str(retrivedata("SOUND").val()), font=("Arial", 30))
    label.grid(column=0, row=0)
    label2 = tk.Label(frame1, text="Cường Độ Bui Đang Là:" + str(retrivedata("DUST").val()), font=("Arial", 30))
    label2.grid(column=1, row=0)
    b=tk.Button(frame3,text="Gui Mail", command=lambda: sendemail.sendmail(retrivedata('DUST').val(), retrivedata('SOUND').val()))
    # t = tk.Text(root, height=1, width=20, font=("Arial", 30))
    # t.grid(column=1, row=1)

    # label2 = tk.Label(root, text="Cường Độ Gửi Đến FireBase:", font=("Arial", 30))
    # label2.grid(column=0, row=1)

    # b=tk.Button(root,text="Cập Nhật Dữ Liệu",command=lambda: senddata(t.get("1.0","end-1c")),font=("Arial",30))

    # b.grid(column=0,row=2,columnspan=2)
    b.grid(column=0,row=0)
    b2=tk.Button(frame3,text='Xuat File Du Doan Ket Xe',command=lambda: MachineLearning.create_report_file())
    b2.grid(column=1,row=0)
    b3=tk.Button(frame3,text='Gui Mail Du Doan', command=lambda: MachineLearning.send_mail() )
    b3.grid(column=2,row=0)
    b4=tk.Button(frame3,text='train ai',command=lambda :MachineLearning.train())
    b4.grid(column=4,row=0)
    y=0
    x_values = []
    x2_values=[]
    y_values = []
    index=count()
    figure = plt.figure()
    def update():
        figure.clear()
        x = retrivedata("SOUND").val();
        x2=retrivedata("DUST").val();
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S.%f")[:-3]
        x_values.append(x)
        x2_values.append(x2)
        y_values.append(next(index))
        global  y
        y += 1
        print(y)
        writedata(retrivedata("SOUND").val(),retrivedata("DUST").val())
        figure.add_subplot(121).plot(y_values, x_values)
        plt.grid()
        plt.xlim(y - 5, y)
        plt.ylim(x-5,x+5)
        figure.add_subplot(122).plot(y_values, x2_values)
        plt.grid()
        plt.xlim(y - 5, y)
        plt.ylim(x2-5,x2+5)
        chart = FigureCanvasTkAgg(figure, frame2)
        chart.get_tk_widget().grid(row=1, column=0)

        print(retrivedata('SOUND').val())
        label.config(text="Cường Độ Âm Thanh Đang Là:" + str(retrivedata("SOUND").val()))
        label2.config(text="Cường Độ Bui Đang Là:" + str(retrivedata("DUST").val()))
        frame2.after(500, update)
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


