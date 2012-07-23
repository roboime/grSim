try:# for python 3
    from tkinter import *
    from tkinter import ttk
except ImportError:# for python 2
    from Tkinter import *
    import ttk

# Helper class to make labels and input
class Input(ttk.Frame):
    def __init__(self, parent, widget='entry', **kw):
        ttk.Frame.__init__(self, parent)
        rows = 0
        cols = 0

        if widget == 'entry':
            rows = 1; cols = 2
            label = ttk.Label(self, text=kw.get('text'), justify='left')
            label.grid(column=0, row=0, sticky=EW)
            entry = ttk.Entry(self)
            entry.grid(column=1, row=0, sticky=EW)

        elif widget == 'check':
            rows = cols = 1
            checkbox = ttk.Checkbutton(self, text=kw.get('text'))
            checkbox.grid(column=0, row=0, sticky=EW)

        elif widget == 'combo':
            rows = cols = 1
            combobox = ttk.Combobox(self, values=kw.get('values'), state=('readonly',))
            combobox.grid(column=0, row=0, sticky=EW)

        else:
            raise TypeError

        for i in range(rows):
            self.columnconfigure(i, weight=1)

        for i in range(cols):
            self.rowconfigure(i, weight=1)


class Client(Tk):

    def loop(self):
        #TODO: network loop goes here
        pass

    def connect(self):
        pass

    def send(self):
        pass

    def reset(self):
        pass

    def __init__(self):
        Tk.__init__(self)

        # Attributes
        self.interval = 50

        # Window
        self.title('grSim Sample Python Client')
        self.resizable(width=False, height=False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = ttk.Frame(self, padding=(10, 10, 10, 10))

        # Controls
        self.sim_addr = Input(content, text='Simulator Address')
        self.sim_port = Input(content, text='Simulator Port')
        self.rob_id =   Input(content, text='Robot Id')
        self.color =    Input(content, 'combo', values=('Yellow', 'Blue'))
        self.speed_x =  Input(content, text='Speed X (m/s)')
        self.speed_y =  Input(content, text='Speed Y (m/s)')
        self.speed_w =  Input(content, text='Speed W (rad/s)')
        self.is_speed = Input(content, 'check', text='Speeds? (otherwise wheels)')
        self.wheel1 =   Input(content, text='Wheel1 (rad/s)')
        self.wheel2 =   Input(content, text='Wheel2 (rad/s)')
        self.wheel3 =   Input(content, text='Wheel3 (rad/s)')
        self.wheel4 =   Input(content, text='Wheel4 (rad/s)')
        self.chip =     Input(content, text='Chip (m/s)')
        self.kick =     Input(content, text='Kick (m/s)')
        self.is_spin =  Input(content, 'check', text='Spin')

        connect = ttk.Button(content, text='Connect', command=self.connect)
        frame =   ttk.Frame(content)
        send =    ttk.Button(frame, text='Send', command=self.send)
        reset =   ttk.Button(frame, text='Reset', command=self.reset)

        # General layout
        def stack(col, widgets):
            row = 0
            for w in widgets:
                if w is not None:
                    w.grid(column=col, row=row, stick=EW)
                row += 1

        stack(0, [self.sim_addr, self.rob_id, self.is_speed, self.speed_x, self.speed_y, self.speed_w, self.chip, self.is_spin, connect])
        stack(1, [self.sim_port, self.color, self.wheel1, self.wheel2, self.wheel3, self.wheel4, self.kick, None, frame])

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)
        send.grid(column=0, row=0, sticky=EW)
        reset.grid(column=1, row=0, sticky=EW)
        content.grid(column=0, row=0, sticky=NSEW)

        for i in range(2):
            content.columnconfigure(i, weight=1)

        for i in range(9):
            content.rowconfigure(i, weight=1)

    def _bgloop(self):
        self.loop()
        self.after(self.interval, self._bgloop)

    def mainloop(self):
        self._bgloop()
        Tk.mainloop(self)


if __name__ == '__main__':
    # Let the magic begin
    app = Client()
    app.mainloop()

