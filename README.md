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

#### Tested on Windows systems and runs normally after being packaged with "pyinstaller"
------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Download Executable File
You can download the latest version of the `.exe` program from the [Releases](https://github.com/Raclsc/WakeOnMagicPacket/releases) page. 
No installation is required, just double-click to open.

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Usage
### Run the Executable File ([Download](https://github.com/Raclsc/WakeOnMagicPacket/releases))
1. Enter the device's MAC address (supports `-` separation, auto-formatting).
2. Set the broadcast IP (default is 255.255.255.255).
3. Click the "Send" button to send the Magic Packet.
4. Success will be displayed on the screen as "Send to 255.255.255.255".

### Run the Program (when not packaged)
```Command Line
python WakeOnMagicPacket.py
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Author
**Raclsc Chen** 
GitHub: [@Raclsc](https://github.com/Raclsc)
