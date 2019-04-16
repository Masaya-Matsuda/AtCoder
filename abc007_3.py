import sys
from collections import deque

class Maze:

    def __init__(self, R, C, input_list, start, goal):
        self.R = R
        self.C = C
        self.maze_list = input_list
        self.goal = goal
        self.count = 0
        self.path = deque([])
        self.path.append([start[0], start[1], 0])

        #{"y_x":count, ....}
        self.visited_dict = {}
        position_str = "{0}_{1}".format(start[0], start[1])
        self.visited_dict[position_str] = 0

    def search(self):
        position = self.path.popleft()

        if [position[0], position[1]] == self.goal:
            print(position[2])
        else:
            new_position = self.return_new_position(position)
            if len(new_position) > 0:
                for i in new_position:
                    position_str = "{0}_{1}".format(i[0], i[1])
                    if not position_str in self.visited_dict.keys():
                        self.path.append(i)
                        self.visited_dict[position_str] = i[2]
            self.search()

    def return_new_position(self, now_position):
        y, x = now_position[0], now_position[1]
        count = now_position[2]+1
        new_position_list = []

        #上方向に進める
        if 0 <= y-1 <= self.R:
            if self.maze_list[y-1][x] == ".":
                new_position_list.append([y-1, x, count])

        #下方向に進める
        if 0 <= y+1 <= self.R:
            if self.maze_list[y+1][x] == ".":
                new_position_list.append([y+1, x, count])

        #左方向に進める
        if 0 <= x-1 <= self.C:
            if self.maze_list[y][x-1] == ".":
                new_position_list.append([y, x-1, count])

        #右方向に進める
        if 0 <= x+1 <= self.C:
            if self.maze_list[y][x+1] == ".":
                new_position_list.append([y, x+1, count])

        return new_position_list

if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    line1 = input().split(" ")
    start = input().split(" ")
    goal = input().split(" ")
    R, C = int(line1[0])-1, int(line1[1])-1
    sy, sx = int(start[0])-1, int(start[1])-1
    gy, gx = int(goal[0])-1, int(goal[1])-1
    input_list = []
    for r in range(R+1):
        r_line = list(input())
        input_list.append(r_line)
    maze = Maze(R, C, input_list, [sy, sx], [gy, gx])
    maze.search()
