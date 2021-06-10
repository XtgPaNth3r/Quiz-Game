def mq(q, a):
    print(q)
    x = input('What do you think the answer is? ').lower()
    if x == a.lower():
        print('You got it correct :) \n\n\n')
    elif x == 'quit':
        quit()
    else:
        print('Incorrect! Next Question!\n\n\n')
        
# to make a question type mk('Your Question', 'your answer')
# quotes are manditory and so are he brackets and the colon
mq('Are houses cheaper in USA than in Canada? ', 'Yes')
mq('Who made minecraft? ', 'Notch')
mq('Is Arjun 5 feet tall yet? ', 'No')
