from utils import *
import math


def get_chooser(depth):
    def temp(this_game_map: np.ndarray):
        return choose(this_game_map, depth)

    return temp


def choose(this_game_map: np.ndarray, depth):
    # return best_choice
    best_score, best_choice = maximizer(this_game_map, depth, 1)
    return best_choice
    #best_choice, v = max_value(this_game_map, depth)
    #return best_choice


def max_value(this_game_map: np.ndarray, depth):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    if depth == 0 or len(choices) == 0:
        return None, get_two_side_score(this_game_map)
    v = -10 ** 10
    max_choice = None
    for choice in choices:
        this_game_map[choice] = 1
        temp, child_value = max_value(-this_game_map.copy(), depth - 1)
        if v < -child_value:
            v = -child_value
            max_choice = choice
        this_game_map[choice] = 0
    return max_choice, v
def maximizer(this_game_map: np.ndarray, depth, itter):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    best_score = -1000000000
    best_choice = None
    for choice in choices:
        this_game_map[choice] = 1
        score = get_two_side_score(this_game_map)
        this_game_map_copy = this_game_map.copy()
        if(itter!=depth):
            score, c = minimizer(this_game_map_copy, depth, itter+1)
        this_game_map[choice] = 0
        if(best_score < score):
            best_score = score
            best_choice = choice
    return best_score, best_choice

def minimizer(this_game_map: np.ndarray, depth, itter):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    worst_score = 1000000000
    worst_choice = None
    for choice in choices:
        this_game_map[choice] = -1
        score = get_two_side_score(this_game_map)
        this_game_map_copy = this_game_map.copy()
        if(itter!=depth):
            score, c = maximizer(this_game_map_copy, depth, itter+1)
        this_game_map[choice] = 0
        if(worst_score > score):
            worst_score = score
            worst_choice = choice
    return worst_score, worst_choice
