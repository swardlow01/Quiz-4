#sarahwardlow
def count_hashtag(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    print(count)


count_hashtag('i use # when I tweet on twitter #ilovehastags', '#')
