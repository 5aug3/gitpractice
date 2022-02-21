sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    #TODO
    rs = ""
    sentence_split = sentence.split() #문자열 리스트 생성
    for i in sentence_split[::-1]:
        rs += (i +" ")
    return rs


print(reverse_sentence(sentence))