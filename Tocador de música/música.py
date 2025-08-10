import time
import sys
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("sza.mp3")
pygame.mixer.music.play()
pygame.event.wait()


def good_days():
        print('\n\n')
        sza_lines = [ 
                ('\033[1;31mGood day living in my mind', 0.08), #delay entre as letras
                ('\033[38;5;208mGotta get right', 0.07),
                ('\033[1;93mTryna free my mind before the end of the world', 0.05),
                ("\033[1;32mI don't miss no ex, I don't miss no text", 0.04),
                ('\033[1;34mI choose not to respond', 0.05), #quarto delay
                ("\033[1;96mI don't regret, just pretend shit never happened", 0.06),
                ("\033[1;95mHalf of us layin' waste to our youth, it's in the present", 0.06),
                ('\033[38;2;255;105;180mNa-na, na-na, na-na, na', 0.16)
        ]
        print('\n\n\n\n\n\n')

        delays=[0.2, 0.07, 0.5, 0.5, 0.5, 0.195, 0.7] #delay entre linhas

        for i, (lines, char_delay) in enumerate(sza_lines):
                for char in lines:
                        print(char, end="")
                        sys.stdout.flush()
                        time.sleep(char_delay)
                print()
                time.sleep(delays[i])
good_days()