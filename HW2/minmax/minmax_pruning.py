from utils import *
import math


def get_chooser(depth):
    def temp(this_game_map: np.ndarray):
        return choose(this_game_map, depth)

    return temp


def choose(this_game_map: np.ndarray, depth):
    # return best_choice
    return max_value(this_game_map, depth, -10 ** 10, -10 ** 10)[0]


def max_value(this_game_map: np.ndarray, depth, alpha, beta):
    available_points = get_available_points(this_game_map)
    choices = list(zip(*np.where(available_points)))
    if depth == 0 or len(choices) == 0:
        return None, get_two_side_score(this_game_map)
    v = -10 ** 10
    max_choice = None
    for choice in choices:
        this_game_map[choice] = 1
        temp, child_value = max_value(-this_game_map.copy(), depth - 1, beta, alpha)
        this_game_map[choice] = 0
        if v < -child_value:
            v = -child_value
            max_choice = choice
        if v > -beta:
            return choice, v
        alpha = max(alpha, v)
    return max_choice, v
