from typing import List

class node(object):
    __slots__ = ('__dict__', 'info', 'i', 'j', 'state')
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

def sorter(e):
    return e.info

def process(nodes: List[List[node]], flattened_nodes: List[node], cutoff: int):
    max_rows = int(len(flattened_nodes)/2)
    if cutoff == max_rows:
        sum_left = 0
        sum_right = 0
        for i in range(max_rows):
            sum_left = sum_left + nodes[i][0].info
            sum_right = sum_right + nodes[i][0].info
        if sum_left > sum_right:
            print(sum_left)
        else:
            print(sum_right)
        return
    
    max_sum = 0
    flattened_nodes.sort(key=sorter)

    for k in range(len(flattened_nodes)):
        init_x = flattened_nodes[k].i
        init_y = flattened_nodes[k].j
        nodes[init_x][init_y].state = 1
        nodes[init_x][(init_y+1)%2].state = 2
        if init_x - 1 >= 0:
            nodes[init_x-1][(init_y+1)%2].state = 2
        if init_x + 1 < max_rows:
            nodes[init_x+1][(init_y+1)%2].state = 2
        count = 1
        for i in range(len(flattened_nodes)):
            curr_x = flattened_nodes[i].i
            curr_y = flattened_nodes[i].j
            if nodes[curr_x][curr_y].state == 0:
                count = count + 1
                nodes[curr_x][curr_y].state = 1
                nodes[curr_x][(curr_y+1)%2].state = 2
                if curr_x - 1 >= 0:
                    nodes[curr_x-1][(curr_y+1)%2].state = 2
                if curr_x + 1 < max_rows:
                    nodes[curr_x+1][(curr_y+1)%2].state = 2
            if cutoff == count:
                break
      
        sum = 0
        for i in range(len(flattened_nodes)):
            x = flattened_nodes[i].i
            y = flattened_nodes[i].j
            if nodes[x][y].state == 0 or nodes[x][y].state == 2:
                sum = sum + nodes[x][y].info
        if sum > max_sum:
            max_sum = sum

        for i in range(max_rows):
            for j in range(2):
                nodes[i][j].state = 0
    print(max_sum)

def main():
    n,k = map(int, input().split())
    
    a = [[int(j) for j in input().split()] for i in range(n)]

    nodes = [None] * len(a)
    flattened_nodes = [None] * len(a) * 2
    for i in range(len(a)):
        nodes[i] = [None] * len(a[i])
        for j in range(2):
            nodes[i][j] = node()
            nodes[i][j] = node(**{'info' : a[i][j], 'state': 0, 'i': i, 'j': j})
            flattened_nodes[2*i+j] = node(**{'info' : a[i][j], 'state': 0, 'i': i, 'j': j})
    p,q = map(int, input().split())
    
    process(nodes, flattened_nodes, k)


if __name__ == '__main__':
    main()
