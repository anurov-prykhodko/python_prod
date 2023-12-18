import pygame
pygame.init()

HEIGHT = 300
WIDTH = 500
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = 'dark orange'
FPS = pygame.time.Clock()

player_size = (20, 20)
player_speed = [1, 1]

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.Surface(player_size)
player_rect = player.get_rect()
player.fill(COLOR_ORANGE)

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if player_rect.bottom >= HEIGHT:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH:
        player_speed[0] = -player_speed[0]

    if player_rect.top <= 0:
        if player_speed != [1, 1]:
            player_speed[1] = -player_speed[1]
        else:
            player_speed[0] = -player_speed[0]

    if player_rect.left <= 0:
        player_speed[0] = -player_speed[0]

    main_display.fill(COLOR_BLACK)
    main_display.blit(player, player_rect)
    player_rect = player_rect.move(player_speed)
    pygame.display.flip()