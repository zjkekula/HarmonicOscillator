import pygame
from pygame.locals import *
from pygame import mixer
import keyboard
#apt-get install -y kmod kbd
import random
from time import sleep
import numpy as np


pygame.init()
width = 1000
height = 500
window = pygame.display.set_mode((width,height))
bg_img = pygame.image.load('ImageBg.jpeg')
bg_img = pygame.transform.scale(bg_img,(width,height))
 
runing = True
while runing:
    window.blit(bg_img,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            runing = False
    pygame.display.update()
pygame.quit()

# assign keyboard letters to notes (C, D, E, F, G, A, B)
notes = {
    'a': 'C',
    's': 'D',
    'd': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'A',
    'j': 'B'
}

# define quantum algorithms (Pauli X, Y, Z, Hadamard, CNOT, SWAP, Phase, T, controlled Z, Toffoli)
algorithms = {
    'x': 'Pauli X',
    'y': 'Pauli Y',
    'z': 'Pauli Z',
    'h': 'Hadamard',
    'c': 'CNOT',
    's': 'SWAP',
    'p': 'Phase',
    't': 'T',
    'cz': 'controlled Z',
    'to': 'Toffoli'
}

# initialize game
print("Welcome to Harmonic Oscillator! Press the corresponding letter key to play the matching note.")
print("As the algorithm scrolls down, press the correct sequence of keys to play the song.")
print("If you play the correct sequence, the algorithm's corresponding visual (Bloch sphere rotation) will play.")
print("If you play the incorrect sequence, the waveform will collapse (decoherence).")

# start game loop
while True:
    # randomly select an algorithm
    algorithm = algorithms[random.choice(list(algorithms.keys()))]
    print("Algorithm: " + algorithm)
    
    # define correct sequence of notes for algorithm
    correct_sequence = []
    if algorithm == 'Pauli X':
        correct_sequence = ['C', 'E', 'G']
    elif algorithm == 'Pauli Y':
        correct_sequence = ['D', 'F', 'A']
    elif algorithm == 'Pauli Z':
        correct_sequence = ['E', 'G', 'B']
    elif algorithm == 'Hadamard':
        correct_sequence = ['C', 'D', 'E']
    elif algorithm == 'CNOT':
        correct_sequence = ['F', 'A', 'C']
    elif algorithm == 'SWAP':
        correct_sequence = ['G', 'B', 'D']
    elif algorithm == 'Phase':
        correct_sequence = ['A', 'C', 'E']
    elif algorithm == 'T':
        correct_sequence = ['B', 'D', 'F']
    elif algorithm == 'controlled Z':
        correct_sequence = ['C', 'D', 'E']
    elif algorithm == 'Toffoli':
        correct_sequence = ['F', 'G', 'A']
        

    # initialize user input sequence
    user_sequence = []

    sleep(15)

    # start algorithm loop
    while len(user_sequence) < len(correct_sequence):
        # get user input
        user_input = keyboard.read_event()
        if user_input.name in notes.keys():
            # add user input to sequence
            user_sequence.append(notes[user_input.name])
           