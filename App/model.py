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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------
def crimesSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['crimes'])


def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['dateTree'])


def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['dateTree'])


def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['dateTree'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['dateTree'])

def newTree(cmpfunction):
    return om.newMap(omaptype='RBT',comparefunction=cmpfunction)

def newList(cmpfunction,type='SINGLE_LINKED'):
    return lt.newList(type,cmpfunction)

def newHash(numelements=503,type='CHAINING',loadFactor=2,comparefunction=None):
    return m.newMap(numelements=numelements,maptype=type,loadfactor=loadFactor,comparefunction=comparefunction)

# Funciones para agregar informacion al catalogo

def addListAccident(lst,accident):
    lt.addFirst(lst,accident)

def addTreeNode(tree,key,value):
    om.put(tree,key,value)

# ==============================
# Funciones de consulta
# ==============================
def getTreeKey(tree,key):
    return om.get(tree,key)

def getTreeAllKeys(tree):
    return om.keySet(tree)

# ==============================
# Funciones de Comparacion
# ==============================