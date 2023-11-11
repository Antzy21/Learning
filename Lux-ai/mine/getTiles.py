import logging
from typing import List
from lux.game_map import DIRECTIONS, Cell, GameMap
from lux.constants import Constants
from commonFunctions import posTupleFromTile

def getTiles(tileCondition, game_map: GameMap) -> List[Cell]:
    tiles: List[Cell] = []
    for y in range(game_map.height):
        for x in range(game_map.width):
            cell = game_map.get_cell(x, y)
            if tileCondition(cell):
                tiles.append(cell)
    return tiles

def getInverse(tiles: List[Cell], game_map: GameMap) -> List[Cell]:
    def filter(cell):
        return cell in tiles
    return getTiles(filter, game_map)

def resourceFilter(tile: 'Cell', player, preserve_trees = True):
    if not tile.has_resource_researched_by_player(player):
        return False
    if preserve_trees and tile.resource.type == Constants.RESOURCE_TYPES.WOOD:
        if tile.resource.amount < 450:
            return False
    return True

def getResourceTiles(game_map: GameMap, player) -> List[Cell]:
    def filter(cell):
        return resourceFilter(cell, player)
    return getTiles(filter, game_map)

def getPlayerCityTiles(player) -> List[Cell]: 
    city_tiles = []
    if len(player.cities) == 0:
        return []
    for _, city in player.cities.items():
        for city_tile in city.citytiles:
            city_tiles.append(city_tile)
    return city_tiles

def isEmpty(cell):
    return cell.isEmpty()

def getEmptyTiles(game_map: GameMap) -> List[Cell]:
    return getTiles(isEmpty, game_map)

def getAdjacentToCityTiles(game_map: GameMap, city) -> List[Cell]:
    tiles: List[Cell] = []
    for city_tile in city.citytiles:
        cell: 'Cell' = city_tile.get_cell(game_map)
        for adj_cell in cell.getAdjacents(game_map):    
            if adj_cell.isEmpty():
                tiles.append(adj_cell)
    return tiles
    
def getUnitTiles(game_map: GameMap, player) -> List[Cell]:
    list = []
    for unit in player.units:
        if not unit.can_act():
            list.append(game_map.get_cell_by_pos(unit.pos))
    return list

def getTilesDict(game_state, player, opponent):
    resource = getResourceTiles(game_state.map, player)
    empty = getEmptyTiles(game_state.map)
    city = getPlayerCityTiles(player)
    not_city = getInverse(city, game_state.map)
    enemy_city = getPlayerCityTiles(opponent)
    unit_occupied = getUnitTiles(game_state.map, player)
    return {
        'resource': resource,
        'empty': empty,
        'city': city,
        'not_city': not_city,
        'enemy_city': enemy_city,
        'unit_occupied': unit_occupied
    }