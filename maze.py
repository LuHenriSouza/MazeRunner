import os,time,sys,random

start = time.time()

def a_estrela_meia_boca(possibles):
    h = 0
    v = 1
    print(end)
    print(f'==================================\n{possibles}')
    arr = []
    for pos in possibles:
        r = [0,0]
        r[h] = end[h] - pos[h]
        r[v] = end[v] - pos[v]

        hip2 = r[h] ** 2 + r[v] ** 2
        distance = hip2 ** (1/2)
        arr.append(distance)

    juntar_array = list(zip(arr, possibles))

    array_ordenado = sorted(juntar_array, key=lambda x: x[0])

    return [elem[1] for elem in array_ordenado]


def get_rand_maze(size, chance):
    size += 2
    maze = []
    for i in range(size):
        line = []
        for i2 in range(size):
            if i2 == 0 or i2 == size - 1 or i == 0 or i == size - 1:
                line.append(1)
            else:
                base = 10000
                rn = random.randint(1, base)
                if rn < base*chance/100:
                    n = 1
                else:
                    n = 0
                line.append(n)
        maze.append(line)
    init = (random.randint(1,size - 2), 0)
    end = (random.randint(1,size - 2), size-1)
    maze[init[0]][init[1]] = 'A'
    maze[end[0]][end[1]] = 'B'
    return [maze, init, end]

def display_maze(m, path):
    m2 = m[:]
    os.system('cls') # windows use 'cls'
    
    for item in path:
        m2[item[0]][item[1]] = "."
    m2[path[-1][0]][path[-1][1]] = "M"
    
    draw = ""
    
    for row in m2:
        for item in row:
            item = str(item).replace("1","█")
            item = str(item).replace("2"," ")
            item = str(item).replace("0"," ")
            
            draw += item
        draw += "\n"
    print(draw)
   
def move(path):
    time.sleep(0.1)
    cur = path[-1]
    display_maze(maze,path)
    possibles2 = [(cur[0],cur[1] + 1),(cur[0],cur[1]- 1),(cur[0] + 1, cur[1]),(cur[0]-1, cur[1]) ]
    possibles = a_estrela_meia_boca(possibles2)
    # random.shuffle(possibles)
    
    
    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in [1,2] :
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == "B":
            path = path + (item,)
            display_maze(maze,path)
            t = time.time() - start
            input(f"Solution found in {t} seconds! Press enter to finish")
            os.system('cls')
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            maze[item[0]][item[1]] = "2"
            display_maze(maze,path)
            time.sleep(0.1)
    
[maze, init, end] = get_rand_maze(20, 20)

move((init,))

input(f"Impossible solution! Press enter to finish")
os.system('cls')
sys.exit()