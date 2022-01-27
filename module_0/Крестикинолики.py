def greet(count):
    if count == 0:
        print("Добро пожаловать в игру крестики-нолики для двоих!",
              "Чтобы выиграть, нужно составить комбинацию три в ряд.",
              "Вводить координаты нужно через пробел: сначала строку, затем столбец.", sep="\n")


def show_board(board):
    """
    Выводит поле с текущим расположением крестиков и ноликов.
    """
    print(" ", 1, 2, 3)
    for i in range(3):
        print(i + 1, *board[i])


def take_input(player_token, board):
    """
    Принимает от пользователя координаты и размещает там соответсвующую фигуру,
    если это возможно. 
    """
    while True:
        inp = input("Куда хотите поставить " + player_token + "? ")
        try:
            x, y = map(int, inp.split())
        except:
            print("Некорректный ввод. Вы уверены, что ввели координаты?")
            continue
        if 1 <= x <= 3 and 1 <= y <= 3:
            if board[x - 1][y - 1] == "·":
                board[x - 1][y - 1] = player_token
                break
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите координаты от 1 1 до 3 3.")


def check(board):
    """
    Проверяет, нет ли выигрышной коомбинации на поле.
    """
    arr = [i for s in board for i in s]
    win_pos = (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    for x, y, z in win_pos:
        if arr[x] in "XO":
            if arr[x] == arr[y] == arr[z]:
                return arr[x]


def main():
    """
    Основная фунция игры.
    """
    greet()
    input("Нажмите Enter, чтобы начать играть.")
    board = [["·" for i in range(3)] for j in range(3)]    
    counter = 0
    while True:
        show_board(board)
        if counter % 2:
            take_input("O", board)
        else:
            take_input("X", board)
        counter += 1
        if counter > 4:
            tmp = check(board)
            if tmp:
                print(tmp, "выиграл!")
                return
        if counter == 9:
            print("Ничья!")
            return
    show_board(board)


while True:
    main()
    inp = input("Наберите 'выход', чтобы выйти, или Enter, чтобы сыграть снова. ")
    if inp == "выход":
        break
