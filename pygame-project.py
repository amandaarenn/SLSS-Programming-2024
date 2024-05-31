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

NUM_SNOWBALLS = 4
NUM_ENEMIES = 5



# load img
SNOWBALL_IMAGE = pg.image.load("./Images/snowball.png")

# scale img
SNOWBALL_IMAGE = pg.transform.scale(
    SNOWBALL_IMAGE, (SNOWBALL_IMAGE.get_width() // 3, SNOWBALL_IMAGE.get_height() // 3)
)    

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pg.image.load("./Images/snowman.webp")

        #  load img
        SNOWMAN_IMAGE = pg.image.load("./Images/snowman.webp")
            # scale img
        SNOWMAN_IMAGE = pg.transform.scale(
            SNOWMAN_IMAGE, (SNOWMAN_IMAGE.get_width() // 8, SNOWMAN_IMAGE.get_height() // 8))    
    
        self.rect = self.image.get_rect()

        self.lives_remaining = 9

    def update(self):
        """Updates the location of sprite to the mouse cursor"""
        self.rect.centerx = pg.mouse.get_pos()[0]
        self.rect.centery = pg.mouse.get_pos()[1]

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        """
        Params:
            player_loc: x,y coords of centerx and top
        """
        super().__init__()

        # Shooting Snowballs
        self.image = pg.image.load("./Images/snowball.png")

        self.rect = self.image.get_rect()

        # Spawn at the Player
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

        self.vel_y = -3  # move up

    def update(self):
        self.rect.y += self.vel_y

        # Kill the bullet if it leaves the screen
        if self.rect.bottom < 0:
            self.kill()

class Goat(pg.sprite.Sprite):
    def __init__(self, centerx: int, centery: int):
        """
        Params:
            centerx: center x spawn of the enemy
            centery: center y spawn of the enemy
        """
        super().__init__()

        self.image = pg.image.load("./Images/goat.png")

        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = centerx, centery

        self.vel_x = 4
        self.vel_y = 2

    def update(self):
        # Movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce in the x-axis
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x *= -1

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


    # Blooper sprites
    enemy_sprites = pg.sprite.Group()


    #Create a player and store it in a variable
    player = Player ()

    all_sprites.add(player)

    for _ in range(NUM_ENEMIES):
        enemy = Goat()
        all_sprites.add(enemy)
        enemy_sprites.add (enemy)

    pg.display.set_caption("Snowball Shooter")


    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

  
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