import sys
from random import choice

def open_and_read_file(filepath):

    file = open(filepath)
    text = file.read()
    file.close()

    return text

def make_chains(text_string):
    chains = {}
    words = text_string.split()
    words.append(None)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]
        if key not in chains:
            chains[key] = []

        chains[key].append(value)
    
    return chains

def make_text(chains):
    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

    return ' '.join(words)

input_path = 'green-eggs.txt'
input_text = open_and_read_file(input_path)
chains = make_chains(input_text)
random_text = make_text(chains)
print(random_text)
print(chains)