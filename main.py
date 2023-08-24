'''
Title: Guess-The-Number
Author: Jatzylap
Version: 1.0
'''

import pygame
import random as r
import time
import zipfile as z
import io
import cv2

ZIP = 'src/a/a.zip'
VIDEO = 'src/a/matrix.mp4'
WINDOW_NAME = 'Guess The Number'
text_input = ['x', 'x']

with z.ZipFile(ZIP) as zip_ref:
    content = zip_ref.namelist()

with z.ZipFile(ZIP) as zip_ref:
    read1 = zip_ref.read(content[0])
    read2 = zip_ref.read(content[1])
    read3 = zip_ref.read(content[2])
    read4 = zip_ref.read(content[3])
    read5 = zip_ref.read(content[4])
    read6 = zip_ref.read(content[5])
    read7 = zip_ref.read(content[6])
    read8 = zip_ref.read(content[7])
    read9 = zip_ref.read(content[8])
    read10 = zip_ref.read(content[9])
    read11 = zip_ref.read(content[10])
    read12 = zip_ref.read(content[11])
    read13 = zip_ref.read(content[12])
    read14 = zip_ref.read(content[13])
    read15 = zip_ref.read(content[14])

    data_1 = io.BytesIO(read1)
    data_2 = io.BytesIO(read2)
    data_3 = io.BytesIO(read3)
    data_4 = io.BytesIO(read4)
    data_5 = io.BytesIO(read5)
    data_6 = io.BytesIO(read6)
    data_7 = io.BytesIO(read7)
    data_8 = io.BytesIO(read8)
    data_9 = io.BytesIO(read9)
    data_10 = io.BytesIO(read10)
    data_11 = io.BytesIO(read11)
    data_12 = io.BytesIO(read12)
    data_13 = io.BytesIO(read13)
    data_14 = io.BytesIO(read14)
    data_15 = io.BytesIO(read15)   

def main():
    pygame.init()
    pygame.display.set_caption(WINDOW_NAME)

    video = cv2.VideoCapture(VIDEO)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    screen = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    correct = pygame.image.load(data_1).convert_alpha()
    end = pygame.image.load(data_2).convert_alpha()
    error1 = pygame.image.load(data_3).convert_alpha()
    error2 = pygame.image.load(data_4).convert_alpha()
    exit_button = pygame.image.load(data_5).convert_alpha()
    exit_button_hover = pygame.image.load(data_6).convert_alpha()
    guideline = pygame.image.load(data_7).convert_alpha()
    level = pygame.image.load(data_8).convert_alpha()
    number = pygame.image.load(data_9).convert_alpha()
    record = pygame.image.load(data_10).convert_alpha()
    shadow = pygame.image.load(data_11).convert_alpha()
    start_button = pygame.image.load(data_12).convert_alpha()
    start_button_hover = pygame.image.load(data_13).convert_alpha()
    title = pygame.image.load(data_14).convert_alpha()
    welcome = pygame.image.load(data_15).convert_alpha()

    # Boxes
    start_button_rect = pygame.Rect(100, 300, 545, 217)
    exit_button_rect = pygame.Rect(650, 300, 545, 217)
    input_rect = pygame.Rect(548, 440, 200, 111)

    # Runtime
    loop = True
    menu = True
    gaming = False
    win = False
    enter = False
    guesses = 0
    caret = 0
    scale = 1
    digits = 0

    while loop:

        if menu:

            clock.tick(fps)
            success, video_image = video.read()
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
            else:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
            screen.blit(video_surf, (0, 0))
            screen.blit(title,(250, 20))
            screen.blit(shadow,(100, 280))
            screen.blit(start_button,(100, 300))
            screen.blit(exit_button,(650, 300))
    
            if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(start_button_hover,(100, 300))
            if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(exit_button_hover,(650, 300))

        if gaming:

            # Levels
            if lvl == 0 and not win:
                screen.fill((100,100,100))
                screen.blit(pygame.transform.scale(welcome,(1000,285)),(115,130),(0,0,800,228))
                pygame.display.flip()
                attempts = 3
                secret_num = r.randint(0,1)
                print("Secret Number: ",secret_num,"Scale: ",scale)
                start_time = time.time()
                while time.time() - start_time < 3:
                    pass
                lvl = 1

            if lvl == 1:
                screen.fill((100,100,100))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(90,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(30,0,30,26))

            if lvl == 2:
                screen.fill((0,180,0))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(180,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(60,0,30,26))

            if lvl == 3:
                screen.fill((0,200,200))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(270,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(90,0,30,26))

            if lvl == 4:
                screen.fill((230,230,0))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(360,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(120,0,30,26))

            if lvl == 5:
                screen.fill((0,100,200))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(450,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(150,0,30,26))

            if lvl == 6:
                screen.fill((255,100,255))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(540,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(180,0,30,26))

            if lvl == 7:
                screen.fill((255,100,0))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(630,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(210,0,30,26))

            if lvl == 8:
                screen.fill((255,0,255))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(720,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(240,0,30,26))

            if lvl == 9:
                screen.fill((128,0,0))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(830,91),(810,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(270,0,30,26))

            if lvl == 10:
                screen.fill((0,0,0))
                screen.blit(guideline,(220,240))
                screen.blit(pygame.transform.scale(number,(900,79)),(770,91),(90,0,90,79))
                screen.blit(pygame.transform.scale(number,(900,79)),(840,91),(0,0,90,79))
                screen.blit(pygame.transform.scale(number,(300,26)),(878,294),(0,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(990,294),(30,0,30,26))
                screen.blit(pygame.transform.scale(number,(300,26)),(1015,294),(0,0,30,26))

            if lvl >= 1:

                # Register attempt
                screen.blit(level,(170,50),(0,0,800,176))
                pygame.draw.rect(screen, 'black', input_rect)
                if enter and not text_box == ['x','x']:
                    if digits == 1:
                        answer = text_box[0]
                    if digits == 2:
                        answer = int(''.join(map(str,text_box)))
                    if secret_num > answer:
                        screen.blit(pygame.transform.scale(error1,(400,114)),(450,565),(0,0,800,228))
                        pygame.display.flip()
                        attempts -= 1
                        guesses += 1
                    if secret_num < answer:
                        screen.blit(pygame.transform.scale(error2,(400,114)),(450,565),(0,0,800,228))
                        pygame.display.flip()
                        attempts -= 1
                        guesses += 1
                    if secret_num == answer:
                        attempts = 3
                        guesses += 1
                        screen.blit(pygame.transform.scale(correct,(400,114)),(450,565),(0,0,800,228))
                        pygame.display.flip()
                        if lvl == 10: lvl = 0; win = True; gaming = False
                        if lvl <= 9: scale += 1; lvl += 1; text_box = ['x','x']; secret_num = r.randint(0,scale)
                    if attempts == 0 and not win: lvl = '?'; guesses = 0; menu = True; gaming = False
                    start_time = time.time()
                    while time.time() - start_time < 2:
                        pass
                    enter = False
                    print("Secret Number: ",secret_num,"Scale: ",scale)

                # Text indicator
                if text_input == ['x','x']:
                    caret_rect = pygame.Rect(643, 450, 10, 90)
                elif type(text_input[0]) is int and text_input[1] == 'x':
                    caret_rect = pygame.Rect(683, 450, 10, 90)
                elif type(text_input[0]) and type(text_input[1]) is int:
                    caret_rect = pygame.Rect(728, 450, 10, 90)
                caret += 0.01
                if caret <= 4:
                    pygame.draw.rect(screen, 'white', caret_rect)
                if caret >= 8:
                    caret = 0
    
                # Text input
                if type(text_input[0]) is int and type(text_input[1]) is str:
                    digits = 1
                    if text_input[0] == 0:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(0,0,90,79))
                    if text_input[0] == 1:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(90,0,90,79))
                    if text_input[0] == 2:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(180,0,90,79))
                    if text_input[0] == 3:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(270,0,90,79))
                    if text_input[0] == 4:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(360,0,90,79))
                    if text_input[0] == 5:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(450,0,90,79))
                    if text_input[0] == 6:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(540,0,90,79))
                    if text_input[0] == 7:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(630,0,90,79))
                    if text_input[0] == 8:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(720,0,90,79))
                    if text_input[0] == 9:
                        screen.blit(pygame.transform.scale(number,(900,79)),(600,458),(810,0,90,79))
    
                if type(text_input[0]) and type(text_input[1]) is int:
                    digits = 2
                    if text_input[0] == 0:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(0,0,90,79))
                    if text_input[0] == 1:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(90,0,90,79))
                    if text_input[0] == 2:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(180,0,90,79))
                    if text_input[0] == 3:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(270,0,90,79))
                    if text_input[0] == 4:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(360,0,90,79))
                    if text_input[0] == 5:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(450,0,90,79))
                    if text_input[0] == 6:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(540,0,90,79))
                    if text_input[0] == 7:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(630,0,90,79))
                    if text_input[0] == 8:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(720,0,90,79))
                    if text_input[0] == 9:
                        screen.blit(pygame.transform.scale(number,(900,79)),(555,458),(810,0,90,79))
                    if text_input[1] == 0:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(0,0,90,79))
                    if text_input[1] == 1:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(90,0,90,79))
                    if text_input[1] == 2:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(180,0,90,79))
                    if text_input[1] == 3:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(270,0,90,79))
                    if text_input[1] == 4:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(360,0,90,79))
                    if text_input[1] == 5:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(450,0,90,79))
                    if text_input[1] == 6:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(540,0,90,79))
                    if text_input[1] == 7:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(630,0,90,79))
                    if text_input[1] == 8:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(720,0,90,79))
                    if text_input[1] == 9:
                        screen.blit(pygame.transform.scale(number,(900,79)),(645,458),(810,0,90,79))

        pygame.display.flip()

        if win:
            guesses = str(guesses)
            screen.fill((100,100,100))
            screen.blit(pygame.transform.scale(end,(1000,285)),(115,130),(0,0,800,228))
            screen.blit(pygame.transform.scale(record,(1000,285)),(125,390),(0,0,1000,285))

            for g in range(len(guesses)):
                print("You correctly guessed the number ",guesses," times")
                if g == 0:
                    if guesses[0] == '0':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(0,0,30,33))
                    if guesses[0] == '1':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(30,0,30,33))
                    if guesses[0] == '2':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(60,0,30,33))
                    if guesses[0] == '3':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(90,0,30,33))
                    if guesses[0] == '4':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(120,0,30,33))
                    if guesses[0] == '5':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(150,0,30,33))
                    if guesses[0] == '6':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(180,0,30,33))
                    if guesses[0] == '7':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(210,0,30,33))
                    if guesses[0] == '8':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(240,0,30,33))
                    if guesses[0] == '9':
                        screen.blit(pygame.transform.scale(number,(300,33)),(900,508),(270,0,30,33))
                else:
                    if guesses[1] == '0':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(0,0,30,33))
                    if guesses[1] == '1':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(30,0,30,33))
                    if guesses[1] == '2':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(60,0,30,33))
                    if guesses[1] == '3':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(90,0,30,33))
                    if guesses[1] == '4':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(120,0,30,33))
                    if guesses[1] == '5':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(150,0,30,33))
                    if guesses[1] == '6':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(180,0,30,33))
                    if guesses[1] == '7':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(210,0,30,33))
                    if guesses[1] == '8':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(240,0,30,33))
                    if guesses[1] == '9':
                        screen.blit(pygame.transform.scale(number,(300,33)),(925,508),(270,0,30,33))

            pygame.display.flip()
            start_time = time.time()
            while time.time() - start_time < 4:
                pass
            guesses = 0
            win = False
            menu = True

        # Event listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if menu:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos
                    if start_button_rect.collidepoint(click_x, click_y):
                        lvl = 0
                        gaming = True
                        menu = False
                    if exit_button_rect.collidepoint(click_x, click_y):
                        loop = False
            if gaming:
                cursor = True
                enter = False
                text_box = []
                if event.type == pygame.KEYDOWN:
                    for key in range(len(text_input)):
                        if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                            if type(text_input[key]) is int and cursor:
                                enter = True
                                text_box.append(text_input[key])
                                text_input[key] = 'x'
                                print(text_input)
                    for key in range(len(text_input)):
                        if event.key == pygame.K_BACKSPACE:
                            if type(text_input[key]) is int and cursor:
                                text_input[key] = 'x'
                                print(text_input)
                        if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 0
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 1
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 2
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 3
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 4
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 5
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 6
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                           if text_input[key] == 'x' and cursor:
                               text_input[key] = 7
                               print(text_input)
                               cursor = False
                        if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 8
                                print(text_input)
                                cursor = False
                        if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            if text_input[key] == 'x' and cursor:
                                text_input[key] = 9
                                print(text_input)
                                cursor = False

    pygame.quit()

if __name__ == '__main__':
    main()