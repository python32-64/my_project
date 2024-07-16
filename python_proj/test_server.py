import socket

import threading
from threading import Thread as Th

from pyautogui import screenshot

con = 1


def f():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8002))

    s.listen(2)
    conn, addr = s.accept()
    print(conn, addr, 'f')
    while 1:
        screenshot().save('myimage.png')
        for i in open('myimage.png', 'rb'):
            conn.send(i)
        s.close()
        break
    # s.close()


def f1():
    import keyboard
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8003))
    con, addr = s.accept()
    key = con.recv(20971520).decode()
    keyboard.press(key)


def f2():
    import mouse
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 8004))
    con, addr = s.accept()
    mouse_pos = con.recv(20971520).decode().split(' ')
    mouse.move(int(mouse_pos[0]), int(mouse_pos[0]))


# f2()

def start():
    while 1:
        f()


Th(target=start).start()
Th(target=f2).start()
Th(target=f1).start()
# Th(target=f2).start()
# try:
#     f()
# except Exception as e:
#     print('er',e)
#     f1()
# else:
#     f2()

    # threading.Thread(target=f1).start()
    # time.sleep(.65)
# for i in open('image.png', 'rb'):
#     conn.send(i)
