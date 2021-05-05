from collections import deque

def find_head(board,m):
    i = 0;
    while True:
        j = 0;
        while j < m:
            if board[i][j] != '.' and board [i][j] != '*':
                return [i,j]
            j += 1
        i += 1

def find_snake(board,head,n,m):
    i, j = head[0], head[1]
    status = 0
    snake = deque()
    snake.append([i,j])
    while True:
        if status!= 2 and i - 1 >= 0 and board[i - 1][j] == '*':
            i -= 1
            snake.append([i,j])
            status = 1
            continue
        elif status != 1 and i + 1 < n and board[i + 1][j] == '*':
            i += 1
            snake.append([i,j])
            status = 2
            continue
        elif status != 4 and j - 1 >= 0 and board[i][j - 1] == '*':
            j -= 1
            snake.append([i,j])
            status = 3
            continue
        elif status != 3 and j + 1 < m and board[i][j+1] == '*':
            j += 1
            snake.append([i,j])
            status = 4
            continue
        else:
            return snake

def move(board,snake,head,commands,n,m):
    for i in commands:
        if i == 'R':
            if board[head[0]][head[1]] == '^':
                board[head[0]][head[1]] = '>'
            elif board[head[0]][head[1]] == 'v':
                board[head[0]][head[1]] = '<'
            elif board[head[0]][head[1]] == '>':
                board[head[0]][head[1]] = 'v'
            elif board[head[0]][head[1]] == '<':
                board[head[0]][head[1]] = '^'
        elif i== 'L':
            if board[head[0]][head[1]] == '^':
                board[head[0]][head[1]] = '<'
            elif board[head[0]][head[1]] == 'v':
                board[head[0]][head[1]] = '>'
            elif board[head[0]][head[1]] == '>':
                board[head[0]][head[1]] = '^'
            elif board[head[0]][head[1]] == '<':
                board[head[0]][head[1]] = 'v'
        else:
            if board[head[0]][head[1]] == '^':
                if (head[0] - 1 >= 0 and board[head[0] - 1][head[1]] == '.') or (head[0] - 1 == snake[-1][0] and head[1] == snake[-1][1]):
                    board[head[0]][head[1]] = '*'
                    board[snake[-1][0]][snake[-1][1]] = '.'
                    board[head[0]-1][head[1]] = '^'
                    snake.pop()
                    snake.appendleft([head[0]-1,head[1]])
                    head = snake[0]
                else:
                    return "Death"
            elif board[head[0]][head[1]] == 'v':
                if (head[0] + 1 < n and board[head[0] + 1][head[1]] == '.') or (head[0] + 1 == snake[-1][0] and head[1] == snake[-1][1]):
                    board[head[0]][head[1]] = '*'
                    board[snake[-1][0]][snake[-1][1]] = '.'
                    board[head[0]+1][head[1]] = 'v'
                    snake.pop()
                    snake.appendleft([head[0]+1,head[1]])
                    head = snake[0]
                else:
                    return "Death"
            elif board[head[0]][head[1]] =='<':
                if (head[1] - 1 >= 0 and board[head[0]][head[1] - 1] == '.') or (head[1] - 1 == snake[-1][1] and head[0] == snake[-1][0]):
                    board[head[0]][head[1]] = '*'
                    board[snake[-1][0]][snake[-1][1]] = '.'
                    board[head[0]][head[1]-1] = '<'
                    snake.pop()
                    snake.appendleft([head[0],head[1]-1])
                    head = snake[0]
                else:
                    return "Death"
            elif board[head[0]][head[1]] =='>':
                if (head[1] + 1 < m and board[head[0]][head[1] + 1] == '.') or (head[1] + 1 == snake[-1][1] and head[0] == snake[-1][0]):
                    board[head[0]][head[1]] = '*'
                    board[snake[-1][0]][snake[-1][1]] = '.'
                    board[head[0]][head[1]+1] = '>'
                    snake.pop()
                    snake.appendleft([head[0],head[1]+1])
                    head = snake[0]
                else:
                    return "Death"
    return "Alive"



#Nhap du lieu
n,m,c = [int(x) for x in input().split()]
board = []
for i in range(n):
    board.append([y for y in input()])
commands = input()

#Tim con ran
head = find_head(board,m)
snake = find_snake(board,head,n,m)
CheckStatus = move(board,snake,head,commands,n,m)

#In hinh dang con ran sau khi ket thuc tro choi
if CheckStatus == "Alive":
    for i in board:
        for j in i:
            print(j,end='')
        print()
else:
    for i in board:
        for j in i:
            if j != '.':
                print('X',end='')
            else:
                print(j,end='')
        print()