
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution. 


# Student ID: 20220053

# Date: 5th December 2022


pass_credit = 0
defer_credit = 0
fail_credit = 0
count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progress_list  =[]
retriever_list =[]
trailer_list = []
exclude_list = []

#PART 1

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
        progress_list.append(pass_credit)
        progress_list.append(defer_credit)
        progress_list.append(fail_credit)
        
    elif pass_credit == 100:
        
        print('Progress(module trailer)','\n')
        trailer_count+= 1
        trailer_list.append(pass_credit)
        trailer_list.append(defer_credit)
        trailer_list.append(fail_credit)
        
    elif fail_credit >= 80:
        
        print ('Exclude','\n')
        exclude_count+= 1
        exclude_list.append(pass_credit)
        exclude_list.append(defer_credit)
        exclude_list.append(fail_credit)
        
    else:
        
        print('Module retriever','\n')
        retriever_count+= 1
        retriever_list.append(pass_credit)
        retriever_list.append(defer_credit)
        retriever_list.append(fail_credit)


   
    
    
#PART 2

    
             
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

            print('\n')
            
            print('-'*50,'\n')
            
            print('Histogram','\n')

            count = progress_count + trailer_count + retriever_count + exclude_count
            
            print('Progress:', progress_count,':',progress_count* '*','')
            
            print('Trailer:'  ,trailer_count,' :', trailer_count* '*','')
            
            print('Retriever:', retriever_count,':', retriever_count* '*','')
            
            print('Excluded:', exclude_count,':', exclude_count* '*','')
            
            print( count, 'outcomes in total' )

            print('\n')
        
            break
        

#PART 2
#Printing the list  
    

def credit_list():

    print('-'*50,'\n')

    print('\n')

    print('Would you like to print the list of the credits? ')

    ask_list = input('Enter "y" for yes or "q" to quit. ')

   


    if ask_list.lower() == 'y':

        print('\n')

        for i in range(0,len(progress_list),3):
            
            print('Progress - ',progress_list[i],',',progress_list[i+1],',',progress_list[i+2])
            
        for i in range(0,len(retriever_list),3):
            
            print('Retriver - ',retriever_list[i],',',retriever_list[i+1],',',retriever_list[i+2])
            
        for i in range(0,len(trailer_list),3):
            
            print('Trailer  - ' ,trailer_list[i],',',trailer_list[i+1],',',trailer_list[i+2])
            
        for i in range(0,len(exclude_list),3):
            
            print('Exclude  - ', exclude_list[i],',',exclude_list[i+1],',',exclude_list[i+2])

    elif ask_list.lower() == 'q':
        

        quit()
        

        
#PART 3
#Creating a text file.

def text_file():

    print('\n')

    print('-'*50,'\n')

    print('\n')

    print('Would you like to print the text file? ')

    ask_text = input('Enter "y" for yes or "q" to quit.')

    if ask_text.lower() == 'y':

        print('\n')           

        file = open('textfile.txt','w')
           

        for i in range(0,len(progress_list),3):

            file.write('\n')

            file.write('Progress - ')
            
            file.write( str(progress_list[i]))

            file.write(' , ')
            
            file.write(str(progress_list[i+1]))

            file.write(' , ')
            
            file.write(str(progress_list[i+2]))
            
        for i in range(0,len(retriever_list),3):

            file.write('\n')

            file.write('Retriver - ')
            
            file.write( str(retriever_list[i]))

            file.write(' , ')
            
            file.write(str(retriever_list[i+1]))

            file.write(' , ')
            
            file.write(str(retriever_list[i+2]))
            
        for i in range(0,len(trailer_list),3):

            file.write('\n')

            file.write('Trailer - ')
            
            file.write( str(trailer_list[i]))

            file.write(' , ')
            
            file.write(str(trailer_list[i+1]))

            file.write(' , ')
            
            file.write(str(trailer_list[i+2]))
            
        for i in  range(0,len(exclude_list),3):

            file.write('\n')

            file.write('Exclude  - ')
            
            file.write(str(exclude_list[i]))

            file.write(' , ')
            
            file.write(str(exclude_list[i+1]))

            file.write(' , ')
            
            file.write(str(exclude_list[i+2]))

        file.close()
        
        file = open('textfile.txt','r')
        
        print(file.read())

        
    elif ask_text.lower() == 'q':

        quit()
    
   
   
valid()

credit(pass_credit,defer_credit,fail_credit)

histogram()

credit_list()

text_file()








 
    

 

