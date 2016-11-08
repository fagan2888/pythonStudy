from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


# application = Application()
# # 设置窗口标题
# application.master.title('Hello world')
# application.mainloop()


class InputApplication(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.quitButton = Button(self, text='Hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello %s' % name)

application = InputApplication()
# 设置窗口标题
application.master.title('Hello world')
application.mainloop()
