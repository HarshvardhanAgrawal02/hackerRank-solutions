# Problem: Say "Hello, World!" With Python
# Difficulty: Easy
#Link: https://www.hackerrank.com/challenges/py-if-else/problem

n=int(input()) # or  int(input().strip()) :- 
#                    - Removes any **extra whitespace, spaces, or newline    
#                      characters** from both ends of the string
#                    - Example: `"  24\n"` → becomes `"24"`

if n%2!=0:
    print("Weird")
elif n%2==0 and 2<=n<=5:
    print("Not Weird")
elif n%2==0 and 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")    