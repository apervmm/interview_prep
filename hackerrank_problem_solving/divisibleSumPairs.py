
import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(len(ar)-1):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0 and i != j:
                count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
