def sort_dictionary(input):
    x = []
    for name in sorted(input, key = lambda x: input[x][1]):
       x.append((name,input[name][0]))

    print(x)  


    





