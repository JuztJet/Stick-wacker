# Stick Wacker Game

# Imports
import pygame

# ---------------------------------------------------------------------------------------------------------------

pygame.init()
w, h = pygame.display.get_desktop_sizes()[0]
#w, h = 700, 400
icon_image = pygame.image.load("Assets\Stick-Man\Stick Image.png")
pygame.display.set_icon(icon_image)
pygame.display.set_caption("Stick-Wacker", "Stick Or is it?")

# ---------------------------------------------------------------------------------------------------------------

screen = pygame.display.set_mode((w, h))
screen.fill("#38B6FF")
print("Dont hit people with sticks")
clock = pygame.time.Clock()

# ---------------------------------------------------------------------------------------------------------------
pygame.key.set_repeat(100)
running = True
reset = False
play = False
start_screen_on = True
char_options_on = False

# ---------------------------------------------------------------------------------------------------------------

score_numbers = [0, 0]
logo_tick = 0
logo_frame = 0
made = 0
player_font = pygame.font.Font('Assets/RobotoMono-Bold.ttf', int(w * 0.013))

# ---------------------------------------------------------------------------------------------------------------

logo_images = [pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (int(w * 0.226), int(h * 0.376)))
               for image in [
                   'Assets/Start Up/Logo1.png',
                   'Assets/Start Up/Logo2.png'
               ]]

play_image = pygame.transform.smoothscale(pygame.image.load("Assets\Start Up\Play.png"),
                                          (int(0.130 * w), int(0.1089 * h)))


# ---------------------------------------------------------------------------------------------------------------

logo_images_rect = [image.get_rect(center=(w / 2, h * 0.25)) for image in logo_images]
play_image_rect = play_image.get_rect(center=(w / 2, h * .70))


# ---------------------------------------------------------------------------------------------------------------


def start_screen(logo_frame, logo_tick, play, start_screen_on, char_options_on):
    if logo_frame == 2:
        logo_frame, logo_tick = 0, 0
    screen.blit(logo_images[logo_frame], logo_images_rect[logo_frame])
    screen.blit(play_image, play_image_rect)
    logo_frame = logo_tick // 50

    logo_tick += 1
    if pygame.mouse.get_pressed() == (True, False, False):
        if play_image_rect.collidepoint(pygame.mouse.get_pos()):
            start_screen_on = False
            char_options_on = True

    return logo_tick, logo_frame, play, start_screen_on, char_options_on


class PlayerCustomisation:
    colours = ['Black', "Red", "Orange", "Yellow", "Green", 'Blue', 'Indigo', 'Violet', 'White']
    screen.fill("#38B6FF")
    play_image_rect = play_image.get_rect(center=(w / 2, h * .82))
    def __init__(self, name):
        self.start_time = 0
        self.player_colour = 0
        self.name = name
        self.valid = False
        self.text = ''
        self.current_colour = 'Black'
        self.real_text = player_font.render(self.text, False, "Black")

        if self.name == "Player 1":
            self.player_image = pygame.transform.smoothscale(
                pygame.image.load("Assets/Stick-Man/Stick-Man-With-Stick.png").convert_alpha(),
                (1.5 * (w * 0.1158), 1.5 * (h * 0.2604)))
            self.fake_player_image = pygame.transform.smoothscale(
                pygame.image.load("Assets/Stick-Man/Stick-Man-No-Stick.png").convert_alpha(),
                (1.5 * (w * 0.1158), 1.5 * (h * 0.2604)))
            self.fake_player_rect = self.fake_player_image.get_rect(center=(w * 0.15, h / 2))
            self.player_rect = self.player_image.get_rect(center=(w * 0.15, h / 2))
            self.textbox = pygame.Rect((0 + w * 0.01, self.player_rect.y - h * 0.1), (self.player_rect.width, 50))
            self.real_text_rect = pygame.Rect(
                (self.textbox.centerx, self.player_rect.y - h * 0.1 + self.real_text.get_height() / 2),
                (self.player_rect.width, 50))



        else:
            self.player_image = pygame.transform.flip(pygame.transform.smoothscale(
                pygame.image.load("Assets/Stick-Man/Stick-Man-With-Stick.png").convert_alpha(),
                (1.5 * (w * 0.1158), 1.5 * (h * 0.2604))), True, False)
            self.fake_player_image = pygame.transform.flip(pygame.transform.smoothscale(
                pygame.image.load("Assets/Stick-Man/Stick-Man-No-Stick.png").convert_alpha(),
                (1.5 * (w * 0.1158), 1.5 * (h * 0.2604))), True, False)
            self.fake_player_rect = self.fake_player_image.get_rect(center=(w * 0.85, h / 2))
            self.player_rect = self.player_image.get_rect(center=(w * 0.85, h / 2))

            self.textbox = pygame.Rect((w - w * 0.01 - self.player_rect.width, self.player_rect.y - h * 0.1),
                                       (self.player_rect.width, 50))
            self.real_text_rect = pygame.Rect(
                (self.textbox.centerx, self.player_rect.y - h * 0.1 + self.real_text.get_height() / 2),
                (self.player_rect.width, 50))


        self.player_right_button = pygame.draw.polygon(screen, "White", [
            (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery - h * 0.02),
            (self.player_rect.x + self.player_rect.width + w * 0.04, self.player_rect.centery),
            (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery + h * 0.02)])
        self.player_left_button = pygame.draw.polygon(screen, "White", [
            (self.player_rect.x - w * 0.02, self.player_rect.centery - h * 0.02),
            (self.player_rect.x - w * 0.04, self.player_rect.centery),
            (self.player_rect.x - w * 0.02, self.player_rect.centery + h * 0.02)])

    def blit_to_screen(self):
        screen.blit(self.player_image, self.player_rect)
        screen.blit(self.fake_player_image, self.fake_player_rect)
        self.player_right_button = pygame.draw.polygon(screen, "White", [
            (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery - h * 0.02),
            (self.player_rect.x + self.player_rect.width + w * 0.04, self.player_rect.centery),
            (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery + h * 0.02)])
        self.player_left_button = pygame.draw.polygon(screen, "White", [
            (self.player_rect.x - w * 0.02, self.player_rect.centery - h * 0.02),
            (self.player_rect.x - w * 0.04, self.player_rect.centery),
            (self.player_rect.x - w * 0.02, self.player_rect.centery + h * 0.02)])
        pygame.draw.rect(screen, "#F0EDE5", self.textbox)
        #pygame.draw.rect(screen, "Blue", self.real_text_rect)
        screen.blit(self.real_text, self.real_text_rect)
        screen.blit(play_image, PlayerCustomisation.play_image_rect)
    def play_button(self):
        if pygame.mouse.get_pressed() == (True, False, False):
            if PlayerCustomisation.play_image_rect.collidepoint(pygame.mouse.get_pos()):
                play = True
                return play

    def button_detection(self):
        if pygame.mouse.get_pressed() == (True, False, False):
            if self.player_right_button.collidepoint(
                    pygame.mouse.get_pos()) and pygame.time.get_ticks() >= self.start_time + 200 and self.player_colour <= 7:
                self.start_time = pygame.time.get_ticks()
                player_1_right_button = pygame.draw.polygon(screen, "Blue", [
                    (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery - h * 0.02),
                    (self.player_rect.x + self.player_rect.width + w * 0.04, self.player_rect.centery),
                    (self.player_rect.x + self.player_rect.width + w * 0.02, self.player_rect.centery + h * 0.02)])
                self.player_colour += 1
                self.current_colour = PlayerCustomisation.colours[self.player_colour]
                self.fake_player_image.fill('white', special_flags=pygame.BLEND_RGB_SUB)
                self.fake_player_image.fill(PlayerCustomisation.colours[self.player_colour],
                                            special_flags=pygame.BLEND_RGB_ADD)
                print(self.current_colour)



            elif self.player_left_button.collidepoint(
                    pygame.mouse.get_pos()) and pygame.time.get_ticks() >= self.start_time + 200 and self.player_colour >= 1:
                self.start_time = pygame.time.get_ticks()
                self.player_left_button = pygame.draw.polygon(screen, "Blue",
                                                              [(self.player_rect.x - w * 0.02,
                                                                self.player_rect.centery - h * 0.02),
                                                               (
                                                                   self.player_rect.x - w * 0.04,
                                                                   self.player_rect.centery),
                                                               (self.player_rect.x - w * 0.02,
                                                                self.player_rect.centery + h * 0.02)])
                self.player_colour -= 1
                self.fake_player_image.fill('white', special_flags=pygame.BLEND_RGB_SUB)

                self.fake_player_image.fill(PlayerCustomisation.colours[self.player_colour],
                                            special_flags=pygame.BLEND_RGB_ADD)
                self.current_colour = PlayerCustomisation.colours[self.player_colour]

    def text_click_detection(self):

        if ok1.textbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (True, False, False):
                ok1.valid = True
                ok2.valid = False
        elif ok2.textbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed() == (True, False, False):
                ok2.valid = True
                ok1.valid = False
    def text_input(self, realtext):
        key = pygame.key.get_pressed()
        if key[pygame.K_BACKSPACE]:
            self.text = self.text[:-1]
        elif len(self.text) < 22:
            if type(realtext)== str:
                self.text += self.text.join(filter(None, [realtext]))
        self.real_text = player_font.render(self.text, False, "Black")
        self.real_text_rect.width = self.real_text.get_width()
        self.real_text_rect.centerx = self.textbox.centerx

    def update2(self):
        self.blit_to_screen()
        self.button_detection()
        self.text_click_detection()
        play = self.play_button()
        return play


class Players(pygame.sprite.Sprite):
    score = player_font.render('{}-{}'.format(score_numbers[0], score_numbers[1]), False, "Black")
    score_rect = score.get_rect(center=(w / 2, h * .9))

    def __init__(self, name, pos, nickname, colour):

        super().__init__()
        self.name = name
        self.walking_frame_num = 0
        self.attack_frame_num = 0
        self.walking_tick = 0
        self.attack_tick = 0
        self.walking_frames = [
            pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215)) for image in
            ['Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img0.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img1.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img2.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img3.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img4.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img5.png', ]]
        for i in self.walking_frames:
            i.fill(colour,special_flags=pygame.BLEND_RGB_ADD)
        self.reverse_walking_frames = [pygame.transform.flip(
            (pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215))), True,
            False) for image in
            ['Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img0.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img1.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img2.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img3.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img4.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img5.png', ]]
        for i in self.reverse_walking_frames:
            i.fill(colour,special_flags=pygame.BLEND_RGB_ADD)
        self.hitting_frames = [
            pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215)) for image in
            ['Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img0.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img1.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img2.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img3.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img4.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img5.png']]
        for i in self.hitting_frames:
            i.fill(colour,special_flags=pygame.BLEND_RGB_ADD)
        self.reverse_hitting_frames = [pygame.transform.flip(
            (pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215))), True,
            False) for image in
            ['Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img0.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img1.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img2.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img3.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img4.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img5.png']]
        for i in self.reverse_hitting_frames:
            i.fill(colour,special_flags=pygame.BLEND_RGB_ADD)

        self.player_text = player_font.render(nickname, False, "#abdbe3")
        self.attack_time = 0
        if self.name == "Player 1":
            self.image = self.walking_frames[self.walking_frame_num]
            self.rect = self.image.get_rect(bottomleft=pos)
            self.control = {
                "right": pygame.K_d,
                'left': pygame.K_a,
                "jump": pygame.K_w,
                'attack': pygame.K_e,
                "jumped": False,
                'attacked': False,
                'facing_right': True
            }
            self.text_health_control = {
                'player_health_level': int(w * 0.065),
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topleft=(self.rect.x, int(self.rect.y - h * 0.115))),
                "player_health_bar_rect": pygame.Rect((self.rect.x, int(self.rect.y - h * 0.08)),
                                                      (int(w * 0.0651), int(h * 0.023))),
                "player_health_bar_background_rect": pygame.Rect((self.rect.x, int(self.rect.y - h * 0.08)),
                                                                 (int(w * 0.065), int(h * 0.023))),
                "player_health_bar_outline_rect": pygame.Rect((self.rect.x, int(self.rect.y - h * 0.08)),
                                                              (int(w * 0.065), int(h * 0.023)))
            }
        if self.name == "Player 2":
            self.image = self.reverse_walking_frames[self.walking_frame_num]
            self.rect = self.image.get_rect(bottomright=pos)
            self.control = {
                "right": pygame.K_RIGHT,
                'left': pygame.K_LEFT,
                "jump": pygame.K_UP,
                'attack': pygame.K_END,
                "jumped": False,
                "attacked": False,
                'facing_right': False
            }
            self.text_health_control = {
                'player_health_level': int(w * 0.065),
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topright=(self.rect.right, self.rect.y - int(h * 0.115))),
                "player_health_bar_rect": pygame.Rect((self.rect.right - int(w * 0.065), self.rect.y - int(h * 0.081)),
                                                      (int(w * 0.065), int(h * 0.023))),
                "player_health_bar_background_rect": pygame.Rect(
                    (self.rect.right - int(w * 0.065), self.rect.y - int(h * 0.081)), (int(w * 0.065), int(h * 0.023))),
                "player_health_bar_outline_rect": pygame.Rect(
                    (self.rect.right - int(w * 0.065), self.rect.y - int(h * 0.081)), (int(w * 0.065), int(h * 0.023)))

            }

    def gravity(self):
        gravity = 0.00057 * h
        if self.rect.y < h * 0.58:
            self.rect.y += (gravity * speed * dt)
            self.text_health_control['player_text_rect'].y = self.rect.y - int(h * 0.115)
            self.text_health_control['player_health_bar_rect'].y = self.rect.y - int(h * 0.081)
            self.text_health_control['player_health_bar_background_rect'].y = self.rect.y - int(h * 0.081)
            self.text_health_control['player_health_bar_outline_rect'].y = self.rect.y - int(h * 0.081)
        else:
            self.control["jumped"] = False
            self.rect.y = h * 0.59

    def move1(self):
        key = pygame.key.get_pressed()
        if key[self.control["right"]]:
            self.control['facing_right'] = True
            self.move2("right")
        elif key[self.control["left"]]:
            self.control['facing_right'] = False
            self.move2("left")
        if key[self.control['attack']] and int(pygame.time.get_ticks() / 100) >= self.attack_time + 5 or self.control[
            'attacked']:
            self.control['attacked'] = True
            self.attack()
        if key[self.control["jump"]] and self.control["jumped"] == False:
            self.control["jumped"] = True
            self.move2("jump")

        if self.rect.x <= -160:
            self.rect.x = w + 140
        elif self.rect.x >= w + 140:
            self.rect.x = -160

    def move2(self, control):
        direction = pygame.Vector2()

        if self.walking_frame_num == 5:
            self.walking_frame_num = 0
            self.walking_tick = 0
        if control == "right":
            self.walking_frame_num = self.walking_tick // 3

            self.image = self.walking_frames[self.walking_frame_num]
            direction.x += 1
            self.rect.move_ip(speed * dt * direction)
            self.text_health_control['player_text_rect'].left = self.rect.left
            self.text_health_control['player_health_bar_outline_rect'].left = self.rect.left
            self.text_health_control['player_health_bar_background_rect'].left = self.rect.left
            self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                'player_health_bar_background_rect'].left
        if control == "left":
            self.walking_frame_num = self.walking_tick // 3

            self.image = self.reverse_walking_frames[self.walking_frame_num]
            direction.x -= 1
            self.rect.move_ip(speed * dt * direction)
            self.text_health_control['player_text_rect'].right = self.rect.right
            self.text_health_control['player_health_bar_outline_rect'].right = self.rect.right
            self.text_health_control['player_health_bar_background_rect'].right = self.rect.right

            self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                'player_health_bar_background_rect'].left
        self.walking_tick += 1

        if control == "jump":
            self.rect.y -= h * 0.55
            self.text_health_control['player_text_rect'].y -= h * 0.55
            self.text_health_control['player_health_bar_rect'].y -= h * 0.55
            self.text_health_control['player_health_bar_background_rect'].y -= h * 0.55
            self.text_health_control['player_health_bar_outline_rect'].y -= h * 0.55

    def collision_blocker(self):
        if player1.rect.colliderect(player2.rect):
            if self.name == "Player 1":
                if player1.rect.centerx <= player2.rect.centerx:
                    player1.rect.right = player2.rect.left
                    self.text_health_control['player_text_rect'].left = self.rect.left
                    self.text_health_control['player_health_bar_outline_rect'].left = self.rect.left
                    self.text_health_control['player_health_bar_background_rect'].left = self.rect.left
                    self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                        'player_health_bar_background_rect'].left


                else:
                    player1.rect.left = player2.rect.right
                    self.text_health_control['player_text_rect'].right = self.rect.right
                    self.text_health_control['player_health_bar_outline_rect'].right = self.rect.right
                    self.text_health_control['player_health_bar_background_rect'].right = self.rect.right
                    self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                        'player_health_bar_background_rect'].left  # if player 2 x is behind player 1 x
            elif player2.rect.centerx <= player1.rect.centerx:
                player2.rect.right = player1.rect.left
                self.text_health_control['player_text_rect'].left = self.rect.left
                self.text_health_control['player_health_bar_outline_rect'].left = self.rect.left
                self.text_health_control['player_health_bar_background_rect'].left = self.rect.left
                self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                    'player_health_bar_background_rect'].left
            else:
                player2.rect.left = player1.rect.right

                self.text_health_control['player_text_rect'].right = self.rect.right
                self.text_health_control['player_health_bar_outline_rect'].right = self.rect.right
                self.text_health_control['player_health_bar_background_rect'].right = self.rect.right

                self.text_health_control['player_health_bar_rect'].left = self.text_health_control[
                    'player_health_bar_background_rect'].left
            self.walking_tick -= 1

    def attack(self):
        if self.attack_frame_num == 5:
            self.attack_frame_num = 0
            self.attack_tick = 0
            self.control['attacked'] = False
            self.damage()

            self.attack_time = int(pygame.time.get_ticks() / 100)
        if self.control['facing_right']:
            self.image = self.hitting_frames[self.attack_frame_num]
        else:
            self.image = self.reverse_hitting_frames[self.attack_frame_num]
        self.attack_frame_num = self.attack_tick // 2

        self.attack_tick += 1

    def damage(self):

        if self.name == "Player 1":
            if player1.rect.colliderect(player2.rect) or player1.control['facing_right'] and (
                    player1.rect.right == player2.rect.left) or player1.control['facing_right'] == False and (
                    player1.rect.left == player2.rect.right):

                player2.text_health_control['player_health_bar_rect'].inflate_ip(-(0.011068 * w), 0)
                if player2.control['facing_right']:
                    player2.text_health_control['player_health_bar_rect'].left = player2.text_health_control[
                        'player_health_bar_background_rect'].left


                else:
                    player2.text_health_control['player_health_bar_rect'].left = player2.text_health_control[
                        'player_health_bar_background_rect'].left

        elif player1.rect.colliderect(player2.rect) or player2.control['facing_right'] and (
                player2.rect.right == player1.rect.left) or player2.control['facing_right'] == False and (
                player2.rect.left == player1.rect.right):

            player1.text_health_control['player_health_bar_rect'].inflate_ip(-(0.011068 * w), 0)
            if player1.control['facing_right']:
                player1.text_health_control['player_health_bar_rect'].left = player1.text_health_control[
                    'player_health_bar_background_rect'].left
            else:
                player1.text_health_control['player_health_bar_rect'].left = player1.text_health_control[
                    'player_health_bar_background_rect'].left

    def health_detection(self, reset):

        if player2.text_health_control['player_health_bar_rect'].width <= 0:
            score_numbers[0] += .5
            Players.score = player_font.render('{}-{}'.format(int(score_numbers[0]), int(score_numbers[1])), True,
                                               "Black")
            sky.blit_Nat_Obj()
            grass.blit_Nat_Obj()
            screen.blit(Players.score, Players.score_rect)
            pygame.display.update()
            clock.tick(.5)

            reset = True
        elif player1.text_health_control['player_health_bar_rect'].width <= 0:
            score_numbers[1] += 1
            Players.score = player_font.render('{}-{}'.format(int(score_numbers[0]), int(score_numbers[1])), True,
                                               "Black")
            sky.blit_Nat_Obj()
            grass.blit_Nat_Obj()
            screen.blit(Players.score, Players.score_rect)
            pygame.display.update()
            clock.tick(.5)

            reset = True

        return reset

    def blit(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_health_control['player_text'], self.text_health_control['player_text_rect'])
        pygame.draw.rect(screen, "blue", self.rect, 1)
        pygame.draw.rect(screen, "red", self.text_health_control['player_health_bar_background_rect'])
        pygame.draw.rect(screen, "green", self.text_health_control['player_health_bar_rect'])
        pygame.draw.rect(screen, "black", self.text_health_control['player_health_bar_outline_rect'],
                         int(round(0.0023 * h, 0)))
        screen.blit(Players.score, Players.score_rect)

    def update(self, reset):
        self.blit()

        self.gravity()
        self.move1()
        self.collision_blocker()
        reset = self.health_detection(reset)
        return reset


class NaturalObjects:
    def __init__(self, name, width, height, pos, filepath):
        self.name = name
        self.width = width
        self.height = height
        self.pos = pos
        self.image = pygame.image.load(filepath).convert()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect(topleft=pos)

    def blit_Nat_Obj(self):
        screen.blit(self.image, self.rect)


sky = NaturalObjects("Sky", w, h, (0, 0), 'Assets/Natural Objects/sky.JPG')
grass = NaturalObjects("Grass", w, h, (0, h * 0.8), 'Assets/Natural Objects/grass.png')


while running:
    # pygame.event.set_allowed([pygame.QUIT])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if char_options_on:
            if 'ok1' in globals():

                if ok1.valid:
                    if event.type == pygame.TEXTINPUT:
                        ok1.text_input(event.text)
                    elif pygame.key.get_focused():
                        ok1.text_input(None)
            if 'ok2' in globals():
                if ok2.valid:
                    if event.type == pygame.TEXTINPUT:
                        ok2.text_input(event.text)
                    elif pygame.key.get_focused():
                        ok2.text_input(None)
    speed = 1000
    dt = clock.tick(50) / 1000
    if reset:
        player1 = Players("Player 1", (w * .03, h * 0.8 - 2), ok1.text, ok1.current_colour)
        player2 = Players("Player 2", (w * .97, h * 0.8 - 2), ok2.text, ok2.current_colour)
        reset = False
        play = True
        char_options_on = False


    elif play:
        sky.blit_Nat_Obj()
        grass.blit_Nat_Obj()
        reset = player1.update(reset)
        reset = player2.update(reset)
        pygame.mouse.set_visible(False)
    elif start_screen_on:
        logo_tick, logo_frame, play, start_screen_on, char_options_on = start_screen(logo_frame, logo_tick, play,
                                                                                     start_screen_on, char_options_on)
    elif char_options_on:
        screen.fill("#38B6FF")
        if made != 1:
            ok1 = PlayerCustomisation("Player 1")
            ok2 = PlayerCustomisation("Player 2")
            made += 1
        reset = ok1.update2()
        reset = ok2.update2()

    pygame.display.flip()
