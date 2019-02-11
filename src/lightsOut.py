import copy
import os
import sys


def run():
    """ Main function to run
    Takes the switches and connections from stdin and
    creates a matrix to be solved.
    """
    buttons = None
    connections = None
    for line in sys.stdin:
        if(buttons == None):
            buttons = list(line.strip("\n").replace(" ", ""))
        else:
            connections = line.split()
    matrix = createMatrix(buttons, connections)
    solution = solve(matrix)
    if(solution != None):
        userOutput(solution, matrix, buttons, connections)
    else:
        print(*buttons)
        print(*connections)
        print("Has no solution")


def userOutput(solution, matrix, buttons, connections):
    """Creates a user friendly out for the solution
    Args:
        solution: array of switches to push
    """
    print(*buttons)
    print(*connections)
    print("Solution:")
    for i in range(len(solution)):
        switch(solution[i], matrix)
        print("Step {}:".format(i + 1))
        print("Press the {} switch".format(buttons[solution[i]]))
        for b in range(len(buttons)):
            if(matrix[b][b] == 1):
                print("{}:ON".format(buttons[b]))
            else:
                print("{}:OFF".format(buttons[b]))


def createMatrix(buttons, connections):
    switches = {}
    matrix = []
    for x in range(len(buttons)):
        switches[buttons[x]] = x
        matrix.insert(x, [])
        for y in range(len(buttons)):
            matrix[x].append(None)
    for s in switches.values():
        matrix[s][s] = 1

    for c in connections:
        x = switches[c[0]]
        y = switches[c[1]]
        matrix[x][y] = 1
    return matrix


def switch(i, matrix):
    connections = []
    for x in range(len(matrix[i])):
        if(matrix[i][x] != None):
            connections.append(x)
    for x in range(len(matrix)):
        for y in connections:
            if(matrix[x][y] != None):
                if(matrix[x][y] == 1):
                    matrix[x][y] = 0
                else:
                    matrix[x][y] = 1
    return matrix


def solve(matrix):
    queue = []
    for x in range(len(matrix)):
        queue.append((copy.deepcopy(matrix), []))
    while(queue):
        currMatrix = queue.pop(0)
        for x in range(len(matrix)):
            if(x in currMatrix[1]):
                continue
            newMatrix = (switch(x, copy.deepcopy(
                currMatrix[0])), copy.deepcopy(currMatrix[1]))
            newMatrix[1].append(x)
            if(sumM(newMatrix[0]) == 0):
                return newMatrix[1]
            else:
                queue.append(newMatrix)


def sumM(matrix):
    t = 0
    for x in matrix:
        for y in x:
            if not (y == None):
                t += y
    return t


if __name__ == "__main__":
    run()
