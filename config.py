from sys import platform
import os


# Тут мелкая боль разработки под виндой, хех, путь коварен.
# Переходи на светлую сторону, ставь Linux!
if platform == 'win32':
    DB = os.getcwd()+'\\db\\nettab.db'
else:
    DB = 'db/nettab.db'


