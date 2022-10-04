import hashlib
import os
import random
import multiprocessing
import datetime
print('''''8                    8                                   8                   
8                    8                                   8                   
8oPYo. .oPYo. .oPYo. 8oPYo.   .oPYo. oPYo. .oPYo. .oPYo. 8  .o  .oPYo. oPYo. 
8    8 .oooo8 Yb..   8    8   8    ' 8  `' .oooo8 8    ' 8oP'   8oooo8 8  `' 
8    8 8    8   'Yb. 8    8   8    . 8     8    8 8    . 8 `b.  8.     8     
8    8 `YooP8 `YooP' 8    8   `YooP' 8     `YooP8 `YooP' 8  `o. `Yooo' 8     
..:::..:.....::.....:..:::..:::.....:..:::::.....::.....:..::...:.....:..::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::''')
while True:
    wordlist = input('wordlist:')
    if os.path.exists(wordlist):
        break
    else:
        print('[+]enter a valid path')
count = 0
lis = list(hashlib.algorithms_available)
lis.remove('shake_256')
lis.remove('shake_128')
for word in lis:
    print(f'[{count}]{word}')
    count += 1
print('[99]---check_for_all_algorithms(unstable)---')
  

while True:
    try:
        algo = int(input('enter the algorithm:'))
    except ValueError:
        print('[+]please enter a number')
        continue
    if algo > len(lis) - 1 and algo != 99:
        print('[+]please enter a valid number')
    else:
        
        if algo != 99:
            algo_str = lis[algo]
        break

hashh = input('hash:')
liss = []
file = open(wordlist,encoding='latin1')
lines = file.readlines()
for line in lines:
        
    refined_word = line.replace('\n', '')
    liss.append(refined_word)
file.close()
if algo != 99:
    print('[+]please wait...')
    print(f'[+]total_words = {len(liss)}\n[+]date = {datetime.datetime.now()}')

    for word in liss:
        if hashh == hashlib.new(algo_str,word.encode()).hexdigest():
            print('[+]HASH SUCCESSFULLY CRACKED')
            print('-'*33)
            print(f'[+]HASH={hashh}\n[+]PLAIN_TEXT={word}\n[+]ALGORITHM={algo_str}')
            print('-'*33)
            exit()

    print('-'*33)
    print('[+]HASH NOT IN WORDLIST')
    print('-'*33)
    exit()

def gay(alg):
    global lis
    global liss
    global used_alg
  

    for word in liss:
        try:
            hashed_word = hashlib.new(lis[alg],word.encode()).hexdigest()
            if hashh == hashed_word:
                print('[+]HASH SUCCESSFULLY CRACKED')
                print('-'*33)
                print(f'[+]HASH={hashh}\n[+]PLAIN_TEXT={word}\n[+]ALGORITHM = {lis[alg]}')
                print('-'*33)
                exit()
        except  Exception as e:
            print(e)
           
length_algo = len(lis) -1
#print('please wait...')
print(f'[+]total_words = {len(liss)}\n[+]date = {datetime.datetime.now()}')
for word in lis:
    if length_algo == -1:
        break
    t1 = multiprocessing.Process(target=gay,args=[length_algo])
    t1.start()
    length_algo = length_algo - 1

