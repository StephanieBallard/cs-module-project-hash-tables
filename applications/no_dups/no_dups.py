def no_dups(s):
    # Your code here
    words = s.split()

    # Store words
    d = {}

    a = []

    for word in words:
        if word not in d:
            d[word] = True
            a.append(word)
        else:
            continue
    return " ".join(a)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))