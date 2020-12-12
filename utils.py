from PlayerInfo import PlayerInfo
from Map import Map
from PlayerInfo import PlayerInfo
from pprint import pprint
import actions
from typing import List


def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def move_available(current_map: Map, other_player: PlayerInfo, x, y):
    # TODO: Check how we store unpassable data
    if 0 <= x < current_map.width and 0 <= y < current_map.height:
        blocked = 'tileType' in current_map.tiles[y][x] and current_map.tiles[y][x]['tileType'] == 'BLOCKTILE'
        other_player_there = other_player.x != -1 and (other_player.x != x or other_player.y != y)
        return not blocked and not other_player_there


def can_move(current_map: Map, other_player: PlayerInfo, self_pos):
    for diff in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if move_available(current_map, other_player, self_pos[0], self_pos[1]):
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

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
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
            if not move_available(maze, other_player, node_position[0], node_position[1]) and node_position != end:
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


def direction(pos1: tuple, pos2: tuple) -> str:
    if pos1[1] == pos2[1] - 1:
        return actions.up()
    if pos1[0] == pos2[0] - 1:
        return actions.left()
    if pos1[1] == pos2[1] + 1:
        return actions.down()
    if pos1[0] == pos2[0] + 1:
        return actions.right()


def get_all_non_digged(map: Map, currpos):
    tiles = []
    for x in range(map.width):
        for y in range(map.height):
            if 'tileType' in map.tiles[y][x] \
                    and map.tiles[y][x]['tileType'] == "DIGTILE" \
                    and map.tiles[y][x]["dug"] == False:
                tiles.append((x, y))

    tiles = sorted(tiles, key=lambda digtile: dist((currpos.x, currpos.y), digtile))
    return tiles


def get_all_undiscovered_tiles(map: Map):
    tiles = []
    for x in range(map.size):
        for y in range(map.size):
            if not bool(map.tiles[y][x]):
                tiles.append((x, y))


def find_closest_coordinate(pos: tuple, tiles: List[tuple]):
    best = (-1, -1)
    best_dist = 1000
    for tile in tiles:
        if dist(pos, tile) < best_dist:
            best = tile
    return best


def get_discovery_tiles_per_direction(map: Map, currpos):
    sol = {}
    sol[actions.up()] = calc_new_tiles(map, (currpos.x, currpos.y - 1))
    sol[actions.down()] = calc_new_tiles(map, (currpos.x, currpos.y + 1))
    sol[actions.left()] = calc_new_tiles(map, (currpos.x - 1, currpos.y))
    sol[actions.right()] = calc_new_tiles(map, (currpos.x + 1, currpos.y))
    return sol


def calc_new_tiles(map: Map, pos: (int, int)):
    # calculates all new tiles that will be discovered if player mozes to pos
    if not within_bounds(map, pos):
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
