from queue import Queue  # queue will be used for implementing BFS
import sys
import heapq
import time

# I have used a python list for state representation

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]  # goal state defined
initial_state = []
path_cost = 0
user_input = sys.argv[1]
initial_state_str = list(user_input)

for i in initial_state_str:
    initial_state.append(int(i))

'''for i in range(0, 9):
    num = int(input())
    initial_state.append(num)  # initial state from user input'''


def is_goal_state(state):  # function to check if current state is the goal state
    return state == goal_state


def get_next_states(state):
    empty_space_index = state.index(0)  # find the index of the empty space which is 0
    next_states = []  # create a list of possible next states

    # define the dimensions of the puzzle
    rows = 3
    cols = 3

    # define the row and column of the empty space
    empty_row = empty_space_index // cols
    empty_col = empty_space_index % cols

    # check and add possible moves (up, down, left, right)
    if empty_row > 0:
        # move up
        next_index = empty_space_index - cols
        next_state = state[:]
        next_state[empty_space_index], next_state[next_index] = next_state[next_index], next_state[empty_space_index]
        next_states.append(next_state)

    if empty_row < rows - 1:
        # move down
        next_index = empty_space_index + cols
        next_state = state[:]
        next_state[empty_space_index], next_state[next_index] = next_state[next_index], next_state[empty_space_index]
        next_states.append(next_state)

    if empty_col > 0:
        # move left
        next_index = empty_space_index - 1
        next_state = state[:]
        next_state[empty_space_index], next_state[next_index] = next_state[next_index], next_state[empty_space_index]
        next_states.append(next_state)

    if empty_col < cols - 1:
        # move right
        next_index = empty_space_index + 1
        next_state = state[:]
        next_state[empty_space_index], next_state[next_index] = next_state[next_index], next_state[empty_space_index]
        next_states.append(next_state)

    return next_states


# function to get action moves
def get_action(current_state, next_state):
    # index of the empty space in both states
    current_empty_index = current_state.index(0)
    next_empty_index = next_state.index(0)

    # calculating the row and column of the empty space in current and next state
    current_row, current_col = divmod(current_empty_index, 3)
    next_row, next_col = divmod(next_empty_index, 3)

    # determining the action based on the movement of the empty space (0)
    if current_row < next_row:
        return "Down"
    elif current_row > next_row:
        return "Up"
    elif current_col < next_col:
        return "Right"
    elif current_col > next_col:
        return "Left"
    return None


# function to print list as 3x3 matrix
def visualize(state):
    for i in range(3):  # loop iterates over the rows of the state
        for j in range(3):  # loop iterates over the columns of the state
            print(state[i * 3 + j], end=" ")
        print()
    print()


def breadth_first(initial_state):
    frontier = Queue()  # queue to store states
    visited = set()  # storing visited nodes

    frontier.put(
        (initial_state, [], []))  # adding initial state to queue, an empty list for path and an empty list for actions

    while not frontier.empty():
        current_state, path, actions = frontier.get()
        visited.add(tuple(current_state))  # current states added as tuple

        if is_goal_state(current_state):  # checks if the current state is the goal state
            return path, actions  # returns path and action if it is the goal state

        next_states = get_next_states(current_state)  # generate possible next states

        for next_state in next_states:  # a loop to explore each possible next state
            if tuple(next_state) not in visited:  # checks if next state is already visited
                new_path = path + [next_state]
                new_actions = actions + [get_action(current_state, next_state)]
                frontier.put((next_state, new_path, new_actions))  # adds next states to queue

    return None  # when no solution found


start1 = time.time()
result = breadth_first(initial_state)  # calling bfs function
end1 = time.time()
print("Breadth First Search")
if result is None:
    print("No solution found.")
    #visualize(initial_state)
    #print()
else:
    #print("Solution found:")
    #for i, state in enumerate(result[0]):
        #print(f"Step {i}:")
        #path_cost += 1
        #visualize(state)
        #print()
    print("Action moves: " + str(result[1]))
    #print("Path cost is ", path_cost)
    print("Time taken for Breadth First Search is ", (end1 - start1))


def iterative_deepening(initial_state):
    depth_limit = 0
    while True:
        result = depth_limited_search(initial_state, depth_limit)
        if result is not None:
            return result
        depth_limit += 1


def depth_limited_search(state, depth_limit):
    return recursive_depth_limited_search(state, depth_limit, [], [])


def recursive_depth_limited_search(state, depth_limit, path, actions):
    if depth_limit == 0:
        if is_goal_state(state):
            return path, actions
        else:
            return None
    elif is_goal_state(state):
        return path, actions
    else:
        next_states = get_next_states(state)
        for next_state in next_states:
            result = recursive_depth_limited_search(next_state, depth_limit - 1, path + [next_state],
                                                    actions + [get_action(state, next_state)])
            if result is not None:
                return result
    return None


start2 = time.time()
result = iterative_deepening(initial_state)
end2 = time.time()
print("Iterative Deepening Search")
if result is None:
    print("No solution found.")
    #visualize(initial_state)
    #print()
else:
    path_cost = 0
    #print("Solution found:")
    #for i, state in enumerate(result[0]):
        #print(f"Step {i}:")
        #path_cost += 1
        #visualize(state)
        #print()
    print("Action moves: " + str(result[1]))
    #print("Path cost is ", path_cost)
    print("Time taken for Iterative Deepening Search is ", (end2 - start2))


def num_wrong_tiles(state):
    # counts the number of tiles in the wrong location
    num_wrong = 0
    for i in range(len(state)):
        if state[i] != goal_state[i] and state[
            i] != 0:  # check if the tile is not in the correct location or is not the empty tile (0)
            num_wrong += 1
    return num_wrong


def manhattan_distance(state):
    # calculates the total manhattan distance for all tiles to move to their correct locations
    total_distance = 0
    for i in range(len(state)):
        if state[i] != 0:  # exclude the empty tile (0) from calculations
            row, col = divmod(i, 3)
            target_row, target_col = divmod(state[i], 3)
            total_distance += abs(row - target_row) + abs(col - target_col)
    return total_distance


def a_star_search(initial_state):
    # visited = set()
    priority_queue = []  # priority queue to store states along with their estimated costs.

    # path_cost = {}
    priority_queue = [(manhattan_distance(initial_state), initial_state)]
    path_cost = {tuple(initial_state): 0}  # dictionary to track the cost to reach each state.
    actions = {tuple(initial_state): []}
    state_path = {tuple(initial_state): []}

    while priority_queue:
        current_priority, current_state = heapq.heappop(priority_queue)
        current_state_tuple = tuple(current_state)
        if current_state == goal_state:

            path = []
            action_moves = []
            state_sequence = state_path[current_state_tuple]
            actions_sequence = actions[current_state_tuple]

            while current_state != initial_state:
                path.append(current_state)
                action_moves.append(actions_sequence[-1])
                current_state = state_sequence.pop()
                actions_sequence.pop()

            path.append(initial_state)
            path.reverse()
            action_moves.reverse()

            return path, action_moves
        next_states = get_next_states(current_state)

        for next_state in next_states:

            new_cost = path_cost[current_state_tuple] + 1
            next_state_tuple = tuple(next_state)

            if next_state_tuple not in path_cost or new_cost < path_cost[next_state_tuple]:
                #update the cost to reach next_state
                path_cost[next_state_tuple] = new_cost

                #priority for next_state
                next_priority = new_cost + manhattan_distance(next_state)

                #push next_state into the priority queue

                heapq.heappush(priority_queue, (next_priority, next_state))
                actions[next_state_tuple] = actions[current_state_tuple] + [get_action(current_state, next_state)]
                state_path[next_state_tuple] = state_path[current_state_tuple] + [current_state]

    return None  # No solution found


start3 = time.time()
result = a_star_search(initial_state)
end3 = time.time()

if result is None:
    print("No solution found.")
    #visualize(initial_state)
    #print()
else:

    #print("Solution found:")
    #for i, state in enumerate(result[0]):
        #print(f"Step {i}:")

        #visualize(state)
        #print()
    print("Action moves: " + str(result[1]))
    timee = end3 - start3
    print("Time taken for A* with manhattan distance ", timee)


def a_star_search(initial_state):
    # visited = set()
    priority_queue = []  # priority queue to store states along with their estimated costs.

    # path_cost = {}
    priority_queue = [(num_wrong_tiles(initial_state), initial_state)]
    path_cost = {tuple(initial_state): 0}  # dictionary to track the cost to reach each state.
    actions = {tuple(initial_state): []}
    state_path = {tuple(initial_state): []}

    while priority_queue:
        current_priority, current_state = heapq.heappop(priority_queue)
        current_state_tuple = tuple(current_state)
        if current_state == goal_state:

            path = []
            action_moves = []
            state_sequence = state_path[current_state_tuple]
            actions_sequence = actions[current_state_tuple]

            while current_state != initial_state:
                path.append(current_state)
                action_moves.append(actions_sequence[-1])
                current_state = state_sequence.pop()
                actions_sequence.pop()

            path.append(initial_state)
            path.reverse()
            action_moves.reverse()

            return path, action_moves
        next_states = get_next_states(current_state)

        for next_state in next_states:

            new_cost = path_cost[current_state_tuple] + 1
            next_state_tuple = tuple(next_state)

            if next_state_tuple not in path_cost or new_cost < path_cost[next_state_tuple]:
                #update the cost to reach next_state
                path_cost[next_state_tuple] = new_cost

                #priority for next_state
                next_priority = new_cost + num_wrong_tiles(next_state)

                #push next_state into the priority queue

                heapq.heappush(priority_queue, (next_priority, next_state))
                actions[next_state_tuple] = actions[current_state_tuple] + [get_action(current_state, next_state)]
                state_path[next_state_tuple] = state_path[current_state_tuple] + [current_state]
    return None  # No solution found


start4 = time.time()
result = a_star_search(initial_state)
end4 = time.time()

if result is None:
    print("No solution found.")
    #visualize(initial_state)
    #print()
else:

    #print("Solution found:")
    #for i, state in enumerate(result[0]):
        #print(f"Step {i}:")

        #visualize(state)
        #print()
    print("Action moves: " + str(result[1]))

    print("Time taken for A* with number of wrong tiles as heuristic cost ", (end4 - start4))