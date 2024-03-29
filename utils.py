from PlayerInfo import PlayerInfo
from Map import Map
from PlayerInfo import PlayerInfo
from pprint import pprint
import actions
from typing import List
import random

dir_to_diff = {
    actions.up(): (0, -1),
    actions.down(): (0, 1),
    actions.left(): (-1, 0),
    actions.right(): (1, 0)
}

shopping_tiles = [[10,10], [10,11], [10,12], [10,13], [10,14], [14,10], [14,11], 
            [14,12], [14,13], [14,14], [11,10], [12,10], [13,10], [11,14], [12,14], [13,14]]

def dist(pos1: tuple, pos2: tuple) -> int:
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar_dist(pos1: tuple, pos2: tuple, map: Map, other_player: PlayerInfo) -> int:
    return len(astar(map, other_player, pos1, pos2))


def add_vector(vec1: tuple, vec2: tuple) -> tuple:
    return vec1[0] + vec2[0], vec1[1] + vec2[1]


def sub_vector(vec1: tuple, vec2: tuple) -> tuple:
    return vec1[0] - vec2[0], vec1[1] - vec2[1]


def move_available(current_map: Map, other_player: PlayerInfo, pos, damage_tolerant=False, sandtrap_tolerant=False):
    # TODO: Check how we store unpassable data
    x, y = pos
    if 0 <= x < current_map.width and 0 <= y < current_map.height:
        blocked = current_map.tiles[y][x].get('tileType', None) == 'BLOCKTILE'
        player_trap = not damage_tolerant and current_map.tiles[y][x].get('trap_type', None) == 'PLAYERTRAP'
        poison_trap = not damage_tolerant and current_map.tiles[y][x].get('trap_type', None) == 'SCORPION'
        sand_trap = not sandtrap_tolerant and current_map.tiles[y][x].get('trap_type', None) == 'QUICKSAND'
        other_player_there = other_player.x != -1 and (other_player.x == x and other_player.y == y)
        return not blocked and not other_player_there and not player_trap and not poison_trap and not sand_trap


def can_move(current_map: Map, other_player: PlayerInfo, self_pos):
    for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if move_available(current_map, other_player, add_vector(self_pos, diff)):
            return True
    return False


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze: Map, other_player: PlayerInfo, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    print(start)
    print(end)

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    iter = 0

    # Loop until you find the end
    while len(open_list) > 0:

        iter += 1
        if iter == 7865:
            return None
        print(iter)

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        print(len(open_list))
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure walkable terrain
            if not move_available(maze, other_player, node_position) and node_position != end:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def move_once(current_game_state, target):
    self_info = current_game_state.self_info.player_info
    path = astar(current_game_state.map, current_game_state.other_info, (self_info['x'], self_info['y']), target)
    print("path: ", path)
    if path is None or len(path) == 1:
        print("Error, cant move arrived at target")
        return "None"
    x_diff = path[1][0] - self_info['x']
    y_diff = path[1][1] - self_info['y']
    if x_diff == 1:
        return actions.right()
    if x_diff == -1:
        return actions.left()
    if y_diff == 1:
        return actions.down()
    return actions.up()


def find_path_to(player: PlayerInfo, other_info: PlayerInfo, current_map: Map, x, y):
    path = astar(current_map, other_info, (player.x, player.y), (x, y))
    if path is None:
        return [None]
    path_wasd = []
    if path is None:
        return None
    for i in range(len(path) - 1):
        diff = (path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1])
        if diff[1] == -1:
            path_wasd.append('w')
        if diff[0] == -1:
            path_wasd.append('a')
        if diff[1] == 1:
            path_wasd.append('s')
        if diff[0] == 1:
            path_wasd.append('d')
    return path_wasd


def get_all_non_digged(map: Map, currpos: (int, int)):
    tiles = []
    for x in range(map.width):
        for y in range(map.height):
            currtile = map.tiles[y][x]
            if 'tileType' in currtile \
                    and currtile['tileType'] == "DIGTILE" \
                    and ('dug' not in currtile
                         or not currtile["dug"]):
                tiles.append((x, y))

    tiles = sorted(tiles, key=lambda digtile: dist((currpos[0], currpos[1]), digtile))
    print("digtiles: ", tiles)
    return tiles


def get_all_undiscovered_tiles(map: Map):
    tiles = []
    for x in range(map.size):
        for y in range(map.size):
            if not map.tiles[y][x]:
                tiles.append((x, y))
    return tiles


def find_closest_coordinate(pos: tuple, tiles: List[tuple], map: Map, other_player: PlayerInfo):
    best = (-1, -1)
    best_dist = 1000
    print("tiles")
    print(tiles)
    print(pos)
    for tile in tiles:
        astar_len = dist(pos, tile)
        #len(astar(map, other_player, pos, tile))
        if astar_len < best_dist:
            best = tile
            best_dist = astar_len
    return best


def get_discovery_tiles_per_direction(map: Map, curr_pos: PlayerInfo) -> dict:
    sol = dict()
    sol[actions.up()] = calc_new_tiles(map, (curr_pos.x, curr_pos.y - 1))
    sol[actions.down()] = calc_new_tiles(map, (curr_pos.x, curr_pos.y + 1))
    sol[actions.left()] = calc_new_tiles(map, (curr_pos.x - 1, curr_pos.y))
    sol[actions.right()] = calc_new_tiles(map, (curr_pos.x + 1, curr_pos.y))
    return sol


def calc_new_tiles(map: Map, pos: (int, int)):
    # calculates all new tiles that will be discovered if player mozes to pos
    if not move_available(map, PlayerInfo({}), pos):
        return -1

    new_tile_cnt = 0
    for xi in range(-3, 3, 1):
        for yi in range(-3, 3, 1):
            if abs(xi) + abs(yi) > 3:
                continue
            newx = pos[0] + xi
            newy = pos[1] + yi
            if within_bounds(map, (newx, newy)) and 'tileType' not in map.tiles[newy][newx]:
                new_tile_cnt += 1
    return new_tile_cnt


def within_bounds(map: Map, pos: (int, int)):
    return 0 <= pos[0] < map.width and 0 <= pos[1] < map.height


def random_movement_action():
    return random.choice([actions.up(), actions.down(), actions.left(), actions.right()])


def find_closest_undiscovered(map: Map, other_info: PlayerInfo, undiscovered: list, start: tuple) -> tuple:
    reached = [start]
    processed = set()
    processed.add(start)
    while len(reached) > 0:
        current = reached[0]
        del reached[0]
        for direction in actions.move_actions:
            diff = dir_to_diff[direction]
            target = add_vector(current, diff)
            if target in undiscovered:
                return target
            if target not in processed and move_available(map, other_info, target):
                reached.append(target)
                processed.add(target)


def get_next_action_towards(maze: Map, other_player: PlayerInfo, start, end):
    if other_player.x == end[0] and other_player.y == end[1] and dist((other_player.x, other_player.y), start) < 3:
        return random_movement_action()
    path = astar(maze, other_player, start, end)
    print(path)
    x_diff = path[1][0] - path[0][0]
    y_diff = path[1][1] - path[0][1]
    if x_diff == 1:
        return actions.right()
    if x_diff == -1:
        return actions.left()
    if y_diff == 1:
        return actions.down()
    return actions.up()


def get_symetric_pos(map: Map, pos: (int, int)):
    return (map.width - pos[0] - 1, map.height - pos[1] - 1)


def near_bazar(pos:PlayerInfo):
    return ((pos.x == 10 or pos.x == 14) and 10 <= pos.y <= 14) \
           or ((pos.y == 10 or pos.y == 14) and 10 <= pos.x <= 14)


def resolve_trade_action(player_totems, bazar_totems, totem_to_sell):

    player_total_cnt = 0
    player_totems_cnt = {}
    for totem in player_totems:
        if totem['totemType'] not in player_totems_cnt:
            player_totems_cnt[totem['totemType']] = 0
        player_totems_cnt[totem['totemType']] += 1
        player_total_cnt += 1

    bazar_totems_cnt = {}
    for totem in bazar_totems:
        if totem['totemType'] not in bazar_totems_cnt:
            bazar_totems_cnt[totem['totemType']] = 0
        bazar_totems_cnt[totem['totemType']] += 1

    # if player doesn't have three parts, buy the totem part to sell
    if player_total_cnt < 3:
        # try to buy unique totem part
        for totem in bazar_totems:
            if totem['totemType'] != totem_to_sell:
                continue
            return actions.buy_part(totem['id'])

        # try to buy neutral
        for totem in bazar_totems:
            if totem['totemType'] != "NEUTRAL":
                continue
            return actions.buy_part(totem['id'])

        print ("WUt2? error")

    # if player has the totem, just sell it
    if totem_to_sell in player_totems_cnt and player_totems_cnt[totem_to_sell] == 2 \
        and "NEUTRAL" in player_totems_cnt and player_totems_cnt["NEUTRAL"] == 1:
        return actions.sell_totem()

    # missing totem unique part
    if totem_to_sell not in player_totems_cnt or player_totems_cnt[totem_to_sell] != 2:
        # try to trade part of another totem for this totem part
        for totem in player_totems:
            if totem['totemType'] == "NEUTRAL" or totem['totemType'] == totem_to_sell:
                continue

            # find totem to buy
            for bazar_totem in bazar_totems:
                if bazar_totem['totemType'] == totem_to_sell:
                    return actions.trade_parts(totem['id'], bazar_totem['id'])

        # try to trade NEUTRAL for this totem part
        for totem in player_totems:
            if totem['totemType'] != "NEUTRAL":
                continue

            # find totem to buy
            for bazar_totem in bazar_totems:
                if bazar_totem['totemType'] == totem_to_sell:
                    return actions.trade_parts(totem['id'], bazar_totem['id'])

    # missing totem neutral part
    if totem_to_sell in player_totems_cnt and player_totems_cnt[totem_to_sell] == 2 and \
        "NEUTRAL" not in player_totems_cnt:

        # find the part not needed
        for totem in player_totems:
            if totem['totemType'] == totem_to_sell:
                continue

            # find totem to buy
            for bazar_totem in bazar_totems:
                if bazar_totem['totemType'] == "NEUTRAL":
                    return actions.trade_parts(totem['id'], bazar_totem['id'])

    print("WUT? error!")




