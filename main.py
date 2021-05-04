from datetime import  datetime
#  User login


# create  a list of available users
list_of_accepted_user = ['Daniel', 'Esua', 'Warrie']
list_of_user_password = ['daniel1234','esua7865', 'warrie9876']

# prompt user to signin(enter name)
user_name = input('what is your name?')

if user_name in list_of_accepted_user:
    user_id = list_of_accepted_user.index(user_name)
    user_password = input('input your password?')
    if user_password == list_of_user_password[user_id]:
        current_date = datetime.now()
        print('Successful login on ' , current_date.strftime("%A,%d %B, %Y. %I:%M%p"))
        print('Welcome {s}'.format(s =user_name))

        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')



        selected_option = int(input('Please select an option: '))
        if (selected_option == 1):
           int(input('How much will you like to withdraw?'))
           print('Take Your Cash')

        if (selected_option == 2):
            int(input('How much would you like to deposit?'))
            print('The Current Balance')

        if (selected_option == 3):
            input('What issue will you like to report?')
            print('Thank you for contacting us')

    else:
        print('Wrong password inputted')
else:
    print('User cannot be found')
