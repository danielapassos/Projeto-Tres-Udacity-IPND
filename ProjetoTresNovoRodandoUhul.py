# -*- coding: cp1252 -*-

oi="Bem vindo ao nosso jogo, vamos lá!"

name = raw_input('''Fiz este jogo em inglês, espero que não se importe!
                     Qual é seu nome?''')

'''the 1st phrase will be'''
easy_string = '''Today is a very 1 day, to keep myself hydrated
I need to drink some 2. I want to stay 3 to mantain my physique
so I'll eat that long and yellow fruit called 4'''

'''2nd phrase:'''
medium_string = '''I love to 1 movies so when I feel like going 2,
I go to the 3 with my friends, when I don't, I stay home and watch 4.'''

'''3rd phrase:'''
hard_string = '''Let's talk about traveling. Can you guess which places
I'm talking about? In South America, the biggest country is 1. It has 
lot's of sunny 2. The Uncle Sam's country is 3 and it's capital is 4.'''

'''Here, I'll define 3 lists of 4 words to complete the phrases,
each list is a level's list'''
easylist = ["warm", "water", "healthy", "banana"]
mediumlist = ["watch", "out", "movies", "netflix"]
hardlist = ["Brazil", "beaches", "United States", "Washington DC"]


quizes = [easy_string, medium_string, hard_string]
answers = [easylist, mediumlist, hardlist]
possibilities = [easylist, mediumlist, hardlist]
spaces = [1, 2, 3, 4]


'''A list of levels to play the game.'''
my_level = ["easy", "medium", "hard"]

'''So the user will be allowed to choose, for this I'll
 use the function called raw_input.'''


def choose_lvl():
    lvl = raw_input(name + ' choose your level: you can play easy'
                    ', medium or hard').lower()
    if lvl == "easy":
        print "You chose the EASY level"
        return easy_string, easylist
    elif lvl == "medium":
        print "You chose the MEDIUM level"
        return medium_string, mediumlist
    elif lvl == "hard":
        print "You chose the HARD level"
        return hard_string, hardlist
    else:
        print 'This is not a level, please choose correctly'
        return choose_lvl()


'''enquanto o que for escrito depois da pergunta, como resposta,
 passa por aqui, e se a a resposta dada for igual as_resposta,
vai printar o resultado, se não, vai
mandar uma mensagem e voltar para a proxima correção'''


def correction(answers):
    indice = 0
    while indice < len(answers):
        if resposta == possibilities[indice]:
            print answers[indice]
            indice +=1
            return answers[indice]
        else:
            "\nSorry, try again.\n"

'''
Início do jogo, dá uma saudação ao jogador e pede as respostas.
'''

def guess_what():
    print oi
    indice=0
    quizes, answers = choose_lvl()
    print quizes
    for blank in spaces:
        resposta = raw_input(name + ", complete the blank " + str(spaces[indice]) +" :").lower()
        if resposta == answers[indice]:
            #resposta = correction(resposta)
            print "\nCorrect! YAY!!!!\n"
            indice +=1
        else:
            print "Sorry, your answer is wrong. Let's start again?"
    print "Yay, you made it :) Let's go to the next level?"
    return guess_what()

guess_what()
