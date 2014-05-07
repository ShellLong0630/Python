import random,time
a=0

##def IN(x):
##    if x not in [1,2]:
##        print ('please input 1 or 2.')
##        result = int(input("your number : "))
##    else:
##        result = "The computer's number is : "
##    return result    
for i in range(1,21):
    b = input("your number : ")

    for t in range(1,100000000000):
        if b not in ['1','2']:
            print ('please input 1 or 2.')
            b = input("your number : ")
        else:
            break
    a+=int(b)
    print('= %s'% a)
    if a==20:
        print('You win!')
        break
    elif a>20:
        print('You lose!')
        break
    time.sleep(0.2)
    #电脑给出数字
    if a in [19,16,13,10,7,4,1]:
        c=1
    elif a in [18,15,12,9,6,3]:
        c=2
    else:
        c = random.randint(1,2)
    print("The computer's number is : %s"% c)
    a+=c
    print('= %s'% a)
    if a==20:
        print('You lose!')
        break
    elif a>20:
        print('You win!')
        break
