# WakeOnMagicPacket
This is a Graphical interface tool created using Python that supports sending Magic Packets over the network to wake devices that support the Wake-on-LAN feature.
It offers a simple and intuitive user interface and can be packaged into a Windows executable (.exe) using "pyinstaller".

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Project Features
1. Graphical User Interface (GUI) operation, no command line needed
2. Customizable broadcast IP address and target MAC address
3. Real-time MAC format validation and formatting (e.g., automatically adding "-")
4. Instant message prompts and error alerts
5. One-click Magic Packet sending
6. Can be packaged into a portable EXE using "pyinstaller"

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Runtime Environment
- Python 3.6+
- Standard libraries: tkinter, socket, sys, time
Tested on Windows systems and runs normally after being packaged with "pyinstaller"
------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Installation and Usage
### Run the Program (when not packaged)
```Command Line
python WakeOnMagicPacket.py


