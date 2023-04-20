from tkinter import *
from tkinter.colorchooser import askcolor

class WhiteBoard:
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.color = 'black'
        self.width = 2

        self.root = Tk()
        self.root.title("YuPaint")
        self.root.geometry("1280x720")
        self.root.configure(bg="#0d0f36")
        self.root.resizable(False,False)

        image_icon= PhotoImage(file="icon.png")
        self.root.iconphoto(False,image_icon)
        
        # canvas
        self.canvas = Canvas(self.root, width=1280, height=520, background="white", cursor="circle")
        self.canvas.pack(pady=10)
        self.canvas.bind('<Button-1>', self.locate_xy)
        self.canvas.bind('<B1-Motion>', self.add_line)
        
        # create frame for buttons
        button_frame = Frame(self.root, bg='#0d0f36')
        button_frame.pack(fill='x', padx=20, pady=10)

        # color picker
        self.color_button = Button(button_frame, text='Pilih Warna', command=self.pick_color)
        self.color_button.pack(pady=5)

        # width slider
        self.width_slider = Scale(button_frame, from_=1, to=100, orient=HORIZONTAL, command=self.change_width)
        self.width_slider.set(self.width)
        self.width_slider.pack(pady=5)

        # undo button
        self.undo_stack = []
        self.undo_button = Button(button_frame, text='Undo', command=self.undo)
        self.undo_button.pack(side=LEFT, padx=5)

        # clear button
        self.clear_button = Button(button_frame, text='Clear', command=self.clear_canvas)
        self.clear_button.pack(side=LEFT, padx=5)

        # center the button frame
        button_frame.update()
        width = button_frame.winfo_width()
        height = button_frame.winfo_height()
        x = (self.root.winfo_width() // 2) - (width // 20)
        y = self.root.winfo_height() - height - 70
        button_frame.place(x=x, y=y)

        self.root.mainloop()

    def locate_xy(self, event):
        self.current_x = event.x
        self.current_y = event.y

    def add_line(self, event):
        self.canvas.create_line((self.current_x, self.current_y, event.x, event.y), width=self.width, fill=self.color, capstyle=ROUND, smooth=TRUE)
        self.undo_stack.append(('line', (self.current_x, self.current_y, event.x, event.y), self.width, self.color))
        self.current_x, self.current_y = event.x, event.y

    def pick_color(self):
        self.color = askcolor()[1]

    def change_width(self, value):
        self.width = int(value)

    def clear_canvas(self):
        self.canvas.delete('all')
        
    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            if action[0] == 'line':
                self.canvas.delete('all')
                for line in self.undo_stack:
                    if line[0] == 'line':
                        self.canvas.create_line(line[1], width=line[2], fill=line[3], capstyle=ROUND, smooth=TRUE)

if __name__ == '__main__':
    WhiteBoard()