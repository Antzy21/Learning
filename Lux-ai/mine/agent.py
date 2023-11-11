from lux.game import Game
from getTiles import getTilesDict, getAdjacentToCityTiles, getInverse
import logging
from commonFunctions import posFromTile, snd
from actions import *

logging.basicConfig(filename='../log-luxai.log', encoding='utf-8', level=logging.DEBUG, filemode='w')

game_state = None
unitMaxCargo = 100
logInfo = ""

def shouldCreateNewWorker(player, tiles): 
    return len(player.units) == 0 or len(tiles['city'])/(len(player.units)**2) >= 2

def agent(observation, configuration):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player
    else:
        game_state._update(observation["updates"])
    
    actions = []
    if game_state.is_night():
        daynight = "Night: "
    elif game_state.is_near_night():
        daynight = "Twilight: "
    else:
        daynight = "Day: "

    logging.info(f"---- {daynight} {game_state.turn} ----")
    ### AI Code goes down here! ### 
    player = game_state.players[observation.player]
    opponent = game_state.players[(observation.player + 1) % 2]

    tiles = getTilesDict(game_state, player, opponent)

    # we iterate over all our units and do something with them
    for unit in player.units:
        #logging.info(onlyFarmersNow)
        if unit.is_worker() and unit.can_act():
            if unit.id in ["u_1", "u_2"] or len(player.units) == 1:
                action = resolveWorkerAction(unit, player, opponent, tiles, game_state)
                actions.append(action)
            else:
                action = farmerAction(unit, player, tiles, game_state)
                actions.append(action)

    # you can add debug annotations using the functions in the annotate object
    # actions.append(annotate.circle(0, 0))
    for _, city in player.cities.items():
        if shouldCreateNewWorker(player, tiles):
            action = createWorker(city, game_state)
        else:
            action = research(city, game_state)
        if action is not None:
            actions.append(action)

    return actions