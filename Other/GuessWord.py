
def Game(secret, try_count):
    print("secret: ", secret[0:try_count], "_"*(len(secret)-try_count), sep='')
    win = (input("Enter guess: ") == secret)
    if win:
        print('You Win!')
    elif try_count < len(secret):
        Game(secret, try_count+1)
    else:
        print('You Loose')

Game('JoshuaFrewin', 0)
