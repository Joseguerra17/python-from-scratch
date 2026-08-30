#importando un modulo y asignandole el nombre m_saludar
import modulo_saludar as m_saludar

saludo = m_saludar.saludar("Lola")
print(saludo)

#desde ese modulo, importamos funciones y las renombramos, (ESTO ES UNA MALA PRACTICA)
from modulo_saludar import saludar as saludar_inicial,despedida as despedida_final

saludo = saludar_inicial("Juanito")
adios = despedida_final("Kratos")
print(adios)

#desde ese modulo, importamos funciones
from modulo_saludar import saludar,despedida

saludo = saludar("Juanito")
adios = despedida("Kratos")
print(saludo)

#forma de ver las propiedades y metodos de el namespace
#print(dir(m_saludar)) 

#acceder al nombre de este modulo
#print(__name__)

#accder al nombre del modulo llamado
#print(m_saludar.__name__)