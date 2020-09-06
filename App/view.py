"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller

assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
casting_file = config.data_dir + 'MoviesCastingRaw-small.csv'
details_file = config.data_dir + 'MoviesDetailsCleaned-small.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________
def print_menu():
    print('Bienvenido')
    print('1- Reinicializar el catálogo de películas')
    print('2- Cargar datos de películas de los archivos csv')
    print('0- Salir')


cont = controller.init_catalog()
while True:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Reinicializando Catálogo...')
        cont = controller.init_catalog()  # cont es el controlador que se usará en adelante.
    if int(inputs[0]) == 2:
        print('Cargando información de los archivos...')
        controller.loadData(casting_file, details_file)
        print('Detalles de películas cargados: ' + str(controller.details_size(cont)))
        print('Casting de películas cargados: ' + str(controller.casting_size(cont)))
    elif int(inputs[0]) == 0:
        sys.exit(0)
    else:
        print('Opción no válida, intente de nuevo')
