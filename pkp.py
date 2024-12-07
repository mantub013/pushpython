
              
n=int(input('enter the fibonacci sequence length to be generated:'))
if n<=0:
    print('please enter a positive integer greater than 0: ')
else:
     first_number=0
     second_number=1
     print('the fibonacci series is:')
     print(first_number)
      
     if n>1:
         print(second_number)
              
     for i in range(2,n):

        new_number=first_number+second_number
        print(new_number)
        first_number=second_number
        second_number=new_number
              

