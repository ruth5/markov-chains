"""Generate Markov text from text files."""

import random


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    return contents



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}
    # split up string and put in list
        # - print it to make sure its printing a list
        # for loop:
        # -set an i variable
    #     - for index in the len(list above):
    #         pairs = listabove[i:i+1]
    #         chain_key = (words[i], words[i + 1])
    #         chain_value = words[i + 2]
    #         chains[chain_key] = chains.get(chain_key, [])
    # # keep track of pairs
    
    words = text_string.split()
    for i in range(0, len(words)-2):
        chain_key = (words[i], words[i+1])
        chains[chain_key] = chains.get(chain_key, list([]))
        word_to_add = words[i+2]
        chain_value = chains[chain_key]
        
        chain_value.append(word_to_add)


    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    
    # choose a random first link for the random text that will be generated
    keys_list = list(chains.keys())
    # print(keys_list)
    # print(random.choice(my_list))
    first_link = random.choice(keys_list)
    words.extend(first_link)
    chain_key = first_link
    
    while True:
        if chain_key in chains:
            chain_value = chains[chain_key]
            random_value = random.choice(chain_value)
            words.append(random_value)
            chain_key = tuple((chain_key[1],random_value))
        else:
            break

   

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)
# print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
