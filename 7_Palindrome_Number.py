def palindrome(n):
    n = str(n)
    a = ''
    b = -1
    for i in range(len(n)):
        a = a + n[b]
        b = b - 1

    if a == n:
        print('True')
    else:
        print('False')

x = input('Enter to check palindrome : ')
x = x.lower()
palindrome(x)


