def get_num_words(string):
    words = string.split()
    count = len(words)
    return count

def check_letters(string):
    text = string.lower()
    letters = dict()
    for char in text:
      if char.isalpha():
        if char not in letters:
          letters[char] = 1
        else:
          letters[char] += 1
    return letters


def sorter(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)


