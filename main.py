# Stick Wacker Game

# Imports
import pygame

pygame.init()

# Getting width and height of window
w, h = pygame.display.get_desktop_sizes()[0]
#w, h = 700, 400
icon_image = pygame.image.load("Assets\Stick-Man\Stick Image.png")
pygame.display.set_icon(icon_image)
pygame.display.set_caption("Stick-Wacker", "Stick Or is it?")
screen = pygame.display.set_mode((w, h))
screen.fill("#38B6FF")
print("Dont hit people with sticks")
clock = pygame.time.Clock()
running = True
reset = False
play = False
player_font = pygame.font.Font('Assets/RobotoMono-Bold.ttf', int(w*0.013))
score_numbers = [0, 0]

logo_images = [pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (int(w*0.326), int(h*0.576))) for image in [
    'Assets/Start Up/Logo1.png',
    'Assets/Start Up/Logo2.png'
]]

play_image = pygame.transform.smoothscale(pygame.image.load("Assets\Start Up\Play.png"), (int(0.207*w), int(0.1689*h)))
logo_images_rect = [image.get_rect(center=(w / 2, h * 0.35)) for image in logo_images]
play_image_rect = play_image.get_rect(center=(w / 2, h * .8))
logo_tick = 0
logo_frame = 0


def start_screen(logo_frame, logo_tick, play):
    if logo_frame == 2:
        logo_frame, logo_tick = 0, 0
    screen.blit(logo_images[logo_frame], logo_images_rect[logo_frame])
    screen.blit(play_image, play_image_rect)
    logo_frame = logo_tick // 50

    logo_tick += 1
    if pygame.mouse.get_pressed() == (True, False, False):
        if play_image_rect.collidepoint(pygame.mouse.get_pos()):
            play = True

    return logo_tick, logo_frame, play
    pass


class Players(pygame.sprite.Sprite):
    score = player_font.render('{}-{}'.format(score_numbers[0], score_numbers[1]), False, "Black")
    score_rect = score.get_rect(center=(w / 2, h * .9))

    def __init__(self, name, pos):

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
        self.reverse_walking_frames = [pygame.transform.flip(
            (pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215))), True,
            False) for image in
            ['Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img0.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img1.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img2.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img3.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img4.png',
             'Assets/Stick-Man/Stick-Man Walking/Stick-Man Walking/img5.png', ]]
        self.hitting_frames = [
            pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215)) for image in
            ['Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img0.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img1.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img2.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img3.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img4.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img5.png']]
        self.reverse_hitting_frames = [pygame.transform.flip(
            (pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (w * 0.1257, h * 0.215))), True,
            False) for image in
            ['Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img0.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img1.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img2.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img3.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img4.png',
             'Assets/Stick-Man/Stick Man Wacking/Stick-Man Wacking/img5.png']]

        self.player_text = player_font.render(self.name, False, "Blue")
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
                'player_health_level': int(w*0.065),
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topleft=(self.rect.x, int(self.rect.y - h*0.115))),
                "player_health_bar_rect": pygame.Rect((self.rect.x, int(self.rect.y - h*0.08)), (int(w*0.0651), int(h*0.023))),
                "player_health_bar_background_rect": pygame.Rect((self.rect.x, int(self.rect.y - h*0.08)), (int(w*0.065), int(h*0.023))),
                "player_health_bar_outline_rect": pygame.Rect((self.rect.x, int(self.rect.y - h*0.08)), (int(w*0.065), int(h*0.023)))
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
                'player_health_level': int(w*0.065),
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topright=(self.rect.right, self.rect.y - int(h*0.115))),
                "player_health_bar_rect": pygame.Rect((self.rect.right - int(w*0.065), self.rect.y - int(h*0.081)), (int(w*0.065), int(h*0.023))),
                "player_health_bar_background_rect": pygame.Rect((self.rect.right - int(w*0.065), self.rect.y - int(h*0.081)), (int(w*0.065), int(h*0.023))),
                "player_health_bar_outline_rect": pygame.Rect((self.rect.right - int(w*0.065), self.rect.y - int(h*0.081)), (int(w*0.065), int(h*0.023)))

            }

    def gravity(self):
        gravity = .5
        if self.rect.y < h * 0.58:
            pass
            self.rect.y += (gravity * speed * dt)
            self.text_health_control['player_text_rect'].y += (gravity * speed * dt)
            self.text_health_control['player_health_bar_rect'].y += (gravity * speed * dt)
            self.text_health_control['player_health_bar_background_rect'].y += (gravity * speed * dt)
            self.text_health_control['player_health_bar_outline_rect'].y += (gravity * speed * dt)
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

    def move2(self, control):#Fix
        direction = pygame.Vector2()

        if self.walking_frame_num == 5:
            self.walking_frame_num = 0
            self.walking_tick = 0
        if control == "right":
            self.walking_frame_num = self.walking_tick // 3

            self.image = self.walking_frames[self.walking_frame_num]
            direction.x += 1
            self.text_health_control['player_text_rect'].x = self.rect.x
            self.text_health_control['player_text_rect'].update((self.rect.x, int(self.rect.y - h*0.12152)), (self.player_text.get_width(), self.player_text.get_height()))
            # self.text_health_control['player_text_rect'].y = int(self.rect.y - h*0.12152)

                # topleft=(self.rect.left + 105, int(self.rect.y - h*0.12152)))
            self.text_health_control['player_health_bar_outline_rect'].update((self.rect.x, self.rect.y - int(h*0.086)),
                                                                              (int(w*0.065), int(h*0.023)))
            self.text_health_control['player_health_bar_background_rect'].update((self.rect.x, self.rect.y - int(h*0.086)),
                                                                                 (int(w*0.065), int(h*0.023)))
            self.text_health_control['player_health_bar_rect'].update((self.rect.x, self.rect.y - int(h*0.086)), (
                self.text_health_control['player_health_level'], int(h*0.023)))
        if control == "left":
            self.walking_frame_num = self.walking_tick // 3

            self.image = self.reverse_walking_frames[self.walking_frame_num]
            direction.x -= 1
            self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                topright=(self.rect.right - 20, self.rect.y - 105))
            self.text_health_control['player_health_bar_outline_rect'].update((self.rect.right - 100, self.rect.y - 75),
                                                                              (100, 20))
            self.text_health_control['player_health_bar_background_rect'].update(
                (self.rect.right - 100, self.rect.y - 75),
                (100, 20))
            self.text_health_control['player_health_bar_rect'].update((self.rect.right - 100, self.rect.y - 75), (
                self.text_health_control['player_health_level'], 20))
        self.rect.move_ip(speed * dt * direction)
        self.text_health_control['player_health_bar_outline_rect'].move_ip(speed * dt * direction)
        self.text_health_control['player_health_bar_background_rect'].move_ip(speed * dt * direction)
        self.text_health_control['player_health_bar_rect'].move_ip(speed * dt * direction)
        self.walking_tick += 1

        if control == "jump":
            self.rect.y -= h*0.55
            self.text_health_control['player_text_rect'].y -= h*0.55
            self.text_health_control['player_health_bar_rect'].y -= h*0.55
            self.text_health_control['player_health_bar_background_rect'].y -= h*0.55
            self.text_health_control['player_health_bar_outline_rect'].y -= h*0.55

    def collision_blocker(self):#Fix
        if player1.rect.colliderect(player2.rect):
            if self.name == "Player 1":
                if player1.rect.x <= player2.rect.x:
                    player1.rect.right = player2.rect.left
                    self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                        topleft=(self.rect.left, self.rect.y - 105))
                    self.text_health_control['player_health_bar_outline_rect'].update(
                        (self.rect.left, self.rect.y - 75),
                        (100, 20))
                    self.text_health_control['player_health_bar_background_rect'].update(
                        (self.rect.left, self.rect.y - 75),
                        (100, 20))
                    self.text_health_control['player_health_bar_rect'].update((self.rect.left, self.rect.y - 75), (
                        self.text_health_control['player_health_level'], 20))


                else:
                    player1.rect.left = player2.rect.right
                    self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                        topright=(self.rect.right
                                  , self.rect.y - 105))
                    self.text_health_control['player_health_bar_outline_rect'].update(
                        (self.rect.right - 100, self.rect.y - 75),
                        (100, 20))
                    self.text_health_control['player_health_bar_background_rect'].update(
                        (self.rect.right - 100, self.rect.y - 75),
                        (100, 20))
                    self.text_health_control['player_health_bar_rect'].update((self.rect.right - 100, self.rect.y - 75),
                                                                              (
                                                                                  self.text_health_control[
                                                                                      'player_health_level'], 20))

            elif player2.rect.centerx <= player1.rect.centerx:
                player2.rect.right = player1.rect.left
                self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                    topleft=(self.rect.left, self.rect.y - 105))
                self.text_health_control['player_health_bar_outline_rect'].update(
                    (self.rect.left, self.rect.y - 75),
                    (100, 20))
                self.text_health_control['player_health_bar_background_rect'].update(
                    (self.rect.left, self.rect.y - 75),
                    (100, 20))
                self.text_health_control['player_health_bar_rect'].update((self.rect.left, self.rect.y - 75), (
                    self.text_health_control['player_health_level'], 20))
            else:
                player2.rect.left = player1.rect.right

                self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                    topright=(self.rect.right
                              , self.rect.y - 105))
                self.text_health_control['player_health_bar_outline_rect'].update(
                    (self.rect.right - 100, self.rect.y - 75),
                    (100, 20))
                self.text_health_control['player_health_bar_background_rect'].update(
                    (self.rect.right - 100, self.rect.y - 75),
                    (100, 20))
                self.text_health_control['player_health_bar_rect'].update((self.rect.right - 100, self.rect.y - 75),
                                                                          (
                                                                              self.text_health_control[
                                                                                  'player_health_level'], 20))

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

    def damage(self):#Fix

        if self.name == "Player 1":
            if player1.rect.colliderect(player2.rect) or player1.control['facing_right'] and (
                    player1.rect.right == player2.rect.left) or player1.control['facing_right'] == False and (
                    player1.rect.left == player2.rect.right):
                player2.text_health_control['player_health_level'] -= 20
                if player2.control['facing_right']:
                    player2.text_health_control['player_health_bar_rect'].update((player2.rect.x, player2.rect.y - 75),
                                                                                 (
                                                                                     player2.text_health_control[
                                                                                         'player_health_level'], 20))
                else:
                    player2.text_health_control['player_health_bar_rect'].update(
                        (player2.rect.right - 100, player2.rect.y - 75), (
                            player2.text_health_control['player_health_level'], 20))

        elif player1.rect.colliderect(player2.rect) or player2.control['facing_right'] and (
                player2.rect.right == player1.rect.left) or player2.control['facing_right'] == False and (
                player2.rect.left == player1.rect.right):

            player1.text_health_control['player_health_level'] -= 20
            if player1.control['facing_right']:
                player1.text_health_control['player_health_bar_rect'].update((player1.rect.x, player1.rect.y - 75), (
                    player1.text_health_control['player_health_level'], 20))
            else:
                player1.text_health_control['player_health_bar_rect'].update(
                    (player1.rect.right - 100, player1.rect.y - 75), (
                        player1.text_health_control['player_health_level'], 20))

    def health_detection(self, reset):

        if player1.text_health_control['player_health_level'] == 0:
            score_numbers[0] += 1
            Players.score = player_font.render('{}-{}'.format(int(score_numbers[0]), int(score_numbers[1])), True,
                                               "Black")
            sky.blit_Nat_Obj()
            grass.blit_Nat_Obj()
            screen.blit(Players.score, Players.score_rect)
            pygame.display.update()
            clock.tick(.5)

            reset = True
        elif player2.text_health_control['player_health_level'] == 0:
            score_numbers[1] += .5
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
        pygame.draw.rect(screen, "black", self.text_health_control['player_health_bar_outline_rect'], 2)
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
player1 = Players("Player 1", (w * .03, h * 0.8 - 2))
player2 = Players("Player 2", (w * .97, h * 0.8 - 2))

while running:
    pygame.event.set_allowed([pygame.QUIT])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if reset:
        player1 = Players("Player 1", (w * .03, h * 0.8 - 2))
        player2 = Players("Player 2", (w * .97, h * 0.8 - 2))
        reset = False

    speed = 1000
    dt = clock.tick(50) / 1000
    if play:
        sky.blit_Nat_Obj()
        grass.blit_Nat_Obj()
        reset=player1.update(reset)
        reset=player2.update(reset)
        pygame.mouse.set_visible(False)
    else:
        logo_tick, logo_frame, play = start_screen(logo_frame, logo_tick, play)

    pygame.display.update()
