def tower_of_hanoi(no_of_disks, source_rod=1, destination_rod=3):
    '''Solving Tower of Hanoi Problem using Recurssion'''
    if no_of_disks==0:
        return
    else:
        tower_of_hanoi(no_of_disks-1, source_rod, 6-source_rod-destination_rod) #Recurcive Leap of Faith
        print("move disk number {} from tower {} to tower {}".format(no_of_disks, source_rod, destination_rod))
        tower_of_hanoi(no_of_disks-1, 6-source_rod-destination_rod, destination_rod)