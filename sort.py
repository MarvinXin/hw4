def sort_dictionary(input):
    x = []
    for name in sorted(input, key = lambda x: input[x][1]):
       print(f'({name}, {input[name][0]})')
       x.append((name,input[name][0]))
       


"""
#My code tester:
input_list={"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}
#result = []
result = sort_dictionary(input_list)
print(result)
"""

