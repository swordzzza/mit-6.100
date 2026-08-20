def same_chars(s1, s2):
    for ch in s1:
        if ch not in s2:
            return False
    for ch in s2:
        if ch not in s1:
            return False
    return True

print(same_chars("abc","cab"))
print(same_chars("abcd","cabaa"))
print(same_chars("abccc","caaab"))
print(same_chars("abcabc","cabz"))

        
