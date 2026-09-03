import pygame
from warrior import Warrior
from mage import Mage
from archer import Archer

def draw(surface,p1, p2):
    p1.draw(surface)
    p2.draw(surface)

def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    clock = pygame.time.Clock()


    p1 = Warrior("Bob", 200, 300)
    p2 = Mage("Billy", 600, 300)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # --- Player 1 Input (WASD) ---
        p1_dx = 0
        p1_dy = 0
        if keys[pygame.K_a]:
            p1_dx -= 1
        if keys[pygame.K_d]:
            p1_dx += 1
        if keys[pygame.K_w]:
            p1_dy -= 1
        if keys[pygame.K_s]:
            p1_dy += 1
        p1.move(p1_dx, p1_dy)

        # --- Player 2 Input (Arrow Keys) ---
        p2_dx = 0
        p2_dy = 0
        if keys[pygame.K_LEFT]:
            p2_dx -= 1
        if keys[pygame.K_RIGHT]:
            p2_dx += 1
        if keys[pygame.K_UP]:
            p2_dy -= 1
        if keys[pygame.K_DOWN]:
            p2_dy += 1
        p2.move(p2_dx, p2_dy)


        screen.fill((40, 44, 52))
        draw(screen, p1, p2)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
