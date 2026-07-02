from janome.tokenizer import Tokenizer

def count_and_vectorize(dic, sent):
    tokenizer = Tokenizer()
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    words = []
    for token in tokenizer.tokenize(sent):
        words.append(token.base_form)

    for i in words:        
        if i in dic:
            if dic[i] == "n":
                num_negative += 1
            elif dic[i] == "p":
                num_positive += 1
            elif dic[i] == "e":
                num_neutral += 1
    num_total = num_negative + num_positive + num_neutral 
    
    return [num_positive, num_negative, num_neutral, num_total]


