from random import *
from pynput import keyboard
### Dicts and Variables
Letters = {
 1:'A',   2:'B',    3:'C',    4:'D',    5:'E',    6:'F',    7:'G',    8:'H',    9:'I',    10:'J',
11:'K',  12:'L',   13:'M',   14:'N',   15:'O',   16:'P',   17:'Q',   18:'R',   19:'S',    20:'T',
21:'U',  22:'V',   23:'W',   24:'X',   25:'Y',   26:'Z',   27:'?',   28:'.',   29:',',    30:"'",
31:';',  32:' ',   33:'!',   34:'-',   35:'(',   36:')',   37:'[',   38:']',   39:'{',    40:'}',
41:'"',
}
#   print(Letters[randint(1,26)])   # [DEBUG]
passage = 0
current = 0
Messages = {
'exit': (
'''
Thank you for your stay within our halls,
We await your return.
'''
),
'bongo': (
'''
PRAISE THE ALMIGHT LORD OF PURPLE, FAMILIAR TO THE ALMIGHT DANDYFUL FATHER
'''
),
}
book = {}
print(
'''
Welcome to the House of Babylon, a program that generates random text pages. 
Each page consists of 500 randomly selected characters from the English alphabet, including spaces and punctuation. 

If you want to try decode some of the secrets of the House of Babylon then press the left shift.
please note due to the current method of reading inputs typing may be a little slow. I should be able to fix it soon.

Press arrow keys to view all generated pages.
Press the down arrow to generate a new page.
To exit the program, press Escape.
''')
### Functions
def scribe():
    global current, passage
    string = []
    a = 500
    while a > 0:
        string.append(Letters[randint(1,41)])
        a -= 1
    page = ''.join(string)
    current = passage
    book[current] = page
    print('Passage ' + str(passage) + '\n' + page + '\n')

def previous_passage():
    global passage, current
    if current > 1 and current <= passage:
        current -= 1
        print('Passage ' + str(current) + '\n' + book[current] +'\n')
    else:
        print("There is no passage 0 here, maybe in the future we'll work on one.")

def next_passage():
    global passage, current
    if current < passage:
        current += 1
        print('Passage ' + str(current) + '\n' + book[current] +'\n')
    else:
        print("If you have yet to write the passage does it truly exist?")

def on_press(key):
    global passage
    if key == keyboard.Key.down:
        try:
            passage += 1
            scribe()
        except:
            print('ERROR')
    if key == keyboard.Key.esc:
        print(Messages['exit'])
        return False
    if key == keyboard.Key.shift_l:
        secret = input('Input secrets: ')
        print(Messages[secret.lower()])
    if key == keyboard.Key.left:
        previous_passage()
    if key == keyboard.Key.right:
        next_passage()

### Literally just to read keyboard input
with keyboard.Listener(
        on_release=on_press
        ) as listener:
    listener.join()
