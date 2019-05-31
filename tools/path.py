import os

print(os.path.isdir('C:/'))

releasePath = ('D:/' if os.path.isdir('D:/') else 'C:/' ) + 'yysScript'


def dirname():
    return os.path.dirname(os.path.realpath(__file__))

    
print(dirname())