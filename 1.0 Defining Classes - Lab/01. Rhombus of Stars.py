n = int(input())

for i in range(n):
    space = ' ' * (n - 1 - i)
    star = '* ' * (i + 1)
    print(f'{space}{star}')

for j in range(n - 2, -1, -1):
    space = ' ' * (n - 1 - j)
    star = '* ' * (j + 1)
    print(f'{space}{star}')


'''
4
-----------------
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
'''