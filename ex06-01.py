import random

def isStackFull():
    global SIZE,stack,top
    if (top>=SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE,stack,top
    if (top==-1):
        return True
    else:
        return False

def push(data) :
    global SIZE, stack, top
    if (isStackFull()):
        return
    top+=1
    stack[top]=data

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        return None
    data=stack[top]
    stack[top]=None
    top-=1
    return data

def peek():
    global SIZE,stack,top
    if(isStackEmpty()):
        return None
    return stack[top]

SIZE=int(input("주운 돌의 개수를 입력하세요 ==> "))
stack=[None for _ in range(SIZE)]
top=-1

if __name__=="__main__":

    stoneAry=[None for _ in range(SIZE)]
    for i in range(0,SIZE):
        stoneAry[i]=input(f'{i+1}번째로 주운 돌의 색깔 ==> ')
    
    random.shuffle(stoneAry)

    print("과자집에 가는길 : ",end=' ')
    for stone in stoneAry:
        push(stone)
        print(stone,"-->",end=' ')
    print("과자집")

    print("우리집에 오는길 : ",end=' ')
    while True:
        stone=pop()
        if stone==None:
            break
        print(stone,"-->",end=' ')
    print("우리집")
