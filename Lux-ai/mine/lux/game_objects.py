from typing import Dict, List, Tuple
import logging
from .constants import Constants
from .game_map import Position, GameMap, Cell
from .game_constants import GAME_CONSTANTS
from commonFunctions import *
from nearest import directionToNearest

UNIT_TYPES = Constants.UNIT_TYPES
night_length = 10

class Player:
    def __init__(self, team):
        self.team = team
        self.research_points = 0
        self.units: list[Unit] = []
        self.cities: Dict[str, City] = {}
        self.city_tile_count = 0
    def researched_coal(self) -> bool:
        return self.research_points >= GAME_CONSTANTS["PARAMETERS"]["RESEARCH_REQUIREMENTS"]["COAL"]
    def researched_uranium(self) -> bool:
        return self.research_points >= GAME_CONSTANTS["PARAMETERS"]["RESEARCH_REQUIREMENTS"]["URANIUM"]

class City:
    def __init__(self, teamid, cityid, fuel, light_upkeep):
        self.cityid = cityid
        self.team = teamid
        self.fuel = fuel
        self.citytiles: list[CityTile] = []
        self.light_upkeep = light_upkeep
    def _add_city_tile(self, x, y, cooldown):
        ct = CityTile(self.team, self.cityid, x, y, cooldown)
        self.citytiles.append(ct)
        return ct

    def get_light_upkeep(self):
        return self.light_upkeep
    def has_fuel_to_survive_night(self) -> bool:
        return self.fuel > self.get_light_upkeep() * night_length
    def cityTileCellsWithAdjResAmt(self, game_map: 'GameMap', player = None) -> List[Tuple['Cell', int]]:
        lst: List[Tuple[Cell, int]] = []
        for city_tile in self.citytiles:
            res_amount = 0
            cell: 'Cell' = city_tile.get_cell(game_map)
            for adjacent_tile in cell.getAdjacents(game_map):
                if adjacent_tile.has_resource_researched_by_player(player):
                    res = adjacent_tile.resource
                    res_amount = res.amount
                    if res.type == Constants.RESOURCE_TYPES.WOOD:
                        res_amount += -400
            lst.append((cell, res_amount))
        lst.sort(key = snd, reverse = True)
        return lst
    def cityTilesWithNoTrees(self, game_map, player) -> List['Cell']:
        city_tiles_with_no_trees = []
        for cell, tree_count in self.cityTileCellsWithAdjResAmt(game_map, player):
            if tree_count == 0:
                city_tiles_with_no_trees.append(cell)
        return city_tiles_with_no_trees
    
    def is_starving(self):
        starving = self.get_light_upkeep() * night_length> self.fuel + 500
        if starving: logging.info(f" City {self.cityid} is starving!")
        return starving

    def should_be_fed(self, game_state):
        near_night_and_hungry = game_state.is_near_night() and not self.has_fuel_to_survive_night()
        should_be_fed = self.is_starving() or near_night_and_hungry
        if should_be_fed and not self.is_starving():
            logging.info(f" City {self.cityid} should be fed")
        return should_be_fed

class CityTile:
    def __init__(self, teamid, cityid, x, y, cooldown):
        self.cityid = cityid
        self.team = teamid
        self.pos = Position(x, y)
        self.cooldown = cooldown
    def can_act(self) -> bool:
        """
        Whether or not this unit can research or build
        """
        return self.cooldown < 1
    def research(self) -> str:
        """
        returns command to ask this tile to research this turn
        """
        return "r {} {}".format(self.pos.x, self.pos.y)
    def build_worker(self) -> str:
        """
        returns command to ask this tile to build a worker this turn
        """
        return "bw {} {}".format(self.pos.x, self.pos.y)
    def build_cart(self) -> str:
        """
        returns command to ask this tile to build a cart this turn
        """
        return "bc {} {}".format(self.pos.x, self.pos.y)
    def get_cell(self, game_map) -> 'Cell':
        return game_map.get_cell_by_pos(self.pos)

class Cargo:
    def __init__(self):
        self.wood = 0
        self.coal = 0
        self.uranium = 0
    def __str__(self) -> str:
        return f"Cargo | Wood: {self.wood}, Coal: {self.coal}, Uranium: {self.uranium}"

class Unit:
    def __init__(self, teamid, u_type, unitid, x, y, cooldown, wood, coal, uranium):
        self.pos = Position(x, y)
        self.team = teamid
        self.id = unitid
        self.type = u_type
        self.cooldown = cooldown
        self.cargo = Cargo()
        self.cargo.wood = wood
        self.cargo.coal = coal
        self.cargo.uranium = uranium
        self.patrol = None
        self.target = None

    def is_worker(self) -> bool:
        return self.type == UNIT_TYPES.WORKER

    def is_cart(self) -> bool:
        return self.type == UNIT_TYPES.CART

    def is_adjacent_to_resource(self, game_map):
        cell = game_map.get_cell_by_pos(self.pos)
        return cell.is_adjacent_to_resource(game_map)

    def get_cargo_space_left(self):
        """
        get cargo space left in this unit
        """
        spaceused = self.cargo.wood + self.cargo.coal + self.cargo.uranium
        if self.type == UNIT_TYPES.WORKER:
            return GAME_CONSTANTS["PARAMETERS"]["RESOURCE_CAPACITY"]["WORKER"] - spaceused
        else:
            return GAME_CONSTANTS["PARAMETERS"]["RESOURCE_CAPACITY"]["CART"] - spaceused
    
    def can_build(self, game_map) -> bool:
        """
        whether or not the unit can build where it is right now
        """
        cell = game_map.get_cell_by_pos(self.pos)
        if not cell.has_resource() and self.can_act() and (self.cargo.wood + self.cargo.coal + self.cargo.uranium) >= GAME_CONSTANTS["PARAMETERS"]["CITY_BUILD_COST"]:
            return True
        return False

    def can_act(self) -> bool:
        """
        whether or not the unit can move or not. This does not check for potential collisions into other units or enemy cities
        """
        return self.cooldown < 1

    def move(self, dir) -> str:
        """
        return the command to move unit in the given direction
        """
        return "m {} {}".format(self.id, dir)

    def transfer(self, dest_id, resourceType, amount) -> str:
        """
        return the command to transfer a resource from a source unit to a destination unit as specified by their ids
        """
        return "t {} {} {} {}".format(self.id, dest_id, resourceType, amount)

    def build_city(self) -> str:
        """
        return the command to build a city right under the worker
        """
        return "bcity {}".format(self.id)

    def pillage(self) -> str:
        """
        return the command to pillage whatever is underneath the worker
        """
        return "p {}".format(self.id)

    def getNewCell(self, direction, game_map):
        pos = self.pos.adjacent(direction)
        return game_map.get_cell_by_pos(pos)
        
    def moveToNearest(self, game_map, target, avoid = []):
        direction = directionToNearest(game_map, self, target, avoid)
        mv = self.move(direction)
        if type(mv) is not str:
            logging.error(f"not string: {mv}")
        return mv