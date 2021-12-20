import time, os, sys

def clrscr():
    if sys.platform == 'win32':
        os.system("cls")
    elif sys.platform == 'linux':
        os.system('clear')

def encryptor(word):
    tor = 0
    t1 = time.time_ns()
    a = "abcdefghijklmnopqrstuvwxyz" * 5
    t2 = time.time_ns()
    print("Time taken to create the alphabet string: ",t2-t1,'nanoseconds.')
    b=''

    # The following for-loop just reverses the order of variable a
    # The coder just got lazy to retype the english alphabets
    for i in range(len(a)-1,0,-1):  
        b=b+a[i]
    output_string = ' '
    # End of for-loop

    new=list(word)      # 'word' is the text to be encryted/decrypted
    for i in range(len(new)):
        if word[i].isalnum():
           continue
        new[i]=' '
    boom = ''.join(new)
    input_list1 = boom.split()
    for single in word:
        list_word = len(input_list1[tor])
        if single.isalpha():
            output_string = output_string + b[(b.index(single) + list_word + 3)]
        else:
            output_string = output_string + single
        if single == ' ':
            if tor <= len(input_list1[tor]):
                tor +=1
    return output_string

def decryptor(word):
    tor = 0
    t1 = time.time_ns()
    a = "abcdefghijklmnopqrstuvwxyz" * 5
    output_string = ' '
    new=list(word)
    for i in range(len(new)):
        if word[i].isalnum():
           continue
        new[i]=' '
    t2 = time.time_ns()
    print("Time taken to create reverse alphabet string: ",t2-t1,'nanoseconds.')
    boom = ''.join(new)      
    input_list1 = boom.split()
    for single in word:
        list_word = len(input_list1[tor])
        if single.isalpha():
            output_string = output_string + a[(a.index(single)+ list_word + 3)]
        else:
            output_string = output_string + single
        if single == ' ':
            if tor <= len(input_list1[tor]):
                tor +=1
    return output_string

while True:
    print('1 Encrypt\n2 Decrypt\n')
    option = str(input("Option number: "))
    clrscr()    
    word = str(input("Text: "))
    t1 = time.time_ns()
    t11 = time.time()
    if option == '1':   
        print('Encrypted Text :', encryptor(word.lower()))
    elif option == '2': 
        print('Decrypted Text :', decryptor(word.lower()))
    else:
        print('ERROR: INCORRECT_OPTION_NUMBER\n Pick either \'1\' or \'2\'')
    t2 = time.time_ns()
    t22 = time.time()
    print('\nTime per single conversion:', t2-t1, "nanoseconds or ",t22-t11, "seconds.\n\n")