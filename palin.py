def palindrome(s: str):
    snew = s.replace(" ", "").lower()
    ls = len(snew)
    if snew[:ls // 2] == snew[ls // 2 + 1:][::-1]:
        return True
    return False

print("taco cat - ", palindrome("taco cat"))
print("rotator - ", palindrome("rotator"))
print("black cat - ", palindrome("black cat"))
print("madam - ", palindrome("madam"))
print("python - ", palindrome("python"))