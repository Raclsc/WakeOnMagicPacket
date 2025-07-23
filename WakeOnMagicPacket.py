## Wake on Magic Packet
import sys
import time
import socket
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#######################################################
#                 Format Magic Packet                 #
#######################################################
def MagicPacket(MAC):
    MAC = str(MAC)
    if len(MAC) == 12:
        pass

    elif len(MAC) == 17 and (MAC.count(":") == 5 or MAC.count("-") == 5):
        Symbol = MAC[2]
        MAC = MAC.replace(Symbol, "")

    else:
        messagebox.showerror("Wake on Magic Packet", "Incorrect MAC Address!\nPlease try again!")
        SendButton.event_generate("<ButtonRelease-1>")
        return "Error"
    
    try:
        MagPkt = bytes.fromhex("FF" * 6 + MAC * 16)

    except Exception as err:
        messagebox.showerror("Wake on Magic Packet", "Incorrect MAC Address!\nPlease try again!")
        SendButton.event_generate("<ButtonRelease-1>")
        return "Error"


    return MagPkt

#######################################################
#                 Sending Magic Packet                #
#######################################################
def Send(Broadcast, MagPkt):
    PORT = 9
    
    try:
        SocketObject = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        SocketObject.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        SocketObject.sendto(MagPkt, (Broadcast, PORT))

    except Exception as err:
        messagebox.showerror("Wake on Magic Packet", "Send Magic Packet Error!\nError Message:\n%s" %(err))
        SendButton.event_generate("<ButtonRelease-1>")

#######################################################
#                 Wake on Magic Packet                #
#######################################################
def WakeOnMagicPacket():
    Broadcast="%s.%s.%s.%s" %(BroadcastEntry_1.get(), BroadcastEntry_2.get(), BroadcastEntry_3.get(), BroadcastEntry_4.get())
    MACaddress=AddressEntry.get()
    MagPkt = MagicPacket(MACaddress)
    if MagPkt != "Error":
        Send(Broadcast, MagPkt)
    print(Broadcast)

#######################################################
#                   Address Display                   #
#######################################################
def AddressDisplay(event):
    AddressText = AddressEntry.get().replace("-", "").upper()

    if len(AddressEntry.get()) > 12:
        AddressText = AddressText[:12]

    AddressFormat = "-".join(AddressText[i:i+2] for i in range(0, len(AddressText), 2))

    AddressEntry.delete(0, END)
    AddressEntry.insert(0, AddressFormat)

#######################################################
#                     Press Button                    #
#######################################################
def PressBTN(event):
    Broadcast="%s.%s.%s.%s" %(BroadcastEntry_1.get(), BroadcastEntry_2.get(), BroadcastEntry_3.get(), BroadcastEntry_4.get())
    SendMessage.set("Send to %s" %(Broadcast))

#######################################################
#                    Release Button                   #
#######################################################
def ReleaseBTN(event):
    time.sleep(0.3)
    SendMessage.set("")

#######################################################
#                    Center Window                    #
#######################################################
def CenterWindow(root):
    root.update_idletasks()
    WindowWidth = root.winfo_width()
    WindowHeight = root.winfo_height()
    ScreenWidth = root.winfo_screenwidth()
    ScreenHeight = root.winfo_screenheight()
    WindowX = (ScreenWidth - WindowWidth) // 2
    WindowY = (ScreenHeight - WindowHeight) //2
    root.geometry("+%d+%d" %(WindowX, WindowY))

#######################################################
#                     Main Program                    #
#######################################################
if __name__ == "__main__":
    root = Tk()
    root.title("Wake on Magic Packet")
    root.after(0, lambda: CenterWindow(root))

    Address = StringVar()
    Address.set("FF-00-FF-00-FF-00")
    # Address.set("AA-AA-AA-AA-AA-AA")
    Broadcast_1 = StringVar()
    Broadcast_1.set("255")
    Broadcast_2 = StringVar()
    Broadcast_2.set("255")
    Broadcast_3 = StringVar()
    Broadcast_3.set("255")
    Broadcast_4 = StringVar()
    Broadcast_4.set("255")
    SendMessage = StringVar()
    SendMessage.set("")

    BroadcastLabel = Label(root, text="IP Broadcast Address:")
    BroadcastEntry_1 = Entry(root, width=3, font=10, justify="center", textvariable=Broadcast_1)
    BroadcastEntry_2 = Entry(root, width=3, font=10, justify="center", textvariable=Broadcast_2)
    BroadcastEntry_3 = Entry(root, width=3, font=10, justify="center", textvariable=Broadcast_3)
    BroadcastEntry_4 = Entry(root, width=3, font=10, justify="center", textvariable=Broadcast_4)
    Dot1 = Label(root, text=".")
    Dot2 = Label(root, text=".")
    Dot3 = Label(root, text=".")
    AddressLabel = Label(root, text="MAC Address:")
    AddressEntry = Entry(root, width=24, font=14, justify="center", textvariable=Address)
    MessageLabel = Label(root, font= 12, justify="center", textvariable=SendMessage, relief="groove")
    SendButton = Button(root, width=10, text="Send", command=WakeOnMagicPacket)
    ExitButton = Button(root, width=10, text="Exit", command=sys.exit)

    AddressEntry.bind("<KeyRelease>", AddressDisplay)
    SendButton.bind("<ButtonPress-1>", PressBTN)
    SendButton.bind("<ButtonRelease-1>", ReleaseBTN)

    BroadcastLabel.grid(row=0, column=0, columnspan=8, sticky="w", ipadx=3, ipady=3, padx=3, pady=3)
    BroadcastEntry_1.grid(row=1, column=1, sticky="nsew", ipadx=3, ipady=3, padx=3)
    Dot1.grid(row=1, column=2, sticky="nsew")
    BroadcastEntry_2.grid(row=1, column=3, sticky="nsew", ipadx=3, ipady=3, padx=3)
    Dot2.grid(row=1, column=4, sticky="nsew")
    BroadcastEntry_3.grid(row=1, column=5, sticky="nsew", ipadx=3, ipady=3, padx=3)
    Dot3.grid(row=1, column=6, sticky="nsew")
    BroadcastEntry_4.grid(row=1, column=7, sticky="nsew", ipadx=3, ipady=3, padx=3)
    AddressLabel.grid(row=2, column=0, columnspan=8, sticky="w", ipadx=3, ipady=3, padx=3)
    AddressEntry.grid(row=3, column=0, columnspan=8, sticky="nsew", ipadx=3, ipady=3, padx=3)
    MessageLabel.grid(row=4, column=0, columnspan=8, sticky="nsew", ipadx=3, ipady=3, padx=3, pady=3)
    SendButton.grid(row=0, column=8, rowspan=3, sticky="nsew", ipadx=3, ipady=3, padx=3, pady=3)
    ExitButton.grid(row=3, column=8, rowspan=2, sticky="nsew", ipadx=3, ipady=3, padx=3, pady=3)
    
    root.mainloop()