#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
'''
Author:Chris Moran
Contact:chris@equalreality.com
Date:2019/06/28
Licence: GPLv3
Version:0.1
How Do You Feel - Terminal application
This application is designed to track a users mood
and display relevant quotes to the user depending on their mood.
'''

import json
import random
import argparse

DIRECTORY = '/Users/chrismoran/projects/Terminal-app/src'

def emotion_list(filename):
    '''
    Reads the contents of a .txt file
    '''
    text = []
    with open(filename, 'r') as file:
        for line in file:
            text.append(line.strip())
        return text

def input_checker(word):
    '''
    Takes the user input and checks if it is a string.
    If it is a string, it converts to lower case.
    If not a string, returns invalid input.
    '''
    try:
        return word.lower()
    except AttributeError:
        return None

def quote_display(mood):
    '''
    Takes user input of mood and prints a random quote from the relevant mood list.
    '''
    try:
        emotion_dict = file_to_dict('emotion-dict.json')
        print('\n' +random.choice(emotion_dict[mood]))
    except FileNotFoundError:
        print('The emotion dictionary file is not present')
        print('Please relocate the file and restart the application')
        exit()

def file_to_string(filename):
    '''
    Returns text from a file named 'filename'.
    '''
    with open(filename, 'r') as file:
        text = file.read()
        return text

def file_to_dict(filename):
    '''
    uses 'file_to_text' to load json as string then converts string to a dictionary
    '''
    dict_str = file_to_string(filename)
    emotion_dict = json.loads(dict_str)
    return emotion_dict

def emotion_counter(mood):
    '''
    Takes user input of mood and writes it to emotion_counter.txt
    '''
    try:
        with open('emotion-counter.txt', 'a+') as file:
            file.write(mood + '\n')
    except FileNotFoundError:
        print('The emotion counter file is not present')
        print('Please relocate the file and restart the application')
        exit()

def track_mood():
    '''
    Prints a list of the number of times moods have been chosen by the user in the past
    '''
    try:
        with open('emotion-counter.txt', 'r') as file:
            text = file.read()
        counts = dict()
        words = text.split()
    except FileNotFoundError:
        print('The emotion list file is not present')
        print('Please relocate the file and restart the application')
        exit()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print('\nYour emotion count is as follows:\n')
    for word in counts:
        print('  ', word, counts[word])
    second_menu()

def select_mood():
    '''
    Prints a menu of available moods that a quote can be added to
    User input selects the mood to add quote to dictionary
    '''
    print('\nWhat emotion do you want to add to?\n')
    emotions = emotion_list('emotion-list.txt')
    try:
        for emotion in emotions:
            print(emotion)
    except FileNotFoundError:
        print('The emotion list file is not present')
        print('Please relocate the file and restart the application')
        exit()
    while True:
        user_input = input('\nChose your emotion: ')
        if user_input in emotions:
            add_quote(user_input)
        else:
            print('\nInvalid input, please try again')

def add_quote(emotion):
    '''
    This appends the quote from the user to the relevant list in the emotion-dict.json file
    '''
    quote_add = input('\nWhat quote would you like to add\n\n: ')
    try:
        with open('emotion-dict.json', 'r') as file:
            text = json.load(file)
    except FileNotFoundError:
        print('The emotion list file is not present')
        print('Please relocate the file and restart the application')
        exit()
    with open('emotion-dict.json', 'w') as file:
        text[emotion].append(quote_add)
        json.dump(text, file)
    print(f'\nYour new quote has been successfully added to the emotion **{emotion}**.\n')
    second_menu()

def second_menu():
    '''
    Menu for secondary features.
    Prompts for user input.
    '''
    print('\nWhat else would you like to do?\n')
    print('[T]rack mood\n[A]dd Quote\n[E]xit\n')
    while True:
        user_input = input(':')
        if input_checker(user_input) == 't' or input_checker(user_input) == 'track mood':
            track_mood()
        elif input_checker(user_input) == 'a' or input_checker(user_input) == 'add quote':
            select_mood()
        elif input_checker(user_input) == 'e' or input_checker(user_input) == 'exit':
            exit()
        else:
            print('\nInvalid response. Please try again\n')

def main_menu(emotion=None):
    '''
    Displays a welcome message and provides a list of possible emotions
    for the user to base their input on.
    Takes a 'mood' of type 'string' as an argument.
    'Mood' is only valid input if it matches the list
    '''
    if emotion is None:
        print('\n\nWelcome to How Do You Feel Terminal Application\n\n')
        print('How are you feeling today?\n')
        emotions = emotion_list('emotion-list.txt')
        try:
            for emo in emotions:
                print(emo)
        except FileNotFoundError:
            print('The emotion list file is not present')
            print('Please relocate the file and restart the application')
            exit()
        while True:
            user_input = input('\n:')
            if user_input in emotions:
                quote_display(user_input)
                emotion_counter(user_input)
                second_menu()
            else:
                print('Invalid input. Please check you spelling and try again')
    else:
        quote_display(emotion)
        emotion_counter(emotion)
        second_menu()

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    EMOTION_HELP = emotion_list('emotion-list.txt')
    PARSER.add_argument('-e', '--emotion', help=f'Your available emotions are {EMOTION_HELP}')
    ARGS = PARSER.parse_args()
    if not ARGS.emotion:
        main_menu()
    elif ARGS.emotion in EMOTION_HELP:
        main_menu(ARGS.emotion)
    else:
        print('Input not valid. See help for available emotions')
        exit()

main_menu()
