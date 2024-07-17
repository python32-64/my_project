import os
import keyboard as kb
import socket, pygame
from threading import Thread as Th
from win32api import GetSystemMetrics
from PIL import Image


def screen():
    def f():
        file = open('image11.png', 'wb')

        d = s.recv(40960)
        while d:
            file.write(d)
            d = s.recv(40960)
        file.close()
        s.close()

    pygame.init()
    X = GetSystemMetrics()[0]
    Y = GetSystemMetrics()[1]


    scrn = pygame.display.set_mode((X, Y))
    status = True
    while (status):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('ваш ip', 8002))

        f()

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                status = False

        imp = pygame.image.load(r"image11.png").convert()
        scrn.blit(imp, (0, 0))
        pygame.display.flip()

    pygame.quit()


def command_keyboard():
    import keyboard, socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(('ваш ip', 8003))
    try:
        while True:
            cli.send(bytes(keyboard.read_key(), encoding='utf-8'))
    except:
        cli.close()


def mouse_():
    import mouse, socket
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(('ваш ip', 8004))
    try:
        while True:
            cli.send(bytes(f'{mouse.get_position()[0]} {mouse.get_position()[1]}', encoding='utf-8'))
    except:
        cli.close()


Th(target=screen).start()
Th(target=mouse_).start()
Th(target=command_keyboard).start()
