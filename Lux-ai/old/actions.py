import logging
from lux.game import Unit, Player
from lux.game_map import DIRECTIONS
from lux.game_objects import City
from getTiles import getAdjacentToCityTiles, getInverse
from commonFunctions import posFromTile, getCityOnPos
from nearest import nearest, nearestCity


def makeNewCityTile(game_map, unit: Unit, city, tiles):
    if city is None:
        tiles['to_build_city'] = tiles['empty']
    else:
        tiles['to_build_city'] = getAdjacentToCityTiles(game_map, city)

    tilePositions = [posFromTile(t) for t in tiles['to_build_city']]    
    if unit.pos in tilePositions:
        #logging.info(f" {unit.id} will build here")
        return unit.build_city()
    else:
        return unit.moveToNearest(game_map, target = tiles['to_build_city'], avoid = tiles['city']+tiles['enemy_city'])

def fuelNearbyCity(game_map, unit: Unit, tiles):
    if unit.get_cargo_space_left() > 20:
        logging.info(f" {unit.id} will collect to fuel city. ")
        return unit.moveToNearest(game_map, target = tiles['resource'], avoid = tiles['enemy_city'])
    else:
        logging.info(f" {unit.id} will return to city. ")
        return unit.moveToNearest(game_map, target = tiles['city'], avoid = tiles['enemy_city'])

def resolveWorkerAction(unit: 'Unit', player: Player, opponent: Player, tiles, game_state):
    game_map = game_state.map
    city: 'City' = nearestCity(player, unit, tiles['city'])
    if city is None:
        return makeNewCityTile(game_map, unit, city, tiles)
    elif city.should_be_fed(game_state) or player.city_tile_count > opponent.city_tile_count + 5:
        return fuelNearbyCity(game_map, unit, tiles)
    elif game_state.is_night():
        return unit.moveToNearest(game_map, target = tiles['city'], avoid = tiles['enemy_city'])
    elif unit.get_cargo_space_left() == 0:
        return makeNewCityTile(game_map, unit, city, tiles)
    else:
        return unit.moveToNearest(game_map, target = tiles['resource'], avoid = tiles['enemy_city'])

def farmer(unit: Unit, player: Player, opponent: Player, tiles, game_state):
    game_map = game_state.map
    city = getCityOnPos(unit.pos, player, game_map)
    if city is None:
        logging.error("Worker not in city")
        return unit.moveToNearest(game_map, tiles['city'])

    city_tile_cells_with_tree_availability = city.cityTileCellsWithAdjResAmt(game_map)
    target = None
    max_tree = 0
    for cell, tree_availability in city_tile_cells_with_tree_availability:
        if tree_availability > max_tree:
            target = [cell]
    logging.error(f"max tree: {max_tree}, {cell}")


    if target is None:
        no_tree_tiles = city.cityTilesWithNoTrees(game_map)
        return unit.moveToNearest(game_map, no_tree_tiles, avoid = getInverse(tiles['city'], game_map))
    return unit.moveToNearest(game_map, target, avoid = getInverse(tiles['city'], game_map))

def createWorker(city: City, game_state):
    if game_state.is_near_night():
        return None
    for cell, _ in city.cityTileCellsWithAdjResAmt(game_state.map):
        city_tile = cell.citytile
        return city_tile.build_worker()

def research(city: City, game_state):
    for city_tile in city.citytiles:
        if city_tile.can_act():
            return city_tile.research()


