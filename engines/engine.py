import sys
from pokerkit import *
from phevaluator.evaluator import evaluate_cards
import json


if len(sys.argv) < 3:
    raise Exception("Unexpected invocation")

if sys.argv[1] == "START":
    print("squid poker bot")
    exit(0)

if len(sys.argv) < 8:
    raise Exception("Unexpected invocation")

executable_name = sys.argv[0]
min_bet_to_not_fold = int(sys.argv[1])
turn_time_ms = int(sys.argv[2])
time_bank_ms = int(sys.argv[3])
game_params_file = sys.argv[4]
game_state_file = sys.argv[5]
game_actions_file = sys.argv[6]
temp_dir_path = sys.argv[7]

game_params_data = open(game_params_file, "r").read().close()
game_params_data = json.loads(game_params_data)
"""
{
    "engines": [<engine names>],
    "small_blind": <integer>,
    "big_blind": <integer>,
    "ante": <integer>,
    "starting_funds": <integer>,
    "starting_time_bank": <integer>
}"""
game_state_data = open(game_state_file, "r").read().close()
game_state_data = json.loads(game_state_data)
"""{
    "you_index": <number>,
    "funds": [<unbet funds>],
    "bets": [<current bets>],
    "folds": [<current fold states>],
    "time_banks": [<time banks>],
    "your_hand": [<two cards>],
    "revealed_cards": [<revealed cards>],
    "small_blind": <small blind index>,
    "big_blind": <big blind index>
}"""

#game_actions_data = open(game_actions_file, "r").read().close()


## sooo... most important stuff is in game_state_data. 

def call():
    print("CALL", flush=True)
def raise_amount(amount):
    print(f"RAISE {amount}", flush=True)
def fold():
    print("FOLD", flush=True)

def evaluate_hand():
    hand = game_state_data["your_hand"] + game_state_data["revealed_cards"]
    return evaluate_cards(hand)

print(evaluate_hand())

# cleanup, logging
#print("long-term logging", file=sys.stderr)
