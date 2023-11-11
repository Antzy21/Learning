import logging
from typing import Tuple, List, Optional
from lux.constants import *
from lux.game_map import *
from functools import reduce

PosTuple = Tuple[int, int]

def posTupleFromPos(pos: Position) -> PosTuple:
    return (pos.x, pos.y)
def posFromTile(tile: Cell) -> Position:
    return tile.pos
def posTupleFromTile(tile: Cell) -> PosTuple:
    return posTupleFromPos(posFromTile(tile))

def fst(tuple: Tuple):
    return tuple[0]
def snd(tuple: Tuple):
    return tuple[1]

def tupleString(t: Tuple):
    if t is None:
        return "None"
    return f"({t[0]},{t[1]})"
def posString(pos: Position):
    if pos is None:
        return "None"
    return tupleString((pos.x, pos.y))
def tilePosString(tile: Cell):
    if tile is None:
        return "None"
    return posString(tile.pos)
def printPos(pos):
    if type(pos) is Position:
        return posString(pos)
    return ""

def defaultPrintFunc(i):
    return f"{i}"
def printList(lst: list, printFunc = defaultPrintFunc, initial_string = ""):
    if lst is None:
        return "empty list"
    def reduceFunc(i1, i2):
        return f"{i1}, {printFunc(i2)}"
    list_string = reduce(reduceFunc, lst, initial_string)
    return list_string

def validateDirection(dir):
    if dir == Constants.DIRECTIONS.CENTER:
        return True
    if dir == Constants.DIRECTIONS.EAST:
        return True
    if dir == Constants.DIRECTIONS.WEST:
        return True
    if dir == Constants.DIRECTIONS.NORTH:
        return True
    if dir == Constants.DIRECTIONS.SOUTH:
        return True
    return False

def positionPathFromDirPath(dirPath: List[Constants.DIRECTIONS], start: Position) -> List[Position]:
    posPath: List[PosTuple] = [posTupleFromPos(start)]
    for direction in dirPath:
        posPath.append(posPath[-1].adjacent(direction))
    return posPath

def getCityOnPos(pos: Position, player, game_map):
    city_tile = game_map.get_cell_by_pos(pos).citytile
    if city_tile is None:
        return None
    return player.cities[city_tile.cityid]