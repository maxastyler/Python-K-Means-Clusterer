import pygame
import sys
from extractor import *
screen_size=(640, 480)
try:
    num_colours=int(sys.argv[2])
except:
    num_colours=6
extract_size=(200, 200)
difference=1
vmin=0.1
vmax=0.9

def main():
    pygame.init()
    screen=pygame.display.set_mode(screen_size)
    print(prepare_for_terminal(str(sys.argv[1]), True))

    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                break
        screen.fill((0, 0, 0))

        for i in range(len(colours)):
            this_rect=pygame.Rect(i*screen_size[0]/len(colours), 0, screen_size[0]/len(colours), screen_size[1])
            pygame.draw.rect(screen, colours[i], this_rect)


        pygame.display.flip()
    pygame.quit()

if __name__=='__main__':
    sys.exit(main())
