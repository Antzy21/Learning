import logging
from math import inf
from typing import Optional, Tuple, List
from commonFunctions import *
from lux.game_map import DIRECTIONS, Cell, Position

ExploredPosDistIndex = Tuple[Position, int, int]

def findPathFrom(explored_pos_dists_and_dirs, target, direction_list = []) -> List[DIRECTIONS]:
    if target[2] is None: # back to origin of search
        return direction_list
    origin = explored_pos_dists_and_dirs[target[2]]
    if target[0] == origin[0].adjacent(DIRECTIONS.WEST):
        direction_list.append(DIRECTIONS.WEST)
    elif target[0] == origin[0].adjacent(DIRECTIONS.EAST):
        direction_list.append(DIRECTIONS.EAST)
    elif target[0] == origin[0].adjacent(DIRECTIONS.NORTH):
        direction_list.append(DIRECTIONS.NORTH)
    elif target[0] == origin[0].adjacent(DIRECTIONS.SOUTH):
        direction_list.append(DIRECTIONS.SOUTH)
    return findPathFrom(explored_pos_dists_and_dirs, origin, direction_list)

def tryFindPath(obj_positions: List[PosTuple], explored_pos_dists_and_dirs: List[ExploredPosDistIndex]) -> Optional[Tuple[PosTuple, List[DIRECTIONS]]]:
    for explored_pos_dist_and_dir in explored_pos_dists_and_dirs:
        if explored_pos_dist_and_dir[0] in obj_positions:
            return (explored_pos_dist_and_dir[0], findPathFrom(explored_pos_dists_and_dirs, explored_pos_dist_and_dir, []))
    return None

def nearestByAvoid(game_map, pos: Position, obj_tiles: List[Cell], avoid_tiles = List[Cell]) -> List[DIRECTIONS]:
    obj_positions = [o.pos for o in obj_tiles]

    if pos in obj_positions:
        return [DIRECTIONS.CENTER]

    avoid_positions = [t.pos for t in avoid_tiles]
    explored_pos_dists_indexs: List[ExploredPosDistIndex] = []
    explored_pos_dists_indexs.append((pos, 0, None))

    current_depth = 0
    frontier_positions = [(pos, 0)]
    result = None

    while result is None:
        current_depth += 1
        if current_depth > 10:
            logging.error(" Warning: Large depth count")
            return [DIRECTIONS.CENTER]

        new_positions = []
        explored_positions = [x[0] for x in explored_pos_dists_indexs]
        for front_pos, origin_index in frontier_positions:
            explore_new = front_pos.getAdjacents(game_map)
            for new_pos in explore_new:
                if new_pos not in explored_positions and new_pos not in avoid_positions:
                    new_positions.append((new_pos, len(explored_pos_dists_indexs)))
                    explored_positions.append(new_pos)
                    explored_pos_dists_indexs.append((new_pos, current_depth, origin_index))
        frontier_positions = new_positions
        result = tryFindPath(obj_positions, explored_pos_dists_indexs)

    if result is None:
        logging.error("Has not reached objective. While Loop failed")
    
    nearest, path_to_objective = result
    #posPath = positionPathFromDirPath(path_to_objective, pos)
    #logging.info(f"Path:{posPath}")
    
    return path_to_objective

def nearest(unit, objectiveTiles: List[Cell]) -> Tuple[Optional[Cell], float]:
    closest_dist = inf
    closest_tile = None
    for tile in objectiveTiles:
        dist = tile.pos.distance_to(unit.pos)
        if dist < closest_dist:
            closest_dist = dist
            closest_tile = tile
    return (closest_tile, closest_dist)

def directionToNearest(game_map, unit, objectiveTiles: List[Cell], tiles_to_avoid: List[Cell] = []) -> DIRECTIONS:
    path = nearestByAvoid(game_map, unit.pos, objectiveTiles, tiles_to_avoid)
    if path is None:
        logging.error(f"No path. Unit: {unit.pos}.")
        return DIRECTIONS.CENTER
    immediate_direction = path[-1]
    if not validateDirection(immediate_direction):
        logging.error("Direction invalid. Unit: {unit.pos}.")
        return DIRECTIONS.CENTER
    return immediate_direction

def nearestCity(player, unit, city_tiles: List[Cell]):
    nearest_city_tile, _ = nearest(unit, city_tiles)
    if nearest_city_tile is None:
        return None
    return player.cities[nearest_city_tile.cityid]
