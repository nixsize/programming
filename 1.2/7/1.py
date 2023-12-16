import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("enter")
            elif event.key == pygame.K_SPACE:
                print("space")
            elif event.key == pygame.K_w:
                print("w")
            elif event.key == pygame.K_a:
                print("a")
            elif event.key == pygame.K_s:
                print("s")
            elif event.key == pygame.K_d:
                print("d")
            elif event.key == pygame.K_ESCAPE:
                print("esc")
            elif event.key == pygame.K_UP:
                print("up arrow")
            elif event.key == pygame.K_DOWN:
                print("down arrow")
            elif event.key == pygame.K_LEFT:
                print("left arrow")
            elif event.key == pygame.K_RIGHT:
                print("right arrow")
pygame.quit()