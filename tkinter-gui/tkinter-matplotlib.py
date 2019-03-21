from tkinter import *
import matplotlib
from matplotlib.figure import Figure
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='OK', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        func = self.nameInput.get()
        root = Tk()
        f = Figure(figsize=(5, 4), dpi=100)
        a = f.add_subplot(111)
        x = np.linspace(1, 10, 100)
        # 绘制图形
        a.plot(x, eval(func))
        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)



app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()
