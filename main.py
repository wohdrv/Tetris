import pygame, sys
from game import Game
from colors import Colors
import time

pygame.init()

font = pygame.font.Font('PressStart2P.ttf', 20)
title_font = pygame.font.Font('PressStart2P.ttf', 20)
play1 = title_font.render("Нажмите Enter,", True, Colors.white)
play2 = title_font.render("Чтобы начать играть", True, Colors.white)
game_over = title_font.render("Игра окончена :(", True, Colors.white)
score = font.render("Счет:", True, Colors.white)
next1 = font.render("Следующая", True, Colors.white)
next2 = font.render("фигура:", True, Colors.white)

score_box = pygame.Rect(350, 190, 170, 60)
next_box = pygame.Rect(350, 360, 170, 170)

# параметры:
res = (550, 640)
start = 0
ticks = 500
first_start = 1

logo = pygame.image.load("logo.bmp")
logo_scale = pygame.transform.scale(logo, (195, 64))

tree = pygame.image.load("tree.bmp")
tree_scale = pygame.transform.scale(tree, (175, 175))

#background = pygame.image.load("background.bmp")
#bkg_scale = pygame.transform.scale(background, (550, 650))

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Tetris by wohdrv")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, ticks)
print("Now lvl speed is", ticks)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                if event.key == pygame.K_RETURN:
                    game.game_over = False
                    game.reset()
                    ticks = 500
                    first_start = 0
                    game.lvl_point = 0
                    pygame.time.set_timer(GAME_UPDATE, ticks)
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.down()
        if game.lvl_point == 20:
            ticks -= 50
            pygame.time.set_timer(GAME_UPDATE, ticks)
            game.lvl_point -= 20
            print("time reduced in 50. Now is", ticks)

    if game.game_over == True and first_start == 1: #Меню
        logo_scale = pygame.transform.scale(logo, (391, 128))
        screen.fill(Colors.dark_state_blue)
        #screen.blit(bkg_scale, (0, 0))
        screen.blit(tree_scale, (190, 350))
        screen.blit(logo_scale, (85, 100))
        screen.blit(play1, (130, 280, 50, 50))
        screen.blit(play2, (80, 300, 50, 50))

    elif game.game_over == True: #Игра окончена
        time.sleep(1)
        screen.fill(Colors.dark_state_blue)
        screen.blit(tree_scale, (190, 350))
        screen.blit(game_over, (100, 200, 50, 50))

    else:
        score_value = font.render(str(game.score), True, Colors.white)

        logo_scale = pygame.transform.scale(logo, (195, 64))
        screen.fill(Colors.dark_state_blue)
        screen.blit(logo_scale, (340, 50))
        screen.blit(score, (390, 150, 50, 50))
        screen.blit(next1, (347, 300, 50, 50))
        screen.blit(next2, (375, 325, 50, 50))

        pygame.draw.rect(screen, Colors.state_blue, score_box, 0, 10)
        screen.blit(score_value, score.get_rect(centerx = score_box.centerx + 40, centery = score_box.centery))
        pygame.draw.rect(screen, Colors.state_blue, next_box, 0, 10)

    game.draw(screen)

    pygame.display.update()
    clock.tick(60)