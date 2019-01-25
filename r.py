#define the function that conputes the square
dictionary={}
def counter():
    #get the test value
    userValue=eval(input("Please enter even number : "))
    #Check whether the value is even
    remainder=userValue%2
    if(remainder==0):
    	#turn my variable into a global variable
        global	squareValue
        squareValue=userValue*userValue
    else:
    	print("Please enter an even number !")
    
    return(squareValue)
#create a while loop to execute the code several times depending on
count=0
while(count<=20):
	#get key from user
	
	squaredValue=counter()
	print(squaredValue)
	
	count=count+1