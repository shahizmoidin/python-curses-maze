
import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],

    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def find_start(maze,start):
    for i ,row in enumerate(maze):
        for j,value in enumerate(row):
            if value==start:
                return i,j


def find_path(maze,stdscr):
    start="O"
    end="X"
    startpos=find_start(maze,start)
    q=queue.Queue()
    q.put((startpos,[startpos]))
    visited=set()

    while not q.empty():
        current_pos,path=q.get()  
        row,col=current_pos

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col]==end:
            return path
        
        neighbour=find_neighbours(maze,row,col)
        for neighou in neighbour:
            if neighou in visited:
                continue
            r,c=neighou
            if maze[r][c]=="#":
                continue

            new_path=path+[neighou]
            q.put((neighou,new_path))
            visited.add(neighou)
        

def find_neighbours(maze,row,col):
    neigbors=[]
    if row>0:
        neigbors.append((row-1,col))
    if row+1<len(maze):
        neigbors.append((row+1,col))
    if col>0:
        neigbors.append((row,col-1))
    if col+1 <len(maze[0]):
        neigbors.append((row,col+1))

    return neigbors






def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)

    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)


def main(stdscr):

    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    find_path(maze,stdscr)
    stdscr.getch()

wrapper(main)