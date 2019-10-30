def read_file(name):
    """
    :param name: name of the file to read
    :return: a list of strings, each element is a line in the file (in the same order)
    """
    with open(name, "r") as f:
        return f.read().splitlines()


def write_file(name, anagram_lists):
    """
    :param name: name of the file to write
    :param anagram_lists: a list that contains lists of words that are anagrams
    :return: None
    """
    with open(name, "w") as f:
        for anagram_list in anagram_lists:
            f.write(', '.join(anagram_list) + "\n")


anagrams = dict()

# Reading the file, iterating through the words
# and groups anagrams in a dictionary of lists
for word in read_file("Files/eventyr.txt"):
    sort = ''.join(sorted(word))
    anagrams.setdefault(sort, []).append(word)

# Filtering away lists that are shorter than 2 elements
anagram_lists = list(filter(lambda x: len(x) > 1, anagrams.values()))
write_file("Files/anagrams.txt", anagram_lists)
