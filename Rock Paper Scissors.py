from random import randint

rps_lst = ['r', 'p', 's']


def win(you, comp_value):
    win_flag = False
    if you == 'r' and comp_value == rps_lst[2]:
        win_flag = True
    elif you == 'p' and comp_value == rps_lst[0]:
        win_flag = True
    elif you == 's' and comp_value == rps_lst[1]:
        win_flag = True

    return win_flag


def game_loop():
    game_over = False
    while not game_over:
        your_value = input("RPS?: ").lower()
        if your_value not in rps_lst:
            print("Unhandled coomand, try it again")
            continue

        comp_value = rps_lst[randint(0, 2)]
        print(f"<{your_value.upper()}> vs <{comp_value.upper()}>")

        if win(your_value, comp_value):
            print("Win!")
            game_over = True
        elif not win(your_value, comp_value) and your_value == comp_value:
            print("Draw between players")
        else:
            print("Lose!")
            game_over = True

    return game_over


game_loop()
