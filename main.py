def get_column(data):
    column_name = []
    column = data.split('\n')
    column_name = column[0].split(',')
    return column_name

data = open('data.csv').read()
print(get_column(data))
