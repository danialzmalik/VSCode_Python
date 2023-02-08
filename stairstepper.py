
def printStep(num):
    numOfPrint=num
    if(num>1):
        num-=1
        printStep(num)
    while(numOfPrint>1):
        print("x", end="")
        numOfPrint-=1        
    print("x")


val = int(input("how many stairs should there be: "))
printStep(val)
