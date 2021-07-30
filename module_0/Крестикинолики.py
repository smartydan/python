board = [["-" for i in range(3)] for j in range(3)]

def greet():
    print("Добро пожаловать в игру крестики-нолики на двоих!")
    

def show_board(board):
    """
    Выводит поле с текущим расположением крестиков и ноликов.
    """ 
    for i in range(3):
        print(i + 1, *board[i])
    print(" ", 1, 2, 3)


def take_input(player_token):
    """
    Принимает от пользователя координаты и размещает там соответсвующую фигуру. 
    """
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            x, y = list(map(int, player_answer.split()))
        except:
            print("Некорректный ввод. Вы уверены, что ввели координаты?")
            continue
        if 1 <= x <= 3 and 1 <= y <= 3:
            if(str(board[x - 1][y - 1]) not in "XO"):
                board[x - 1][y - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите координаты от 1 1 до 3 3.")


def check(board):
   """
   Проверяет, нет ли выигрышной коомбинации на поле.
   """
   win_coord = (((1, 1), (2, 1), (3, 1)), ((1, 2),(2, 2), (3, 2)), ((1, 3),(2, 3), (3, 3)), ((1, 1), (1, 2), (1, 3)),\
                ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)), ((1, 1), (2, 2), (3, 3)), ((1, 3), (2, 2), (3, 1)))
   for i in win_coord:
       if board[i[0][0] - 1][i[0][1] - 1] == board[i[1][0] - 1][i[1][1] - 1] == board[i[2][0] - 1][i[2][1] - 1] and board[i[0][0] - 1][i[0][1] - 1] in "XO":
          return board[i[0][0] - 1][i[0][1] - 1]
   return False


def main(board):
    """
    Основная фунция игры.
    """
    greet()
    counter = 0
    win = False
    while not win:
        show_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    show_board(board)
    
    
main(board)

input("Нажмите Enter для выхода!")
