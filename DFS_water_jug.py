# This program shows the dfs algorithm to find the goal state in the water jug problem

import sys
frontier = []
explored_set = []
graph = {}

def expand(node, left_jug_capacity, right_jug_capacity):
    nodes = []


    left_jug = node[0]
    right_jug = node[1]
    left_jug = left_jug_capacity

    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)


    left_jug = node[0]
    right_jug = node[1]
    right_jug = right_jug_capacity

    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)

    left_jug = node[0]
    right_jug = node[1]
    left_jug = 0

    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)


    left_jug = node[0]
    right_jug = node[1]
    right_jug = 0

    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)


    left_jug = node[0]
    right_jug = node[1]
    if left_jug == left_jug_capacity:
        pass
    else:
        empty_room = left_jug_capacity - left_jug
        if empty_room <= right_jug:
            left_jug += empty_room
            right_jug -= empty_room 
        else:
            left_jug += right_jug
            right_jug = 0

    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)

    left_jug = node[0]
    right_jug = node[1]
    if right_jug == right_jug_capacity:
        pass
    else:
        empty_room = right_jug_capacity - right_jug
        if empty_room <= left_jug:
            right_jug += empty_room
            left_jug -= empty_room 
        else:
            right_jug += left_jug
            left_jug = 0
    
    new_node = []
    new_node.append(left_jug)
    new_node.append(right_jug)
    nodes.append(new_node)

    return nodes

def display(left_jug, right_jug):
    return f"<{left_jug} , {right_jug}>"
def main(left_jug_capacity, right_jug_capacity, left_jug, right_jug, left_jug_end, right_jug_end):
    # Geting the capacity of the left and right jug
    

    # Displaying the initial states of the game
    print(f"current state = {display(left_jug=left_jug, right_jug=right_jug)}")

    initial_state = []
    initial_state.append(left_jug)
    initial_state.append(right_jug)

    frontier.append(initial_state)
    
    end_game = 0
    while (end_game == 0):

        # If frontier is empty then stop
        if len(frontier) == 0:
            break

        node = frontier[-1]

        if node[0] == left_jug_end and node[1] == right_jug_end:
            break

        frontier.pop(-1)

        explored_set.append(node)

        expaded_result = expand(node, left_jug_capacity, right_jug_capacity)

        for i in expaded_result:
            if i not in frontier and i not in explored_set:
                frontier.append(i)
                graph[str(node)] = i
        print(frontier)

        # Display the desired state you want to reach
        # print(f"End state = {display(left_jug=left_jug_end, right_jug=right_jug_end)}")
        
        # print(display(left_jug=node[0], right_jug=node[1]))
        if left_jug == left_jug_end and right_jug == right_jug_end:
            end_game = 1

# left_jug_capacity = int(input("Enter the capacity of the left jug : "))
# right_jug_capacity = int(input("Enter the capacity of the right jug : "))

# # Getting the initial state of the jugs
# left_jug = int(input("Enter the initial liquid of the left jug : "))
# right_jug = int(input("Enter the initial liquid of the right jug : "))

# # Getting the final state of the jugs
# left_jug_end = int(input("Enter the final state of the left jug : "))
# right_jug_end = int(input("Enter the final state of the right jug : "))
# if __name__ == "__main()__":
main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
print(graph)