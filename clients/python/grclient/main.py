try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import *
    import ttk

# Helper class to make labels and input
class Input(ttk.Frame):
    def __init__(self, parent, text):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=text)
        entry = ttk.Entry(self)
        # placement
        label.grid(column=0, row=0, columnspan=2, sticky=(W))
        entry.grid(column=3, row=0, columnspan=2, sticky=(W, E))

root = Tk()
root.title('grSim Sample Python Client')
content = ttk.Frame(root, padding=(12, 12, 12, 12))

# Controls
simulator_addr = Input(content, 'Simulator Address')
simulator_port = Input(content, 'Simulator Port')
robot_id = Input(content, 'Robot Id')
robot_color = ttk.Combobox(content, values=('Yellow', 'Blue'))
speed_x = Input(content, 'Speed X (m/s)')
speed_y = Input(content, 'Speed Y (m/s)')
speed_w = Input(content, 'Speed W (rad/s)')
is_speed = ttk.Checkbutton(content, text='Send linear speeds? (otherwise will use wheel speeds)')
wheel1 = Input(content, 'Wheel1 (rad/s)')
wheel2 = Input(content, 'Wheel2 (rad/2)')
wheel3 = Input(content, 'Wheel3 (rad/2)')
wheel4 = Input(content, 'Wheel4 (rad/2)')
chip = Input(content, 'Chip (m/s)')
kick = Input(content, 'Kick (m/s)')
is_spin = ttk.Checkbutton(content, text='Spin')
connect = ttk.Button(content, text='Connect')
send = ttk.Button(content, text='Send')
reset = ttk.Button(content, text='Reset')

# General layout
def stack(col, widgets):
    row = 0
    for w in widgets:
        w.grid(column=col, row=row, columnspan=2)
        row += 1

stack(0, [simulator_addr, robot_id, speed_x, speed_y, speed_w, is_speed, chip, is_spin, connect])
stack(2, [simulator_port, robot_color, wheel1, wheel2, wheel3, wheel4, kick])
send.grid(column=2, row=8, columnspan=1)
reset.grid(column=3, row=8, columnspan=1)
content.grid(column=0, row=0, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
for i in range(4):
    content.columnconfigure(i, weight=1)
for i in range(9):
    content.rowconfigure(i, weight=1)

# Let the magic begin
root.mainloop()

