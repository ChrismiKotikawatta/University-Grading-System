
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution. 


# Student ID: 20220053

# Date: 30th November 2022


pass_credit = 0
defer_credit = 0
fail_credit = 0
count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

def valid():

    global pass_credit, defer_credit, fail_credit
        
    while True:
        
#validation of the pass credits

        while True:
            
            try:
                pass_credit= int(input('Enter your total pass credits: '))
                break
            except ValueError:
                print('Integer is Required!')
                continue

        if pass_credit <=120 and pass_credit % 20 == 0:
            pass
        else:
            print('Out of Range!')
            continue

#validation of the defer credits
        
        while True:

            try:
                defer_credit = int(input('Enter your total  defer credits: ' ))
                break
            except ValueError:
                print('Integer is Required! ')
                continue
            
        if defer_credit <=120 and defer_credit % 20 == 0:
            pass
        else:
            print('Out of Range!')
            continue

#validation of fail credits
        
        while True:
            
            try:
                fail_credit = int(input('Enter your total fail credits:'))
                break
            except ValueError:
                print('Integer is Required! ')
                continue

        if fail_credit <=120 and fail_credit % 20 == 0:
            pass
        else:
            print('Out of Range!')
            continue


        total_credit = pass_credit + defer_credit + fail_credit

        if total_credit != 120:
            print('Total s Incorrect! Try Again! ')
            continue
        else:
            break




def credit(pass_credit, defer_credit, fail_credit):
    
    global progress_count,trailer_count,retriever_count,exclude_count

    

# Enter the credits

    if pass_credit == 120:
        
        print('Progress','\n')
        
        progress_count+= 1
        
    elif pass_credit == 100:
        
        print('Progress(module trailer)','\n')
        
        trailer_count+= 1
        
    elif fail_credit >= 80:
        
        print ('Exclude','\n')
        
        exclude_count+= 1
        
    else:
        
        print('Module retriever','\n')
        
        retriever_count+= 1
   
    
    


    
             
def histogram():


    while True:

#Asking the user if they want to enter another set of data.
        
        print('Would you like to enter another set of data?')

        
        ask = input('Enter "y" for yes or "q" to quit or view results. ')
        
        
#If it is yes ask the user to enter the credits.
        
        if ask.lower() == "y":
            
            print('\n')

            valid()
            
            credit(pass_credit,defer_credit,fail_credit)
            
            continue
        
#If it is no exit the loop and print the histogram
        

        elif ask.lower() == 'q':
            
            print('-'*50 ,'\n')
            
            print('Histogram','\n')
            
            count = progress_count + trailer_count + retriever_count + exclude_count
            
            print('Progress:', progress_count,':', progress_count* '*','')
            
            print('Trailer:'  ,trailer_count,' :', trailer_count* '*','')
            
            print('Retriever:', retriever_count,':', retriever_count* '*','')
            
            print('Excluded:', exclude_count,':', exclude_count* '*','')

            print('\n')
            
            print( count, 'outcomes in total' )
            
            break
        
    
    

   

valid()

credit(pass_credit,defer_credit,fail_credit)

histogram()




 
