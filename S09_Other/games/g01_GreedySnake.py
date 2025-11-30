import pygame
import sys
import random

pygame.init()

# 游戏窗口设置
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 创建窗口和时钟
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇 - Snake Game")
clock = pygame.time.Clock()

# 字体
font = pygame.font.SysFont(None, 36)

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def get_random_position():
    return (
        random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
        random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
    )

def main():
    # 初始蛇的位置（从中间开始）
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = RIGHT
    next_direction = direction

    # 初始食物位置
    food = get_random_position()
    while food in snake:
        food = get_random_position()

    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        main()  # 重新开始游戏
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_UP and direction != DOWN:
                        next_direction = UP
                    elif event.key == pygame.K_DOWN and direction != UP:
                        next_direction = DOWN
                    elif event.key == pygame.K_LEFT and direction != RIGHT:
                        next_direction = LEFT
                    elif event.key == pygame.K_RIGHT and direction != LEFT:
                        next_direction = RIGHT

        if not game_over:
            direction = next_direction
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (
                (head_x + dx * GRID_SIZE) % WIDTH,
                (head_y + dy * GRID_SIZE) % HEIGHT
            )

            # 检查是否撞到自己
            if new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                # 检查是否吃到食物
                if new_head == food:
                    score += 1
                    food = get_random_position()
                    while food in snake:
                        food = get_random_position()
                else:
                    snake.pop()

        # 绘制
        screen.fill(BLACK)
        draw_grid()

        # 画蛇
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

        # 画食物
        pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

        # 显示分数
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if game_over:
            game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
