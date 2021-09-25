import logging
import json

from flask import request, jsonify
import requests

from codeitsuisse import app

ARENA_END_POINT = "https://cis2021-arena.herokuapp.com/"

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # get the battleId
    battleId = data["battleId"]
    logging.info("data" + str(data)+ " battleId"+ str(battleId))
    code = {
        "NW": 0, "N": 1, "NE": 2,
        "W" : 3, "C": 4, "E" : 5,
        "SW": 6, "S": 7, "SE": 8
    }  
    board = [0, 0, 0, 
             0, 0, 0, 
             0, 0, 0]
    game_end = False
    s = requests.Session()
    res = s.get(ARENA_END_POINT + "/tic-tac-toe/start/" + battleId)
    logging.info(res.json()["id"])
    # initial event
        # "O" goes first
    if res.json()["youAre"] == "O":
        first = True
    elif res.json()["youAre"] == "X":
        first = False
    
    if not first:
        res = s.get(ARENA_END_POINT + "/tic-tac-toe/start/" + battleId).json()
        board[code[res["position"]]] = 1 if first else 2

    while game_end != True:
        res = s.post(ARENA_END_POINT + "/tic-tac-toe/play/" + battleId, {"action": 'C'}).json()
        game_end = True
        # try:
        #     if res["action"] == "putSymbol":
                
            
    
    return json.dumps(res)

def input_is_valid(input, board):
    try:
        if board[input] == 0:
            return True
        else:
            return False
    except KeyError:
        return False    
    
# @app.route('/tic-tac-toe', methods=['POST'])
# def get_battle_id():
#     data = request.get_json()
#     logging.info("battle id: {}".format(data))
#     battleId = data.get("battleId")
#     return battleId
    

# @app.route('https://cis2021-arena.herokuapp.com/tic-tac-toe/start/<battleId>', methods=['GET'])
# def event_stream(battleId):
#     return f'Event {battleId}'

# @app.route('https://cis2021-arena.herokuapp.com/tic-tac-toe/start/<battleId>', methods=['POST'])

