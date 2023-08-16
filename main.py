# Stick Wacker Game

# Imports
import pygame

pygame.init()

# Getting width and height of window
w, h = pygame.display.get_desktop_sizes()[0]
#w, h = 1300, 700
screen = pygame.display.set_mode((w, h))
screen.fill("White")
clock = pygame.time.Clock()
running = True
player_font = pygame.font.Font('Assets/RobotoMono-Bold.ttf', 20)


class Players(pygame.sprite.Sprite):

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

        self.player_text = player_font.render(self.name, True, "Blue")
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
                'player_health_level': 100,
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topleft=(self.rect.x, self.rect.y - 100)),
                "player_health_bar_rect": pygame.Rect((self.rect.x, self.rect.y - 70), (100, 20)),
                "player_health_bar_background_rect": pygame.Rect((self.rect.x, self.rect.y - 70), (100, 20)),
                "player_health_bar_outline_rect": pygame.Rect((self.rect.x, self.rect.y - 70), (100, 20))
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
                'player_health_level': 100,
                "player_text": self.player_text,
                "player_text_rect": self.player_text.get_rect(topright=(self.rect.right, self.rect.y - 100)),
                "player_health_bar_rect": pygame.Rect((self.rect.right - 100, self.rect.y - 70), (100, 20)),
                "player_health_bar_background_rect": pygame.Rect((self.rect.right - 100, self.rect.y - 70), (100, 20)),
                "player_health_bar_outline_rect": pygame.Rect((self.rect.right - 100, self.rect.y - 70), (100, 20))

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

        if self.rect.x <= -250:
            self.rect.x = w + 140
        elif self.rect.x >= w + 140:
            self.rect.x = -250

    def move2(self, control):
        direction = pygame.Vector2()

        if self.walking_frame_num == 5:
            self.walking_frame_num = 0
            self.walking_tick = 0
        if control == "right":
            self.walking_frame_num = self.walking_tick // 3

            self.image = self.walking_frames[self.walking_frame_num]
            direction.x += 1
            self.text_health_control['player_text_rect'] = self.player_text.get_rect(
                topleft=(self.rect.x + 20, self.rect.y - 105))
            self.text_health_control['player_health_bar_outline_rect'].update((self.rect.x, self.rect.y - 75),
                                                                              (100, 20))
            self.text_health_control['player_health_bar_background_rect'].update((self.rect.x, self.rect.y - 75),
                                                                                 (100, 20))
            self.text_health_control['player_health_bar_rect'].update((self.rect.x, self.rect.y - 75), (
                self.text_health_control['player_health_level'], 20))
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
            self.rect.y -= 450
            self.text_health_control['player_text_rect'].y -= 450
            self.text_health_control['player_health_bar_rect'].y -= 450
            self.text_health_control['player_health_bar_background_rect'].y -= 450
            self.text_health_control['player_health_bar_outline_rect'].y -= 450

    def collision_blocker(self):
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
        if player1.rect.colliderect(player2.rect):
            print(2)

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
            if player1.rect.colliderect(player2.rect) or player1.control['facing_right'] and (player1.rect.right == player2.rect.left) or player1.control['facing_right']==False and (player1.rect.left == player2.rect.right):
                player2.text_health_control['player_health_level'] -= 20
                if player2.control['facing_right']:
                    player2.text_health_control['player_health_bar_rect'].update((player2.rect.x, player2.rect.y - 75), (
                        player2.text_health_control['player_health_level'], 20))
                else:
                    player2.text_health_control['player_health_bar_rect'].update(
                        (player2.rect.right - 100, player2.rect.y - 75), (
                            player2.text_health_control['player_health_level'], 20))

        elif player1.rect.colliderect(player2.rect) or player2.control['facing_right'] and (player2.rect.right == player1.rect.left) or player2.control['facing_right']==False and (player2.rect.left == player1.rect.right):


            player1.text_health_control['player_health_level'] -= 20
            if player1.control['facing_right']:
                player1.text_health_control['player_health_bar_rect'].update((player1.rect.x, player1.rect.y - 75), (
                    player1.text_health_control['player_health_level'], 20))
            else:
                player1.text_health_control['player_health_bar_rect'].update(
                    (player1.rect.right - 100, player1.rect.y - 75), (
                        player1.text_health_control['player_health_level'], 20))


    def blit(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text_health_control['player_text'], self.text_health_control['player_text_rect'])
        pygame.draw.rect(screen, "blue", self.rect, 1)
        pygame.draw.rect(screen, "red", self.text_health_control['player_health_bar_background_rect'])
        pygame.draw.rect(screen, "green", self.text_health_control['player_health_bar_rect'])
        pygame.draw.rect(screen, "black", self.text_health_control['player_health_bar_outline_rect'], 2)

    def update(self):
        self.blit()

        self.gravity()
        self.move1()
        self.collision_blocker()


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
player1 = Players("Player 1", (w * .03, h * 0.8-2))
player2 = Players("Player 2", (w * .97, h * 0.8-2))

while running:
    pygame.event.set_allowed([pygame.QUIT])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    speed = 1000
    dt = clock.tick(50) / 1000
    sky.blit_Nat_Obj()
    grass.blit_Nat_Obj()
    player1.update()
    player2.update()
    pygame.display.update()
