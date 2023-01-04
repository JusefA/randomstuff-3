def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))