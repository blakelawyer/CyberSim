#if self.path: # TRY REWRITING THE COMMUTE ALGORITHM
            #move = self.path.pop(0)
            #if move == 'N':
             #   self.y = self.y - 1
            #elif move == 'S':
                #self.y = self.y + 1
            #elif move == 'E':
                #self.x = self.x + 1
            #elif move == 'W':
                #self.x = self.x - 1
            #elf.history.append((self.x, self.y))
            #self.rect.x = self.x * settings.TILESIZE
            #self.rect.y = self.y * settings.TILESIZE
import util


def go_to_work_path(self, goalx, goaly):
    path = []
    y = goaly - self.y
    x = goalx - self.x
    for i in range(y):
        path.append('S')
    for i in range(x):
        path.append('E')
    return path

def bfs(self, goalx, goaly):
    visited = []
    bfs_queue = util.Queue()
    bfs_queue.push([self.x, self.y, []])
    while not bfs_queue.isEmpty():
        node = bfs_queue.pop()
        if node[0] != goalx or node[1] != goaly:
            if (node[0], node[1]) not in visited:
                visited.append((node[0], node[1]))
                successors = []
                up = True
                down = True
                left = True
                right = True
                for wall in self.game.walls:
                    if wall.x == node[0] + 1 and wall.y == node[1]:
                        right = False
                    if wall.x == node[0] - 1 and wall.y == node[1]:
                        left = False
                    if wall.y == node[1] + 1 and wall.x == node[0]:
                        down = False
                    if wall.y == node[1] - 1 and wall.x == node[0]:
                        up = False
                if up:
                    successors.append((node[0], node[1] - 1))
                if down:
                    successors.append((node[0], node[1] + 1))
                if left:
                    successors.append((node[0] - 1, node[1]))
                if right:
                    successors.append((node[0] + 1, node[1]))
                for s in successors:
                    if s not in visited:
                        path_history = []
                        path_history.extend(node[2])
                        path_history.append(s)
                        bfs_queue.push((s[0], s[1], path_history))
        else:
            path = []
            if self.x + 1 == node[2][0][0] and self.y == node[2][0][1]:
                path.append('E')
            elif self.x - 1 == node[2][0][0] and self.y == node[2][0][1]:
                path.append('W')
            elif self.x == node[2][0][0] and self.y + 1 == node[2][0][1]:
                path.append('S')
            elif self.x == node[2][0][0] and self.y - 1 == node[2][0][1]:
                path.append('N')
            for i in range(len(node[2]) - 1):
                if node[2][i][0] + 1 == node[2][i + 1][0] and node[2][i][1] == node[2][i + 1][1]:
                    path.append('E')
                elif node[2][i][0] - 1 == node[2][i + 1][0] and node[2][i][1] == node[2][i + 1][1]:
                    path.append('W')
                elif node[2][i][0] == node[2][i + 1][0] and node[2][i][1] + 1 == node[2][i + 1][1]:
                    path.append('S')
                elif node[2][i][0] == node[2][i + 1][0] and node[2][i][1] - 1 == node[2][i + 1][1]:
                    path.append('N')

            return path