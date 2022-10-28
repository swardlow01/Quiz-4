#sarahwardlow
def hash_spam(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index:index + len(target)] == target:
            total += 1
        index += 1
    print(total)


hash_spam('#yolo #holla #sick', '#')
