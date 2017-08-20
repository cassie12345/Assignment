import re


def same_letters(item, target):
    return len([i for (i, t) in zip(item, target) if i == t])


def build(pattern, words, seen, match_words):
    return [word for word in words
            if re.search(pattern, word) and word not in seen.keys() and
            word not in match_words]

def find(word, words, seen, target_word, word_path, short):
    match_words = []
    for i in range(len(word)):
        match_words += build(word[:i] + "." + word[i + 1:], words, seen, match_words)
    for w in match_words:
        if w in exclude:
            match_words.remove(w)
        if short:
            for l in rare:
                if l not in target_word:
                    if l in w:
                        match_words.remove(w)
    if len(match_words) ==0:
        return False
    match_words = sorted([(same(w, target_word), w) for w in match_words])
    if shortest:
        match_words.reverse()
    for (match, item) in match_words:
        if match >= len(target_word) - 1:
            if match == len(target_word) - 1:
                word_path.append(item)
            return True
        seen[item] = True
    for (match, item) in match_words:
        word_path.append(item)
        if find(item, words, seen, target_word, shortest):
            return True
        word_path.pop()


def check_word(text):
    while True:
        try:
            output = input(text)
            output = output.lower()
            output - output.replace(' ', '')
            if output.isaplpha():
                if output in dictionary:
                    return output
                else:
                    print('Please enter a valid word.')
            else:
                print('Please enter a valid word.')
        except:
            print('Please enter a valid word.')
            continue



fname = input("Enter dictionary name: ")
file = open(fname)
lines = file.readlines()
while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  target = input("Enter target word:")
  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

