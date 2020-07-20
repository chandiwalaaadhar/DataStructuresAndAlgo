import copy

def tower_of_hanoi(no_of_disks, source_rod, auxillary_rod ,destination_rod):
    '''Solving Tower of Hanoi Problem using Recurssion'''
    if no_of_disks==0:
        return
    else:
        tower_of_hanoi(no_of_disks-1, source_rod, auxillary_rod, destination_rod) #Recursive Leap of Faith
        destination_rod.append(source_rod.pop())
        print("move disk number {} from tower {} to tower {}".format(no_of_disks, source_rod, destination_rod))
        tower_of_hanoi(no_of_disks-1, auxillary_rod, destination_rod, source_rod)


def digit_to_bitstr(num):
    '''Solving digit to bit strings using Recurssion'''
    if (num==0):
        return []
    if (num==1):
        return ['0','1']
    return [digit+bitstr for digit in digit_to_bitstr(1) for bitstr in digit_to_bitstr(num-1)]


def check_palindrome(word):
    '''Checking Palindrome Number using Recurssion'''
    if (len(word)<=1): #base case 1
        return True
    elif (len(word)==2 and word[0]==word[1]): #base case 2
        return True
    elif (word[0]==word[-1] and check_palindrome(word[1:-1]) is True): #Recursive Leap of Faith
        return True
    return False


def permute(list_, start_idx):
    '''Calculating Permutations of an Input list'''
    if (start_idx==len(list_)-1):
        print (toList(list_)) #Helper Function
    else:
        for i in range(start_idx, len(list_), 1):
            list_[start_idx], list_[i]= list_[i], list_[start_idx]
            permute(list_, start_idx+1) #Recursive Leap of Faith
            list_[start_idx], list_[i]= list_[i], list_[start_idx] #Backtracking 
def toList(list_):
    '''Helper Function for permute()'''
    return (''.join(list_))


def is_list(list_):
    '''Helper Functin for deepReverse()'''
    return isinstance(list_, list)
def deepReverse(deepList):
    '''Approach to reverse a list with nested lists
    Input: [1, [2,3], 4, [5,6]]
    Output: [[6, 5], 4, [3, 2], 1]'''
    deepList.reverse()
    for i in deepList:
        if is_list(i):
            deepReverse(i)
    return deepList


def get_characters(num):
    '''Helper Function for keypad_combinations'''
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""
def keypad_combinations(num):
    '''Function to calculate Mobile keypad combinations
    Input: 23
    Output: ['da', 'db', 'dc', 'ea', 'eb', 'ec', 'fa', 'fb', 'fc'] '''
    if num==0:
        return []
    if (num/10<1):
        return [element for element in get_characters(num)]
    else: 
        current_iter = num%10
        result=[]
        for i in get_characters(current_iter):
            for j in keypad_combinations(num//10):
                result.append(i+j)
        return result


if __name__ == "__main__":
    #permute(['a','d','a','h','r','a'], 0)
    #print(keypad_combinations(23))