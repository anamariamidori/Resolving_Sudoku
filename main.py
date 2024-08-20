import random

#aqui temos uma função para cada tentativa de numero possível
#assim producando por linha, coluna e bloco de 3x3 vendo se tem o numero a ser tentado naquele quadrado
def tentativa(x,y,n,sudoku):
    # n = numero que esta tentando no momento
    #verifica se a linha contem N
    if n in sudoku[y]:
        return False
    #verifica se a coluna conte N
    if n in [sudoku[i][x] for i in range(9)]:
        return False
    #verifica bloco 3x3
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True
#aqui ele ve se a resposta que estou colocando resolve o problema, se não ele volta e tenta novos numeros
def resolve(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if tentativa(x,y,n,sudoku):
                        sudoku[y][x] = n
                        if resolve(sudoku):
                            return True #aqui é a parte que ele achou um nó que resolve
                        sudoku[y][x] = 0 # aqui ele diz que o nó não resolve o sudoku e retorna para o proximo numero
                return False
    return True


def print_board(sudoku):
    for a in range(0, 9):
        print(sudoku[a])
        a = a + 1


#aqui ele gera o sudoku
def generate_sudoku():
    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        startRow, startCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[startRow + i][startCol + j] == num:
                    return False
        return True
#preenche o jogo com os numeros e sua resposta
    def fill_board(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    num_list = list(range(1, 10))
                    random.shuffle(num_list)
                    for num in num_list:
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if fill_board(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
#retira a resposta e mantem apenas o jogo
    def remove_numbers(board, level):
        count = {'easy': 30, 'medium': 40, 'hard': 50}
        cells_to_remove = count.get(level, 30)
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                cells_to_remove -= 1

    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    level = 'easy'  # mude a dificuldade caso queira para medium ou hard
    remove_numbers(board, level)
    return board


# Test the Sudoku generator
sudoku_board = generate_sudoku()
print_board(sudoku_board)

print("\n")
print_board(resolve(sudoku_board))
