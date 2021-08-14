def isPalindrome(x):
    if x == x[::-1]:
        return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]) and answer < j - i:
                answer = j - i
    return answer
