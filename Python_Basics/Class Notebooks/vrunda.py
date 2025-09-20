print('custom module is called')

def palindrome(a): 
    if a== a[::-1]: 
        return 'palindrome'
    return 'not palindrome'

def is_even(a):
    if a%2 ==0: 
        return 'Even'
    return 'Odd'

print(__name__) # we want to check how name is printed 

if __name__ == '__main__': #testing purposes, to make sure module is working as needed
    print(palindrome('121'))
    print(is_even(2))
else: # not needed as we are passing it
    pass # we dont want to test the module, we want to use it. 