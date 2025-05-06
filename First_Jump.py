import pygame
from random import randint

# Game Variables -

pygame.init()

g_ttl = "The First Jump"
pygame.display.set_caption(g_ttl)

# Screen Setup
scn_wdth = 1280
scn_ht = 720
scn = pygame.display.set_mode((scn_wdth, scn_ht))

fps = 60
plr_grav = 0
clk = pygame.time.Clock()

start_time = 0
score = 0

# Theme Colours -
# Darker Blue
theme_colour_1 = (45, 189, 239)
# Sky Blue
theme_colour_2 = (96, 198, 238)
# Lighter Blue
theme_colour_3 = (139, 210, 240)
# Green
theme_colour_4 = (10, 112, 48)

blk = (0, 0, 0)
white = (255, 255, 255)

# Font -

def pixel_font(size):
    font = pygame.font.Font("FirstJumpAssets/PixelOperator8.ttf", size)
    return font


# Player Collisions - If enemy rect collides with the player return function as true or return false

def collision(player_run, player_jump, enemies):
    if enemies:
        for enemy_rect in enemies:
            if player_run.colliderect(enemy_rect) or player_jump.colliderect(enemy_rect):
                return True
    return False


# Score Tracker - score = seconds while the game is active

def display_score():
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    return current_score


# Sounds -

jump_sound = pygame.mixer.Sound("FirstJumpAssets/PlayerJump.wav")
jump_sound.set_volume(0.2)

bg_music = pygame.mixer.Sound("FirstJumpAssets/FirstJumpMusic.mp3")
bg_music.set_volume(0.3)
bg_music.play(loops=-1)


# Menu Objects -

# Scrolling Background
game_bg = pygame.image.load("FirstJumpAssets/Background.jpg").convert()
game_bg_width = game_bg.get_width()
game_bg_tiles = int(game_bg_width / scn_wdth) + 1
game_bg_scroll_x_pos = 0


# Game Title Text (First Jump)
def title_text():
    title_text_surf = pixel_font(55).render(
        "First Jump", False, white).convert_alpha()
    title_text_rect = title_text_surf.get_rect()
    title_text_border = title_text_rect.inflate(10, 15)
    title_text_rect.midbottom = (640, 100)
    title_text_border.midbottom = (640, 105)

    pygame.draw.rect(scn, theme_colour_2, title_text_border)
    scn.blit(title_text_surf, title_text_rect)


# Current Score While Playing Text
def active_game_score_text():
    score_text_render = pixel_font(20).render(
        f"Score: {score}", False, white).convert_alpha()
    score_text_rect = score_text_render.get_rect()
    score_text_rect.topleft = (0, 20)
    score_text_border = score_text_rect.inflate(10, 10)
    score_text_border.topleft = (0, 15)

    pygame.draw.rect(scn, theme_colour_2, score_text_border)
    scn.blit(score_text_render, score_text_rect)


# Start Menu -

# Start Menu Game Description
def start_menu_game_desc_text():
    game_desc_text_render_1 = pixel_font(35).render(
        "Avoid enemies at all costs!", False, white).convert_alpha()
    game_desc_text_render_2 = pixel_font(35).render(
        "  Failure is not an option!", False, white).convert_alpha()
    game_desc_rect_1 = game_desc_text_render_1.get_rect(midtop=(640, 140))
    game_desc_rect_2 = game_desc_text_render_1.get_rect(midtop=(640, 200))

    scn.blit(game_desc_text_render_1, game_desc_rect_1)
    scn.blit(game_desc_text_render_2, game_desc_rect_2)


# Start Menu - Controls Text
def controls_text():
    # Controls - line 1
    controls_text_render_1 = pixel_font(35).render(
        "Controls :", False, white).convert_alpha()
    controls_text_rect_1 = controls_text_render_1.get_rect(center=(640, 500))

    scn.blit(controls_text_render_1, controls_text_rect_1)

    # Controls - line 2
    controls_text_render_2 = pixel_font(30).render(
        "Jump = [SPACE]", False, white).convert_alpha()
    controls_text_rect_2 = controls_text_render_2.get_rect(center=(640, 550))

    scn.blit(controls_text_render_2, controls_text_rect_2)

    #   Controls - line 3
    controls_text_render_3 = pixel_font(30).render(
        "Quit = [Q]", False, white).convert_alpha()
    controls_text_rect_3 = controls_text_render_3.get_rect(center=(640, 600))

    scn.blit(controls_text_render_3, controls_text_rect_3)

    # Border around controls text
    cntr_border_rect = pygame.Rect((0, 0), (365, 160))
    cntr_border_rect.center = (640, 545)

    pygame.draw.rect(scn, white, cntr_border_rect, 3)


# Start Menu - Play Text
def start_menu_play_text():
    menu_play_text_render = pixel_font(40).render(
        "Press [SPACE] To Start!", False, white).convert_alpha()
    menu_play_text_rect = menu_play_text_render.get_rect(midbottom=(640, 700))

    scn.blit(menu_play_text_render, menu_play_text_rect)


# Game Over Menu -

# Display game over text
def you_lost_text():
    menu_you_lost_text_surf = pixel_font(40).render(
        "You Got Hit! Game Over!", False, white)
    menu_you_lost_text_rect = menu_you_lost_text_surf.get_rect(
        center=(640, 160))

    scn.blit(menu_you_lost_text_surf, menu_you_lost_text_rect)


# Display final score
def final_score_text():
    final_score_render_1 = pixel_font(35).render(
        f"Your Score Was:", False, white).convert_alpha()
    final_score_render_2 = pixel_font(35).render(
        f"{score}", False, white).convert_alpha()
    final_score_render_3 = pixel_font(35).render(
        f"{score_comment}", False, white).convert_alpha()

    final_score_rect_1 = final_score_render_1.get_rect(midbottom=(640, 540))
    final_score_rect_2 = final_score_render_2.get_rect(midbottom=(640, 600))
    final_score_rect_3 = final_score_render_3.get_rect(midbottom=(640, 260))

    scn.blit(final_score_render_1, final_score_rect_1)
    scn.blit(final_score_render_2, final_score_rect_2)
    scn.blit(final_score_render_3, final_score_rect_3)


# Display play again text
def play_again_text():
    menu_play_again_text_render = pixel_font(40).render(
        "Press [SPACE] To Play Again", False, white)
    menu_play_again_text_rect = menu_play_again_text_render.get_rect(
        midbottom=(640, 700))

    scn.blit(menu_play_again_text_render, menu_play_again_text_rect)


# Player Assets and Functions -

# Load player sprite images
plr_run_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/PlayerSpriteSheet.png").convert_alpha()
plr_jump_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/PlayerJump.png").convert_alpha()
plr_death_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/PlayerDeath.png").convert_alpha()


# Player sprite function - separate sprites from the sprite sheet assigning width and height of each sprite in the sheet then scale them
def get_plr_sprite(sprite_sheet, frame, width, height, scale):
    # Create surface to paste image to
    plr_surf = pygame.Surface((width, height)).convert_alpha()
    # Blit cut out player img to surf
    plr_surf.blit(sprite_sheet, (0, 0), ((frame * width), 0, width, height))
    # Set colour of player surf to alpha(invisible)
    plr_surf.set_colorkey(blk)
    # Increase size of the player
    plr_scaled_surf = pygame.transform.scale(
        plr_surf, (width * scale, height * scale))
    return plr_scaled_surf


# Player Spin Animation For Start Menu w Rect -

plr_start_rect = (get_plr_sprite(
    plr_jump_sprite_sheet_img, 0, 15, 15, 10)).get_rect()
plr_start_rect.center = (640, 360)

# Player spin animations variables
plr_start_anim_list = []
plr_start_anim_steps = 4
plr_start_last_update = pygame.time.get_ticks()
plr_start_anim_cd = 150
plr_start_frame = 0

# Create an image list for player spin animation
for x in range(plr_start_anim_steps):
    plr_start_anim_list.append(get_plr_sprite(
        plr_jump_sprite_sheet_img, x, 15, 15, 10))


# Player Running Animation w Rect -

# Player run rect (for collisions)
plr_run_rect = (get_plr_sprite(
    plr_run_sprite_sheet_img, 0, 14, 18, 4)).get_rect()
plr_run_rect.bottomleft = (100, 560)

# Player run animation variables
plr_run_anim_list = []
plr_run_anim_steps = 8
plr_run_last_update = pygame.time.get_ticks()
plr_run_anim_cd = 75
plr_run_frame = 0

# Create an image list for player run animation
for x in range(plr_run_anim_steps):
    plr_run_anim_list.append(get_plr_sprite(
        plr_run_sprite_sheet_img, x, 14, 18, 4))


# Player Jump Animation w Rect -

# Player Jump Rect (for collisions)
plr_jump_rect = (get_plr_sprite(
    plr_jump_sprite_sheet_img, 0, 15, 15, 4)).get_rect()
plr_jump_rect.bottomleft = (100, 560)

# Player jump animation variables
plr_jump_anim_list = []
plr_jump_anim_steps = 4
plr_jump_last_update = pygame.time.get_ticks()
plr_jump_anim_cd = 75
plr_jump_frame = 0

# Create an image list for player jump animation
for x in range(plr_jump_anim_steps):
    plr_jump_anim_list.append(get_plr_sprite(
        plr_jump_sprite_sheet_img, x, 15, 15, 4))


# Game Over Player Death Animation w Rect -

plr_death_rect = (get_plr_sprite(
    plr_death_sprite_sheet_img, 0, 16, 19, 10)).get_rect()
plr_death_rect.center = (640, 360)

# Player death animation variables
plr_death_anim_list = []
plr_death_anim_steps = 3
plr_death_last_update = pygame.time.get_ticks()
plr_death_anim_cd = 100
plr_death_frame = 0

# Create an image list for player run animation
for x in range(0, 4):
    plr_death_anim_list.append(get_plr_sprite(
        plr_death_sprite_sheet_img, x, 16, 19, 10))


# Enemy Load / Functions -
# Enemy sprite sheet load
gs_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/SlimeGreenSpriteSheet.png").convert_alpha()
ps_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/SlimePurpleSpriteSheet.png").convert_alpha()
b_sprite_sheet_img = pygame.image.load(
    "FirstJumpAssets/BirdSpriteSheet.png").convert_alpha()


# Slime sprite sheet function - separate sprites from the sprite sheet assigning width and height of each sprite in the sheet then scale them
def slime_sprite(sprite_sheet, frame, width, height, scale):
    # Create surface to paste image to
    s_surf = pygame.Surface((width, height)).convert_alpha()
    # Blit cut out green slime img to surf
    s_surf.blit(sprite_sheet, (0, 0), ((frame * width), 0, width, height))
    # Set colour of green slime surf to alpha(invisible)
    s_surf.set_colorkey(blk)
    # Flip the green slime to face correct way
    s_flip = pygame.transform.flip(s_surf, True, False)
    # Increase size of the green slime
    s_scaled_flip = pygame.transform.scale(
        s_flip, (width * scale, height * scale))
    return s_scaled_flip


# Bird sprite sheet function - separate sprites from the sprite sheet assigning width and height of each sprite in the sheet then scale them
def bird_sprite(sprite_sheet, frame, width, height, scale):
    # Create surface to paste image to
    b_surf = pygame.Surface((width, height)).convert_alpha()
    # Blit cut out green slime img to surf
    b_surf.blit(sprite_sheet, (0, 0), ((frame * width), 0, width, height))
    # Set colour of green slime surf to alpha(invisible)
    b_surf.set_colorkey(blk)
    # Increase size of the green slime
    b_scaled = pygame.transform.scale(b_surf, (width * scale, height * scale))
    return b_scaled


# Enemy Spawning / Movement -
# Spawning variables
enemy_rect_list = []
# How often an enemy spawns in milliseconds
spwn_timer = 900

# User event, 900ms enemy spawn timer
enemy_tmr = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_tmr, spwn_timer)


# Enemy movement function
def enemy_move(enemy_list, speed):
    if enemy_list:
        # Move all enemy rects to the left 8 pixels
        for enemy_rect in enemy_list:
            enemy_rect.x -= (8 + speed)

            # Green Slime - Bottom set to 560
            if enemy_rect.bottom == 560:
                scn.blit(gs_anim_list[gs_frame], enemy_rect)

            # Purple Slime - Bottom set to 561
            if enemy_rect.bottom == 561:
                scn.blit(ps_anim_list[ps_frame], enemy_rect)

            # Bird - Bottom set to 400
            if enemy_rect.bottom == 400:
                scn.blit(b_anim_list[b_frame], enemy_rect)

        # Delete enemies not on screen - Check if enemies are off the screen, copy enemies that are on screen to enemy_list
        enemy_list = [enemy for enemy in enemy_list if enemy.x > -500]

        return enemy_list
    # If the list is empty return empty list - stops a game crash if the game is not active
    else:
        return []


# Green Slime Animation Variables -
gs_anim_list = []
gs_anim_steps = 4
gs_last_update = pygame.time.get_ticks()
gs_anim_cd = 150
gs_frame = 0
# Create cut-out Green Slime images in a list for animations
for x in range(gs_anim_steps):
    gs_anim_list.append(
        slime_sprite(gs_sprite_sheet_img, x, 14, 15, 4))


# Purple Slime Animation Variables -
ps_anim_list = []
ps_anim_steps = 4
ps_last_update = pygame.time.get_ticks()
ps_anim_cd = 150
ps_frame = 0
# Create cut-out Purple Slime images in a list for animations
for x in range(ps_anim_steps):
    ps_anim_list.append(
        slime_sprite(ps_sprite_sheet_img, x, 14, 15, 4))


# Bird Animation Variables -
b_anim_list = []
b_anim_steps = 9
b_last_update = pygame.time.get_ticks()
b_anim_cd = 75
b_frame = 0
# Create cut-out bird images in a list for animations
for x in range(b_anim_steps):
    b_anim_list.append(
        bird_sprite(b_sprite_sheet_img, x, 32, 32, 2.5))


# Game Loop Variables -
running = True
main_menu = True
game_active = False
game_over = False
jumping = False
collision_detected = False
game_speed = 0


while running:

    # Event Handler -

    for event in pygame.event.get():

        # Quit game -
        #   if x in top right is clicked, exit game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

        # Main menu -
        #   Look for [SPACE] key press to start game
        if main_menu:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main_menu = False
                game_active = True

                # Restart timer for score from 0
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:

            # Player Jump -
            #   Look for [SPACE] key press and if player is on the ground, if true Jump (invert gravity)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and plr_run_rect.bottom >= 560:
                    plr_grav = -25
                    jump_sound.play()
                    jumping = True

            # Enemy Spawning
            if event.type == enemy_tmr:
                # Select enemy to spawn randomly (1 to 3)
                enemy_type = randint(1, 3)
                # assign a random x position for the enemies to add variation to enemy distance
                rand_x_pos = randint(1280, 1400)

                if enemy_type == 1:

                    gs_rect = (
                        slime_sprite(gs_sprite_sheet_img, 0, 14, 15, 4)).get_rect(bottomleft=(rand_x_pos, 560))

                    enemy_rect_list.append(gs_rect)

                elif enemy_type == 2:
                    ps_rect = (
                        slime_sprite(ps_sprite_sheet_img, 0, 14, 15, 4)).get_rect(bottomleft=(rand_x_pos, 561))

                    enemy_rect_list.append(ps_rect)

                elif enemy_type == 3:
                    b_rect = (
                        (bird_sprite(b_sprite_sheet_img, 0, 32, 32, 2.5)).get_rect(bottomleft=(rand_x_pos, 400)))

                    enemy_rect_list.append(b_rect)

        # Game Over -
        #   Look for [SPACE] key press to restart game
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                game_over = False
                # Reset Player Death Animation
                plr_death_frame = 0
                # Restart timer for score from 0
                start_time = int(pygame.time.get_ticks() / 1000)
                # Delete any enemies on screen
                enemy_rect_list.clear()
                # Reset game speed
                game_speed = 0
    # </editor-fold>

    # Main Menu Screen -
    if main_menu:
        # Display Start Menu -
        scn.fill(theme_colour_2)
        title_text()
        start_menu_game_desc_text()
        controls_text()
        start_menu_play_text()

        # Update Start Menu Player Animation -
        plr_start_current_time = pygame.time.get_ticks()

        if plr_start_current_time - plr_start_last_update >= plr_start_anim_cd:
            plr_start_frame += 1
            plr_start_last_update = plr_start_current_time

            if plr_start_frame >= len(plr_start_anim_list):
                plr_start_frame = 0

        scn.blit(plr_start_anim_list[plr_start_frame], plr_start_rect)

    # Game Over Screen -
    if game_over:
        #   Final Score Flavour Text
        if score <= 10:
            score_comment = "Better Luck Next Time!".center(25)
        elif score <= 30:
            score_comment = "Nice!".center(25)
        else:
            score_comment = "WOW! Well Played!".center(25)

        # Display Game Over Menu
        scn.fill(theme_colour_2)
        title_text()
        you_lost_text()
        final_score_text()
        play_again_text()

    if game_over:

        # Update Game Over Player Death Animation - (Stops at third frame)
        plr_death_current_time = pygame.time.get_ticks()

        # if at third frame just display third frame every loop
        if plr_death_frame >= 3:
            scn.blit(plr_death_anim_list[3], plr_death_rect)

        elif plr_death_frame < 4:
            scn.blit(plr_death_anim_list[plr_death_frame], plr_death_rect)
            if plr_death_current_time - plr_death_last_update >= plr_death_anim_cd:
                plr_death_frame += 1
                plr_death_last_update = plr_death_current_time
                scn.blit(plr_death_anim_list[plr_death_frame], plr_death_rect)

    # Game Active Loop -
    if game_active:

        # Scrolling Background -
        for tile in range(0, game_bg_tiles):
            scn.blit(game_bg, (tile * game_bg_width + game_bg_scroll_x_pos, 0))

        # Scroll game background
        game_bg_scroll_x_pos -= 6 + game_speed
        # Reset scroll
        if abs(game_bg_scroll_x_pos) > game_bg_width:
            game_bg_scroll_x_pos = 0

        # Start Score Timer
        score = display_score()

        # Increase speed of enemies
        if score == 10:
            game_speed = 1
        if score == 20:
            game_speed = 2
            spwn_timer = 800
        if score == 30:
            game_speed = 4
            spwn_timer = 600
        if score == 60:
            game_speed = 6
            spwn_timer = 500
        if score == 90:
            game_speed = 8
            spwn_timer = 400

        # Display Game UI -
        title_text()
        active_game_score_text()

        # Update Enemy Movement
        enemy_rect_list = enemy_move(enemy_rect_list, game_speed)

        # Collisions -
        if collision(plr_run_rect, plr_jump_rect, enemy_rect_list):
            game_active = False
            game_over = True

        # Player -
        #   Player Gravity
        plr_grav += 1.5
        plr_run_rect.y += plr_grav
        plr_jump_rect.y += plr_grav

        #   Player Ground (Stop player falling off the game window)
        if plr_run_rect.bottom >= 560:
            plr_run_rect.bottom = 560

        if plr_jump_rect.bottom >= 560:
            plr_jump_rect.bottom = 560

        #   Display Player with rect
        if jumping and plr_run_rect.bottom >= 560:
            jumping = False

        if jumping:
            plr_jump_current_time = pygame.time.get_ticks()

            if plr_jump_current_time - plr_jump_last_update >= plr_jump_anim_cd:
                plr_jump_frame += 1
                plr_jump_last_update = plr_jump_current_time

                if plr_jump_frame >= len(plr_jump_anim_list):
                    plr_jump_frame = 0

            scn.blit(plr_jump_anim_list[plr_jump_frame], plr_jump_rect)

        if not jumping:
            plr_run_current_time = pygame.time.get_ticks()

            if plr_run_current_time - plr_run_last_update >= plr_run_anim_cd:
                plr_run_frame += 1
                plr_run_last_update = plr_run_current_time

                if plr_run_frame >= len(plr_run_anim_list):
                    plr_run_frame = 0

            scn.blit(plr_run_anim_list[plr_run_frame], plr_run_rect)

        # Enemy Animation Update -

        # Update Green Slime Animation -
        gs_current_time = pygame.time.get_ticks()

        if gs_current_time - gs_last_update >= gs_anim_cd:
            gs_frame += 1
            gs_last_update = gs_current_time

            if gs_frame >= len(gs_anim_list):
                gs_frame = 0

        # Update Purple Slime Animation -
        ps_current_time = pygame.time.get_ticks()

        if ps_current_time - ps_last_update >= ps_anim_cd:
            ps_frame += 1
            ps_last_update = ps_current_time

            if ps_frame >= len(ps_anim_list):
                ps_frame = 0

        # Update Bird Animation -
        b_current_time = pygame.time.get_ticks()
        if b_current_time - b_last_update >= b_anim_cd:
            b_frame += 1
            b_last_update = b_current_time

            if b_frame >= len(b_anim_list):
                b_frame = 0

    # Update Display -
    pygame.display.update()
    # Max FPS
    clk.tick(fps)
