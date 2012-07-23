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

    def __init__(self):
        Tk.__init__(self)

        self.title('grSim Sample Python Client')
        self.resizable(width=False, height=False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = ttk.Frame(self, padding=(12, 12, 12, 12))

        # Controls
        sim_addr = Input(content, text='Simulator Address')
        sim_port = Input(content, text='Simulator Port')
        rob_id =   Input(content, text='Robot Id')
        color =    Input(content, 'combo', values=('Yellow', 'Blue'))
        speed_x =  Input(content, text='Speed X (m/s)')
        speed_y =  Input(content, text='Speed Y (m/s)')
        speed_w =  Input(content, text='Speed W (rad/s)')
        is_speed = Input(content, 'check', text='Speeds? (otherwise wheels)')
        wheel1 =   Input(content, text='Wheel1 (rad/s)')
        wheel2 =   Input(content, text='Wheel2 (rad/s)')
        wheel3 =   Input(content, text='Wheel3 (rad/s)')
        wheel4 =   Input(content, text='Wheel4 (rad/s)')
        chip =     Input(content, text='Chip (m/s)')
        kick =     Input(content, text='Kick (m/s)')
        is_spin =  Input(content, 'check', text='Spin')

        connect = ttk.Button(content, text='Connect')
        frame =   ttk.Frame(content)
        send =    ttk.Button(frame, text='Send')
        reset =   ttk.Button(frame, text='Reset')

        # General layout
        def stack(col, widgets):
            row = 0
            for w in widgets:
                if w is not None:
                    w.grid(column=col, row=row, stick=EW)
                row += 1

        stack(0, [sim_addr, rob_id, is_speed, speed_x, speed_y, speed_w, chip, is_spin, connect])
        stack(1, [sim_port, color, wheel1, wheel2, wheel3, wheel4, kick, None, frame])

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


if __name__ == '__main__':
    # Let the magic begin
    app = Client()
    app.mainloop()

