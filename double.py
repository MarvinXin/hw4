#from double import double

def double(func):
    def inner():
        func()
        print("Let's try that again!")
        func()
    return inner



"""
@double
def greet():
    print("Hello World!")


def main():
    greet()

main()
"""