from janome.tokenizer import Tokenizer

def check(entry, words):
    for i in range(len(entry)):
        if entry[i] != words[i]:
            return False
    return True

def match(dic_arr, words):
    for entry in dic_arr:
        if check(entry[0], words):
            return entry[1]
    return None

def count_and_vectorize(sentence, dictionary):
    nums = [0, 0, 0]  # neutral, positive, negative
    t = Tokenizer()
    words = [ token.base_form for token in t.tokenize(sentence) ]
    for i in range(len(words)):
        if words[i] in dictionary:
            tmp = match(dictionary[words[i]], words[i+1:])
            if not(tmp == None):
                nums[tmp] = nums[tmp] + 1
    return nums