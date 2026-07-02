from collections import Counter
def ansomnote(ransomnote,maganize):
    ransom_count=Counter(ransomnote)
    maganize_count=Counter(maganize)
    
    for ch in ransom_count:
        if ransom_count[ch]>maganize_count[ch]:
            return False
    return True
ransomnote="aa"
maganize="aab"
print(ansomnote(ransomnote,maganize))    