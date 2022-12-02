"""
Pseudocode:

define main 
    test cases 1,2,3

    print test cases

define skip_tuples 
    this skip_tuples function will input a tuple, then return a new tuple as output

"""


def main():

    #Test cases
    TestCase1 = ('I', 'am', 'a', 'test', 'tuple')
    TestCase2 = ('Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday')
    TestCase3 = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')

    print(skip_tuples(TestCase1))
    print(skip_tuples(TestCase2))
    print(skip_tuples(TestCase3))

def skip_tuples(Tuples):
    '''
    skips the next inputted value, starting from the first
    '''
    return Tuples[::2]

if __name__=="__main__":
    main()
