sentence=input("Enter a sentence: ").lower().split()
s=set(sentence)
d={}
for i in s:
    d[i]=sentence.count(i)
d=sorted(d.items(),reverse=False)
for word, freq in d.items():
    print(f"{word}: {freq}")