import random
import copy

def init_st_generator(arr, n):
    for i in range(n):
        col = [random.randint(0, n-1), i]
        arr.append(col)
    return arr

def heuristic(arr, n):
    score = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i][0] == arr[j][0] or abs(arr[i][0] - arr[j][0]) == abs(arr[i][1] - arr[j][1]):
                score += 1
    return score

class queens_problem_state:
    def __init__(self, lst):
        self.lst = lst
        self.score = heuristic(lst, len(lst))

    def display(self):
        print("state : ", self.lst, "   score : ", self.score)

def problem_solver(init_st, n):
    waiting = [queens_problem_state(init_st)]
    visited = set()

    while waiting:
        current = waiting.pop(0)
        visited.add(tuple(map(tuple, current.lst)))
        if current.score == 0:
            current.display()
            return True

        for i in range(n):
            for j in range(n):
                if i != current.lst[j][0]:
                    temp = copy.deepcopy(current.lst)
                    temp[j][0] = i
                    new_state = queens_problem_state(temp)
                    if tuple(map(tuple, new_state.lst)) not in visited:
                        waiting.append(new_state)

    return False

init_st = []
init_st_generator(init_st, 4)
print("---INITIAL---")
print("state : ", init_st, "    score : ", heuristic(init_st, 4))
print("---FINAL---")
problem_solver(init_st, 4)
