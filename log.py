import time
from log import timestamp

def timestamp(func):
    def inner():
        print(time.ctime())
        func()
    return inner

"""
@timestamp
def hi():
    print('hi')

def main():
    hi()

main()
"""