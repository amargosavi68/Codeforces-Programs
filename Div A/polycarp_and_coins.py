"""
@Author: Amar Gosavi
problem link: https://codeforces.com/contest/1551/problem/A
>>input:
     6
     1000
     30
     1
     32
     1000000000
     5

>>output:
     334 333
     10 10
     1 0
     10 11
     333333334 333333333
     1 2
"""

T = int(input())
for _ in range(T):
     N = int(input())
     if N == 1:
          print(1,0)
     elif N == 2:
          print(0,1)
     else:
          temp = N // 3
          rem = N % 3
          if rem == 1:
               print(temp+1, temp)
          elif rem == 2:
               print(temp, temp+1)
          else:
               print(temp, temp)