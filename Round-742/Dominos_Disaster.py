"""
@Author: Amar Gosavi
Link: https://codeforces.com/contest/1567/problem/A
"""

def solve(string):
     ans = ""
     for ch in string:
          if ch == "L":
               ans += "L"
          elif ch == "R":
               ans += "R"
          elif ch == "U":
               ans += "D"
          else:
               ans += "U"
     return ans

def main():
     t = int(input())
     for _ in range(t):
          n = int(input())
          string = input()
          ans = solve(string)
          print(ans)

if __name__ == "__main__":
     main()