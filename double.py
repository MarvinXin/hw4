from double import double

def double(func):
    def inner():
        func()
        print("Lets do this again!")
        func()
    return inner


'''

@double
def greet():
    print("Hello World!")


def main():
    greet()

main()
'''