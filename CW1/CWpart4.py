# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

# Any code taken from other sources is referenced within my code solution. 


# Student ID: 20220053

# Date: 11th December 2022


pass_credit = 0
defer_credit = 0
fail_credit = 0
count = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
user_count = 0
progress_list  =[]
retriever_list =[]
trailer_list = []
exclude_list = []
user_list = []
user_count=0


def user():
    
    global user_id,user_count
    

    user_id = input('Enter your user ID: ')
    user_count+=1
    user_list.append(user_id)
    return user_id

    



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
    
    global progress_list,trailer_list,retriever_list,exclude_list
    
    

    

# Enter the credits


    if pass_credit == 120:
        
        print('Progress','\n')
        progress_count+= 1
        progress_list.append(pass_credit)
        progress_list.append(defer_credit)
        progress_list.append(fail_credit)
        type_credit='Progress'
        
    elif pass_credit == 100:
        
        print('Progress(module trailer)','\n')
        trailer_count+= 1
        trailer_list.append(pass_credit)
        trailer_list.append(defer_credit)
        trailer_list.append(fail_credit)
        type_credit = 'Progress(module trailer)'
        
    elif fail_credit >= 80:
        
        print ('Exclude','\n')
        exclude_count+= 1
        exclude_list.append(pass_credit)
        exclude_list.append(defer_credit)
        exclude_list.append(fail_credit)
        type_credit = 'Exclude'
        
    else:
        
        print('Module retriever','\n')
        retriever_count+= 1
        retriever_list.append(pass_credit)
        retriever_list.append(defer_credit)
        retriever_list.append(fail_credit)
        type_credit = 'Module retriever'
        
    return type_credit        
        
   
    
    
#PART 2

    
             
def histogram():



    while True:
        

        print('Would you like to enter another set of data?')

        ask = input('Enter "y" for yes or "q" to quit or view results. ')



        if ask.lower() == "y":
            
            print('\n')

            user()
            
            valid()
            
            credit(pass_credit,defer_credit,fail_credit)
            
            continue

        elif ask.lower() == 'q':
            
            print('-'*50 ,'\n')
            
            print('Histogram' ,'\n')

            count = progress_count + trailer_count + retriever_count + exclude_count
            
            print('Progress:', progress_count,':', progress_count* '*','')
            
            print('Trailer:'  ,trailer_count,' :', trailer_count* '*','')
            
            print('Retriever:', retriever_count,':', retriever_count* '*','')
            
            print('Excluded:', exclude_count,':', exclude_count* '*','')
            
            print('\n')
            
            print( count, 'outcomes in total' ,'\n')
        
            break
        
    


def dictonaries(user_id,type_credit):

    print('-' *50 ,'\n' )
    
    global progress_list,trailer_list,retriever_list,exclude_list,user_list,user_count

    
    
    dict ={}

    
        
    for i in range(0,len(progress_list),3):
        
        dict[user_id] = progress_list[i],progress_list[i+1],progress_list[i+2]
        for key, value in dict.items():
            print(key,':',' Progress - ', value)
        
            
      
    for i in range(0,len(trailer_list),3):
        
        dict[user_id] = trailer_list[i],trailer_list[i+1],trailer_list[i+2]
        

        
        for key, value in dict.items():
            print(key,':','  Trailer - ', value)
            

    
    for i in range(0,len(retriever_list),3):
        
        dict[user_id] = retriever_list[i],retriever_list[i+1],retriever_list[i+2]
        

        
        for key, value in dict.items():
            print(key,':' ,' Retriever - ', value)

       
    for i in range(0,len(exclude_list),3):
        
        dict[user_id] = exclude_list[i],exclude_list[i+1],exclude_list[i+2]
        

        
        for key, value in dict.items():
            print(key,':' ,' Exclude - ', value)
        

    
    
    
user_id = user()   
   
valid()

type_credit=credit(pass_credit,defer_credit,fail_credit)

histogram()

dictonaries(user_id,type_credit)

