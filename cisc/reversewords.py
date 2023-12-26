"""
Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

Example 1:

Input:  S = i.like.this.program.very.much
Output:     much.very.program.this.like.i
Explanation: After reversing the whole
            string(not individual words), the input
            string becomes
            much.very.program.this.like.i
"""


def reverseWords(S: str):
    # Vanila Code
    newstr = S.split(".")
    newstr.reverse()
    return ".".join(newstr)


def reverseWordsAlgo(S: str):
    # Some hard code
    ar = []
    start, end = 0, 0
    for i in range(len(S)):
        if (c := S[i]) == ".":
            end = i
            ar.append(S[start: end])
            start = end + 1
        
        if i == len(S) - 1:
            ar.append(S[start: i+1])

    L, R = 0, len(ar) -1
    while L < R:
        temp = ar[L]
        ar[L] = ar[R]
        ar[R] = temp
        L += 1
        R -= 1

    return ".".join(ar)

print(reverseWordsAlgo("much.very.program.this.like.i"))
