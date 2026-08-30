#si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("c:\\Users\\guerr\\OneDrive\\Desktop\\Python-de-cero\\python-from-scratch\\funciones_up")

import saludar as modulo_saludar

print(modulo_saludar.despedida("Kraton"))
