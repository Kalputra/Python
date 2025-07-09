import pygame,sys, random
from pygame.math import Vector2

pygame.init()
pygame.mixer.music.load("Sounds/bgmusic.mp3")

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)


GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 25
number_of_cells = 18
OFFSET = 75

class Food:
    def __init__(self, snake_body):
        self.position = self.generate_random_pos(snake_body)
        
    def draw(self):
        food_rect = pygame.Rect(OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)
        screen.blit(food_surface, food_rect)

    def generate_random_cell(self):
        x = random.randint(0, number_of_cells -1)
        y = random.randint(0, number_of_cells -1)
        return Vector2(x,y)
        
    def generate_random_pos(self, snake_body):
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()
        return position

class snake:
    def __init__(self):
        self.body = [Vector2(6, 9), Vector2(5,9), Vector2(4, 9)]
        self.body_direction = Vector2(1, 0)  # Initial direction to the right
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound("Sounds/eat.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("Sounds/wall.mp3")
        
    def draw(self):
        for segment in self.body: 
            segment_rect = (OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)
            
    def update(self):
        self.body.insert(0, self.body[0] + self.body_direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]

    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.body_direction = Vector2(1,0)
        
class Game:
    def __init__(self):
        self.snake = snake()
        self.food = Food(self.snake.body)
        self.state = "MENU"
        self.score = 0
        
    def draw(self):
        self.food.draw()
        self.snake.draw()
        
    def update(self):
        if self.state == "RUNNING":
            self.check_collision_with_food()
            self.check_collision_with_edges()
            self.snake.update()
            self.check_collision_with_tail()

    def draw_menu(self):
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  
        screen.blit(overlay, (0, 0))
        button_text = score_font.render("START GAME", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        pygame.draw.rect(screen, (50, 50, 50), button_rect.inflate(30, 20), border_radius=10)
        screen.blit(button_text, button_rect)

        return button_rect

    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
            self.snake.eat_sound.play()

    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()

    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0
        pygame.mixer.music.stop()
        self.snake.wall_hit_sound.play()

    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
                self.game_over()
    
    def draw_game_over(self):
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

    #Game Over Text
        over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        over_rect = over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))
        screen.blit(over_text, over_rect)

    # restart button
        pygame.mixer.music.play(-1)
        button_text = score_font.render("Restart?", True, (255, 255, 255))
        button_rect = button_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
        pygame.draw.rect(screen, (50, 50, 50), button_rect.inflate(30, 20), border_radius=10)
        screen.blit(button_text, button_rect)

        return button_rect

        
screen = pygame.display.set_mode((2*OFFSET + cell_size*number_of_cells, 2*OFFSET + cell_size*number_of_cells))

pygame.display.set_caption("retro snake")

clock = pygame.time.Clock()

game = Game()
food_surface = pygame.image.load("Makanan/food.png")

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

start_button_rect = pygame.Rect(0, 0, 0, 0) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if game.state == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.play(-1)
                    game.state = "RUNNING"
        if game.state == "STOPPED":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        game.snake = snake()
                        game.food = Food(game.snake.body)
                        game.score = 0
                        game.state = "RUNNING"

        if event.type == SNAKE_UPDATE and game.state == "RUNNING":
            game.update()

        if event.type == pygame.KEYDOWN:
            game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.body_direction != Vector2(0,1):
                game.snake.body_direction = Vector2(0, -1)   
            if event.key == pygame.K_DOWN and game.snake.body_direction != Vector2(0, -1):
                game.snake.body_direction = Vector2(0, 1) 
            if event.key == pygame.K_LEFT and game.snake.body_direction != Vector2(1, 0):
                game.snake.body_direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.body_direction != Vector2(-1, 0):
                game.snake.body_direction = Vector2(1, 0)

        
    #Drawing
    screen.fill(GREEN)
    pygame.draw.rect(screen, DARK_GREEN, 
        (OFFSET-5, OFFSET-5, cell_size*number_of_cells+10, cell_size*number_of_cells+10), 5)
    title_surface = title_font.render("Retro Snake", True, DARK_GREEN)
    screen.blit(title_surface, (OFFSET-5, 20))
    
    if game.state == "MENU":
        game.draw()
        start_button_rect = game.draw_menu() 
    elif game.state == "STOPPED":
        game.draw()
        restart_button_rect = game.draw_game_over()
    else:
        game.draw()
        
    if game.state != "MENU":
        score_surface = score_font.render(f"Score: {game.score}", True, DARK_GREEN)
        score_x = OFFSET + cell_size * number_of_cells - score_surface.get_width()
        score_y = OFFSET - score_surface.get_height() - 15
        screen.blit(score_surface, (screen.get_width() - score_surface.get_width() - 65, 20))
    
    pygame.display.update()
    clock.tick(60)