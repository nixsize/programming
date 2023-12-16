import pygame

pygame.init()
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
x, y = width // 2 - 5, height // 2 - 5
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
currentColor = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y > 0:
                    y -= 10
            elif event.key == pygame.K_DOWN:
                if y + 10 < height:
                    y += 10
            elif event.key == pygame.K_LEFT:
                if x > 0:
                    x -= 10
            elif event.key == pygame.K_RIGHT:
                if x + 10 < width:
                    x += 10
            elif event.key == pygame.K_c:
                currentColor = (currentColor + 1) % len(colors)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colors[currentColor], (x, y, 10, 10))
    pygame.display.flip()
pygame.quit()