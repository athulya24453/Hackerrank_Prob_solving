

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_s = scores[0]
    max_s = scores[0]
    
    max_c = 0
    min_c = 0
    
    for score in scores:
        if score<min_s:
            min_c += 1
            
        if score>max_s:
            max_c += 1
            
    ans = [max_c, min_c]
    
    return ans

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
