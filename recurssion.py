def tower_of_hanoi(no_of_disks, source_rod=1, destination_rod=3):
    '''Solving Tower of Hanoi Problem using Recurssion'''
    if no_of_disks==0:
        return
    else:
        tower_of_hanoi(no_of_disks-1, source_rod, 6-source_rod-destination_rod) #Recurssive Leap of Faith
        print("move disk number {} from tower {} to tower {}".format(no_of_disks, source_rod, destination_rod))
        tower_of_hanoi(no_of_disks-1, 6-source_rod-destination_rod, destination_rod)

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
    elif (word[0]==word[-1] and check_palindrome(word[1:-1]) is True): #Recurssive Leap of Faith
        return True
    return False