import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
#
def set_weights(st):
    weights = [1,1,1,1]
    for i in range(4):
        if st[i]>0: weights[i] = 0
    return weights
def move_value (course,pos):
    mv = [1,2,3,2]
    if course[0] == "G":
        mv = [0,0,0,0]
        return mv
    if course[pos+1] == "#":
            mv[0]=-3
            mv[1] = -3
            mv[2] = -3
            mv[3] = 2
            return mv
    if course[pos+2] == "#":
            mv[0] = 1
            mv[1] = -2
            mv[2] = -2
            mv[3] = -2
            return mv
    if course[pos+3] == "#":
            mv[0] = 1
            mv[1] = 2
            mv[2] = -1
            mv[3] = 2
            return mv
    return mv



player_idx = int(input())
nb_games = int(input())
move_list = ["left","down","right","up"]


# game loop
while True:
    output = ""
    ppos = []
    gpu = []
    st = []
    gw= [1,1,1,1]
    for i in range(3):
        score_info = input()
    for i in range(nb_games):
        inputs = input().split()
        gpu.append(inputs[0]+"xxx")
        ppos.append(int(inputs[player_idx+1]))
        st.append(int(inputs[player_idx+4]))

        

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print("Debug messages...", file=sys.stderr, flush=True)
    print("Player idx..."+str(player_idx), file=sys.stderr, flush=True)
    print("course 0..."+str(gpu[0]), file=sys.stderr, flush=True)
    print("game weight..."+str(gw), file=sys.stderr, flush=True)
    # print("next for game 0 :" + str(gpu[0][ppos[0]+1]), file=sys.stderr, flush=True)
    move_v0 = move_value(gpu[0],ppos[0])
    move_v1 = move_value(gpu[1],ppos[1])
    move_v2 = move_value(gpu[2],ppos[2])
    move_v3 = move_value(gpu[3],ppos[3])
    print("positions in games ..."+str(ppos), file=sys.stderr, flush=True)
    
    print("move value for game 0 ..."+str(move_v0), file=sys.stderr, flush=True)
    print("move value for game 1 ..."+str(move_v1), file=sys.stderr, flush=True)
    print("move value for game 2 ..."+str(move_v2), file=sys.stderr, flush=True)
    print("move value for game 3 ..."+str(move_v3), file=sys.stderr, flush=True)
    gw = set_weights(st)
    print("weights ..."+str(gw), file=sys.stderr, flush=True)
    move_values = [0,0,0,0]
    for i in range(4):
        move_values[i] = (move_v0[i]*gw[0])+ (move_v1[i]*gw[1])+(move_v2[i]*gw[2])+(move_v3[i]*gw[3])
    print("move value overall......."+str(move_values), file=sys.stderr, flush=True)
    best_move_score = max(move_values)
    best_move_index = move_values.index(best_move_score)
    best_move = move_list[best_move_index]
    output = best_move
    print (output)
    
