import random 
import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 100

class Player(pg.sprite.Sprite):
    # TODO: Change Mario image depending on facing direction
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/mario.webp")

        self.rect = self.image.get_rect()

    def update(self):
        """Updates the location of sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/coin.png")

        self.rect = self.image.get_rect()

        # Randomize initial location
        self.rect.centerx = random.randrange(0, WIDTH - self.rect.width)
        self.rect.centery = random.randrange(0, HEIGHT - self.rect.height)


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0


    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Coin sprites
    coin_sprites = pg.sprite.Group()

    for _ in range(NUM_COINS):
        coin = Coin()
        
        all_sprites.add(coin_sprites)
        coin_sprites.add(coin)

    #Create a player and store it in a variable
    player = Player ()

    all_sprites.add(player)

    pg.display.set_caption("Jewel Thief Clone (Don't sue us Nintendo)")


    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Collison between player and coin_sprites
        # Get a list of ALL coin_sprites that collide
        # with the player sprite
        # For every coin that colllides, print "gyatt"
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)

        for coin in coins_collided:
            # increase the score by 1 
            score += 1

            print(score)

        # --- Draw items
        screen.fill (WHITE)

        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()