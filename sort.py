def sort_dictionary(input):
    x = []
    for name in sorted(input, key = lambda x: input[x][1]):
       print(f'({name}, {input[name][0]})')
       x.append((name,input[name][0]))
       


