import logging
from lux.game_map import Cell, Position
from typing import Tuple, List
from lux.constants import Constants
from commonFunctions import posTupleFromTile

def directionToObjective(pos: Position, objective: Cell, tiles_to_avoid: List[Cell] = []) -> Constants.DIRECTIONS:
    pos_to_avoid = [posTupleFromTile(tile) for tile in tiles_to_avoid]
    can_reach, direction = canReachObjectiveFromPos((pos.x, pos.y), posTupleFromTile(objective), pos_to_avoid)
    if can_reach:
        return direction

def canReachObjectiveFromPosByMovingY(pos: Tuple[int, int], obj_pos: Tuple[int, int], pos_to_avoid: List[Tuple[int, int]] = [], allowBackTravel = False) -> bool:
    if pos[1] > obj_pos[1]:
        new_pos = (pos[0], pos[1] - 1)
        dir = Constants.DIRECTIONS.NORTH
    else:
        new_pos = (pos[0], pos[1] + 1)
        dir = Constants.DIRECTIONS.SOUTH
    can_reach, _ = canReachObjectiveFromPos(new_pos, obj_pos, pos_to_avoid)
    return (can_reach, dir)
    
def canReachObjectiveFromPosByMovingX(pos: Tuple[int, int], obj_pos: Tuple[int, int], pos_to_avoid: List[Tuple[int, int]] = [], allowBackTravel = False) -> Tuple[bool, Constants.DIRECTIONS]:
    #try move x first
    if pos[0] > obj_pos[0]:
        new_pos = (pos[0] - 1, pos[1])
        dir = Constants.DIRECTIONS.WEST
    else:
        new_pos = (pos[0] + 1, pos[1])
        dir = Constants.DIRECTIONS.EAST
    can_reach, _ = canReachObjectiveFromPos(new_pos, obj_pos, pos_to_avoid)
    return (can_reach, dir)

def XthenY(pos, obj_pos, pos_to_avoid):
    can_reach, dir = canReachObjectiveFromPosByMovingX(pos, obj_pos, pos_to_avoid)
    if can_reach:
        return (True, dir)
    else:
        can_reach, dir = canReachObjectiveFromPosByMovingY(pos, obj_pos, pos_to_avoid)
        if can_reach:
            return (True, dir)
    logging.info(" Unable to find path")
    return (False, Constants.DIRECTIONS.CENTER)

def YthenX(pos, obj_pos, pos_to_avoid):
    can_reach, dir = canReachObjectiveFromPosByMovingY(pos, obj_pos, pos_to_avoid)
    if can_reach:
        return (True, dir)
    else:
        can_reach, dir = canReachObjectiveFromPosByMovingX(pos, obj_pos, pos_to_avoid)
        if can_reach:
            return (True, dir)
    logging.info(" Unable to find path")
    return (False, Constants.DIRECTIONS.CENTER)

def canReachObjectiveFromPos(pos: Tuple[int, int], obj_pos: Tuple[int, int], pos_to_avoid: List[Tuple[int, int]] = [], allowBackTravel = False) -> Tuple[bool, Constants.DIRECTIONS]:

    if pos in pos_to_avoid:
        #logging.info(" Avoid")
        return (False, Constants.DIRECTIONS.CENTER)
    
    x_dif = pos[0] - obj_pos[0]
    y_dif = pos[1] - obj_pos[1]

    if x_dif == 0 and y_dif == 0:
        return (True, Constants.DIRECTIONS.CENTER)

    if abs(x_dif) >= abs(y_dif):
        return XthenY(pos, obj_pos, pos_to_avoid)
    else:
        return YthenX(pos, obj_pos, pos_to_avoid)

    # Allow back travel here
