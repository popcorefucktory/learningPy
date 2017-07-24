parMap = {
    ')': '(',
    '}': '{',
    ']': '['
}


def balanced(astr):
    stack = []
    opening = parMap.values()
    closing = parMap.keys()
    for c in astr:
        if (c in opening):
            stack.append(c)
        else:
            if (c in closing):
                if not stack or parMap.get(c) != stack.pop():
                    return False
    return not stack


print(balanced("fdhjh(dfd[3({)}(]{er}{er}df{er}(34)7)"))
