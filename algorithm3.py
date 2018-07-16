# Find the single different character between two strings

str1 = 'abcd'
str2 = 'abcde'

for i in str2:
    if i not in str1:
        print(i)
        