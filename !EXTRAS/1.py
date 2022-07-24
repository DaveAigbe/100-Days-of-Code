filename = '../Intermediate Projects/Flash Card App/known_words.txt'

with open(filename, 'r') as f:
    known_words = f.read().split()





for x in known_words:
    print(known_words.count(x))