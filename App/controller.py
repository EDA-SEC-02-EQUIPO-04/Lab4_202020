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

import config as cf
from App import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def initCatalog_movies():
    """
    Llama la función de inicialización del catalogo de películas del modelo.
    
    """
    # catalog_movies es utilizado para interactuar con el modelo de películas
    catalog_movies = model.newCatalog_movies()
    # catalog_casting es utilizado para interactural con l modelo de casting
    catalog_casting = model.newCatalog_casting()
    return catalog_movies,catalog_casting

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________



def loadData(catalog_movies, catalog_casting, movies, casting):
    """
    Carga los datos de los archivos del modelo

    Args:
        movies (csv): Archivo  que contiene las películas
        casting (csv): Archivo que contiene el casting de las películas
    """
    loadMovies(catalog_movies, movies)
    loadMovies(catalog_casting, casting)

def loadMovies(catalog, moviesfile,):
    """
    Carga cada una de las lineas del archivo de movies.
    - Se agrega cada película al catalogo de películas
    - Por cada película se encuentran sus directores y por cada
      director, se crea una lista con sus películas
    """
    moviesfilem = cf.data_dir + moviesfile
    inpunt_file = csv.DictReader(open(moviesfile))
    for movie in inpunt_file:
        model.addmovie(catalog, movie)
        movies = movie["vote_average"].split(',')
        for movie in movies:
            


