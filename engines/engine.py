import sys

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
game_state_data = open(game_state_file, "r").read().close()
game_actions_data = open(game_actions_file, "r").read().close()


## sooo... most important stuff is in game_state_data. 

print("FOLD", flush=True)

# cleanup, logging
print("long-term logging", file=sys.stderr)
