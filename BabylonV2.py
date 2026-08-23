### Read Me:
'''
Trying to make an app for the house of babylon python code
'''
### Libraries
import pygame, os
from random import *
### Setup
pygame.init()
pygame.display.set_caption('House of Babylon V2')
screen = pygame.display.set_mode((550,680))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.match_font('lucidaconsole'),20)
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
white = (255,255,255)
clicking = False
typing_active = False
input_text = ""
result_text = ""
Running = True
secrets_found = []
book = {
0 : (
'''
Welcome to the House of Babylon, a program that generates random text pages. 
Each page consists of 500 randomly selected characters from the English alphabet, including spaces and punctuation. 

If you want to try decode some of the secrets of the House of Babylon then press the left shift.
please note due to the current method of reading inputs typing may be a little slow. I should be able to fix it soon.

To exit the program, press Escape.
'''
),
}
Messages = {
'exit': (
'''
Thank you for your stay within our halls,
We await your return.
'''
),
}
Secrets = {
'bongo': (
'''
PRAISE THE ALMIGHT LORD OF PURPLE, FAMILIAR TO THE ALMIGHT DANDYFUL FATHER
'''
),
'dandyvt': (
'''
The cutest witch on twitch!!!
'''
),
'test': (
'''
Testing, testing, is this thing on?
'''
),
'shepard': (
'''
Hmmm... something seems just off here
'''
),
'5h3p4rd': (
'''
Thats me, the man of a 1000 projects... Help I think my backlog became sentient
'''
),
'rat': (
''' 
The Jester king? What why? There is nothing to steal in this.
'''
),
'sine': (
''' 
You devilish black cat, I see you there
'''
),
'prometheus': (
''' 
Where did you hear that? 
I mean I think I have spoken to like 5 people about it aside from that it has been rather dead in the water... so to speak.
'''
),
'cathedral': (
''' 
Welcome, welcome. 
Sorry but you only have access to the stoop, inside the scribes are working hard at many projects. 
Some to help other projects, some to help other people, and some to test before we bring them out to you, the public.
'''
),
'purple': (
'''
Oh yeah purple... which one is that? is that the blue that isn't blue?
'''
),
'hastur': (
'''
I love the king in yellow.
It has been an inspiration for some of my projects and it is a genuinely good book. 
I highly recommend it.
'''
),
':)': (
'''
:)
'''
)
}
### Functions
def scribe():
    global current, passage
    passage += 1
    string = [('Passage: ' + str(passage) + '\n')]
    a = 500
    while a > 0:
        string.append(Letters[randint(1,41)])
        a -= 1
    page = ''.join(string)
    current = passage
    book[current] = page
#    print('Passage ' + str(passage) + '\n' + page + '\n')  #[DEBUG]

def previous_passage():
    global passage, current
    if current > 1 and current <= passage:
        current -= 1
    #    print('Passage ' + str(current) + '\n' + book[current] +'\n')  #[DEBUG]
    else:
        pass

def next_passage():
    global passage, current
    if current < passage:
        current += 1
    #    print('Passage ' + str(current) + '\n' + book[current] +'\n')  #[DEBUG]
    else:
        pass
def draw_text(text, font, colour, surface, x, y):
    textobj = font.render(text, 1, colour,wraplength=500)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj,textrect)
    
def secret_math(b):
    global secrets_found
    secrets_found.append(b)
    secrets_found = list(dict.fromkeys(secrets_found))
    return int(len(secrets_found)) + 1
### Rects
text_box = pygame.Rect(20,20,510,400)
button1 = pygame.Rect(20,430,168,30)
button2 = pygame.Rect(191,430,168,30)
button3 = pygame.Rect(362,430,168,30)
secrets = pygame.Rect(20,470,510,30)

while Running:
    screen.fill((20,20,50))
    mx, my = pygame.mouse.get_pos()
    
    pygame.draw.rect(screen,(0,0,0),text_box)
    draw_text(str(book[current]),font,white,screen,25,25)
    draw_text(('Total Passages: ' + str(len(book)-1)),font,white,screen,275,25)
    pygame.draw.rect(screen,(75,75,75),button1)
    draw_text('Previous',font,white,screen,25,435)
    pygame.draw.rect(screen,(75,75,75),button2)
    draw_text('Generate',font,white,screen,196,435)
    pygame.draw.rect(screen,(75,75,75),button3)
    draw_text('Next',font,white,screen,367,435)
    pygame.draw.rect(screen,(75,75,75),secrets)
    draw_text(
        ('Secrets found: '+str(len(secrets_found))+' of '+str(len(Secrets))),
        font,white,screen,260,400
        )
    if typing_active:
        draw_text((">>: "+ input_text),font,white,screen,25,475)
    else:
        draw_text('Secrets',font,white,screen,25,475)
### Events
    clicking = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            Running = False
        if event.type == pygame.K_ESCAPE:
            Running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        if button1.collidepoint((mx,my)):
            if clicking:
                previous_passage()
            #    print('button1')   #[DEBUG]
        if button2.collidepoint((mx,my)):
            if clicking:
                scribe()
            #    print(len(book))   #[DEBUG]
            #    print('button2')   #[DEBUG]
        if button3.collidepoint((mx,my)):
            if clicking:
                next_passage()
            #    print('button3')   #[DEBUG]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if secrets.collidepoint(event.pos):
                typing_active = True
                input_text = ""
        if event.type == pygame.KEYDOWN and typing_active:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                key = input_text.lower()
                if key in Secrets:
                    result_text = Secrets[key]
                    secret_math(result_text)
                else:
                    result_text = '''
Unknown Secret.
                    '''
                input_text = ''
                typing_active = False
            elif event.key == pygame.K_BACKSPACE:
                input_text =  input_text[:-1]
            else:
                input_text += event.unicode
    draw_text(result_text,font,white,screen,25,485)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()