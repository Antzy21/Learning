import math
import logging
from typing import List

from .constants import Constants

DIRECTIONS = Constants.DIRECTIONS
RESOURCE_TYPES = Constants.RESOURCE_TYPES


class Resource:
    def __init__(self, r_type: str, amount: int):
        self.type = r_type
        self.amount = amount


class Cell:
    def __init__(self, x, y):
        self.pos = Position(x, y)
        self.resource: Resource = None
        self.citytile = None
        self.road = 0
    def has_resource(self) -> bool:
        return self.resource is not None and self.resource.amount > 0
    def has_resource_researched_by_player(self, player):
        if player is None:
            return self.has_resource()
        if not self.has_resource():
            return False
        elif self.resource.type == Constants.RESOURCE_TYPES.WOOD:
            return True
        elif self.resource.type == Constants.RESOURCE_TYPES.COAL:
            return player.researched_coal()
        elif self.resource.type == Constants.RESOURCE_TYPES.URANIUM:
            return player.researched_uranium()
        else:
            return False
    def has_city(self) -> bool:
        return self.citytile is not None
    def getAdjacents(self, game_map) -> List['Cell']:
        adj_positions = self.pos.getAdjacents(game_map)
        adj_cells = []
        for adj_pos in adj_positions:
            adj_cells.append(game_map.get_cell_by_pos(adj_pos))
        return adj_cells
    def is_adjacent_to_resource(self, game_map) -> bool:
        adjacents = self.getAdjacents(game_map)
        for adj in adjacents:
            if adj.has_resource():
                return True
        return False
    def isEmpty(self) -> bool:
        return not self.has_resource() and self.citytile is None

    def __str__(self) -> str:
        return f"{self.pos}"
        
class GameMap:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.map: List[List[Cell]] = [None] * height
        for y in range(0, self.height):
            self.map[y] = [None] * width
            for x in range(0, self.width):
                self.map[y][x] = Cell(x, y)

    def get_cell_by_pos(self, pos) -> Cell:
        return self.map[pos.y][pos.x]

    def get_cell(self, x, y) -> Cell:
        return self.map[y][x]

    def _setResource(self, r_type, x, y, amount):
        """
        do not use this function, this is for internal tracking of state
        """
        cell = self.get_cell(x, y)
        cell.resource = Resource(r_type, amount)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, pos) -> int:
        return abs(pos.x - self.x) + abs(pos.y - self.y)

    def distance_to(self, pos):
        """
        Returns Manhattan (L1/grid) distance to pos
        """
        return self - pos

    def is_adjacent(self, pos):
        return (self - pos) <= 1

    def is_on_map(self, game_map: 'GameMap'):
        return (game_map.width > self.x and self.x >= 0) and (game_map.height > self.y and self.y >= 0)

    def __eq__(self, pos) -> bool:
        return self.x == pos.x and self.y == pos.y

    def equals(self, pos):
        return self == pos

    def translate(self, direction, units) -> 'Position':
        if direction == DIRECTIONS.NORTH:
            return Position(self.x, self.y - units)
        elif direction == DIRECTIONS.EAST:
            return Position(self.x + units, self.y)
        elif direction == DIRECTIONS.SOUTH:
            return Position(self.x, self.y + units)
        elif direction == DIRECTIONS.WEST:
            return Position(self.x - units, self.y)
        elif direction == DIRECTIONS.CENTER:
            return Position(self.x, self.y)

    def adjacent(self, direction) -> 'Position':
        return self.translate(direction, 1)

    def getAdjacents(self, game_map) -> List['Position']:
        positions =  [
            self.adjacent(DIRECTIONS.WEST),
            self.adjacent(DIRECTIONS.EAST),
            self.adjacent(DIRECTIONS.NORTH),
            self.adjacent(DIRECTIONS.SOUTH)
        ]
        positions_on_map = []
        for pos in positions: 
            if pos.is_on_map(game_map):
                positions_on_map.append(pos)
        return positions_on_map

    def direction_to(self, target_pos: 'Position') -> DIRECTIONS:
        """
        Return closest position to target_pos from this position
        """
        check_dirs = [
            DIRECTIONS.NORTH,
            DIRECTIONS.EAST,
            DIRECTIONS.SOUTH,
            DIRECTIONS.WEST,
        ]
        closest_dist = self.distance_to(target_pos)
        closest_dir = DIRECTIONS.CENTER
        for direction in check_dirs:
            newpos = self.translate(direction, 1)
            dist = target_pos.distance_to(newpos)
            if dist < closest_dist:
                closest_dir = direction
                closest_dist = dist
        return closest_dir

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
