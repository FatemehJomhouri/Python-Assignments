def xy(x, y):
    for rows in range(0, x):
        if y % 2 == 0:
            if rows % 2 == 0:
                print(y // 2 * '#*')
            else:
                print(y // 2 * '*#')
        else:
            if rows % 2 == 0:
                print(y // 2 * '#*' + '#')
            else:
                print(y // 2 * '*#' + '*')


x = int(input('Enter number of rows: '))
y = int(input('Enter number of columns: '))

xy(x, y)