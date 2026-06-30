def wordpattern(pattern,s):
    word=s.split()
    if len(pattern)!=len(word):
        return False
    char_to_word={}
    word_to_char={}
    for ch,word in zip(pattern,word):
        if ch in char_to_word:
          if char_to_word[ch]!=word:
              return False
        else:
            char_to_word[ch]=word
        if word in word_to_char:
            if word_to_char[word]!=ch:
                return False
        else:
            word_to_char[word]=ch
    return True
pattern="abba"
s="dog,cat,cat,dog"
result=wordpattern(pattern,s)
print(result)
            



