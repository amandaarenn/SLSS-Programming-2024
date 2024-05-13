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
NUM_ENEMIES = 5

# load img
BLOOPER_IMAGE = pg.image.load("./Images/blooper.png")

# scale img
BLOOPER_IMAGE = pg.transform.scale(
    BLOOPER_IMAGE, (BLOOPER_IMAGE.get_width() // 8, BLOOPER_IMAGE.get_height() // 8)
)    



class Player(pg.sprite.Sprite):
    # TODO: Change Mario image depending on facing direction
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/mario.webp")

        self.rect = self.image.get_rect()

        self.lives_remaining = 9

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


class Blooper (pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = BLOOPER_IMAGE
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

        
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])

    
    def update(self):
        "Move the blooper and bounce it off the edge of the window"
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce
        if self.rect.left < 0:
            self.rect_left = 0
            self.vel_x *= -1
        if self.rect.right > WIDTH:
            self.rect_right = WIDTH
            self.vel_x *= -1
        if self.rect.top < 0:
            self.rect_top = 0
            self.vel_y *= -1
        if self.rect.bottom > HEIGHT:
            self.rect_bottom = HEIGHT
            self.vel_y *= -1



def start():
    """Environment Setup and Game Loop"""

    pg.init()
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    font = pg.font.SysFont("Futura", 24)

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Coin sprites
    coin_sprites = pg.sprite.Group()

    # Blooper sprites
    enemy_sprites = pg.sprite.Group()

    for _ in range(NUM_COINS):
        coin = Coin()
        
        all_sprites.add(coin_sprites)
        coin_sprites.add(coin)

    #Create a player and store it in a variable
    player = Player ()

    all_sprites.add(player)

    for _ in range(NUM_ENEMIES):
        enemy = Blooper()
        all_sprites.add(enemy)
        enemy_sprites.add (enemy)

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
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)

        for coin in coins_collided:
            # increase the score by 1 
            score += 1

            print(score)
    
        # if the coin_sprites group is empty
        # respawm al the coins 
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COINS):
                coin = Coin()
                all_sprites.add(coin)
                coin_sprites.add(coin)

        # TODO: detect collisions with enemies
        enemies_collided = pg.sprite.spritecollide(
            player, 
            enemy_sprites, 
            False
        )

        #TODO:iterate through enemies collided to notify in console
        for enemy in enemies_collided:
            
            # Decrease players life by one life per second
            player.lives_remaining -= (1 / 60)
            
            #Print the players current lives remaining
            print (f"Lives:{int(player.lives_remaining)}")



        # --- Draw items
        screen.fill(WHITE)

        all_sprites.draw(screen)

        # Create an image that has the score in it
        score_image = font.render(f"Score: {score}", True, GREEN)
        lives_image = font.render(
            f"Lives Remeaning: {int(player.lives_remaining)}", True, GREEN
        )
    
        # Draw/blit the image on the screen
        screen.blit(score_image, (5,5))
        screen.blit(lives_image, (5, 35))

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()