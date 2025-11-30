import pygame
import sys
import random

pygame.init()

# 屏幕与网格设置
GRID_WIDTH, GRID_HEIGHT = 15, 15
CELL_SIZE = 30
PADDING = 2
WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("迷宫寻宝 - Maze Runner")
clock = pygame.time.Clock()
FPS = 30

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)  # 玩家
RED = (255, 50, 50)  # 宝藏
GREEN = (50, 255, 100)  # 出口
WALL_COLOR = (40, 40, 40)
PATH_COLOR = (220, 220, 220)

# 字体
font = pygame.font.SysFont(None, 36)

# 方向：(dy, dx)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def generate_maze(width, height):
    """使用 DFS（递归回溯）生成完美迷宫"""
    # 初始化：1 表示墙，0 表示通路
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def dfs(y, x):
        maze[y][x] = 0  # 标记为通路
        random.shuffle(DIRECTIONS)
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy * 2, x + dx * 2
            if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] == 1:
                # 打通中间的墙
                maze[y + dy][x + dx] = 0
                dfs(ny, nx)

    # 从 (1,1) 开始（确保边界是墙）
    dfs(1, 1)
    return maze


def find_dead_ends(maze):
    """找出所有死胡同（只有一条邻居的通路）"""
    dead_ends = []
    h, w = len(maze), len(maze[0])
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if maze[y][x] == 0:
                neighbors = 0
                for dy, dx in DIRECTIONS:
                    if maze[y + dy][x + dx] == 0:
                        neighbors += 1
                if neighbors == 1:  # 死胡同
                    dead_ends.append((y, x))
    return dead_ends


def draw_maze(maze, player_pos, treasure_pos, exit_pos, treasure_collected):
    screen.fill(WALL_COLOR)
    h, w = len(maze), len(maze[0])
    for y in range(h):
        for x in range(w):
            rect = pygame.Rect(x * CELL_SIZE + PADDING, y * CELL_SIZE + PADDING,
                               CELL_SIZE - 2 * PADDING, CELL_SIZE - 2 * PADDING)
            if maze[y][x] == 0:
                pygame.draw.rect(screen, PATH_COLOR, rect)
            else:
                pygame.draw.rect(screen, WALL_COLOR, rect)

    # 画宝藏（如果还没拿到）
    if not treasure_collected and treasure_pos:
        ty, tx = treasure_pos
        pygame.draw.circle(screen, RED,
                           (tx * CELL_SIZE + CELL_SIZE // 2,
                            ty * CELL_SIZE + CELL_SIZE // 2),
                           CELL_SIZE // 3)

    # 画出口（只有拿到宝藏才显示）
    if treasure_collected and exit_pos:
        ey, ex = exit_pos
        pygame.draw.rect(screen, GREEN,
                         (ex * CELL_SIZE + PADDING * 2,
                          ey * CELL_SIZE + PADDING * 2,
                          CELL_SIZE - PADDING * 4,
                          CELL_SIZE - PADDING * 4))

    # 画玩家
    py, px = player_pos
    pygame.draw.circle(screen, BLUE,
                       (px * CELL_SIZE + CELL_SIZE // 2,
                        py * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 3)


def main():
    # 生成迷宫
    maze = generate_maze(GRID_WIDTH, GRID_HEIGHT)

    # 设置起点（固定为 (1,1)）
    player_pos = [1, 1]

    # 随机选一个死胡同放宝藏
    dead_ends = find_dead_ends(maze)
    if dead_ends:
        treasure_pos = random.choice(dead_ends)
    else:
        treasure_pos = (GRID_HEIGHT - 2, GRID_WIDTH - 2)  # fallback

    # 出口位置（右下角）
    exit_pos = (GRID_HEIGHT - 2, GRID_WIDTH - 2)

    treasure_collected = False
    game_won = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_won:
                    if event.key == pygame.K_r:
                        main()  # 重启
                        return
                    elif event.key == pygame.K_q:
                        running = False
                else:
                    dy, dx = 0, 0
                    if event.key == pygame.K_UP:
                        dy = -1
                    elif event.key == pygame.K_DOWN:
                        dy = 1
                    elif event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1

                    new_y = player_pos[0] + dy
                    new_x = player_pos[1] + dx
                    # 检查是否在范围内且不是墙
                    if GRID_HEIGHT > new_y >= 0 == maze[new_y][new_x] and 0 <= new_x < GRID_WIDTH:
                        player_pos[0] = new_y
                        player_pos[1] = new_x

                    # 检查是否捡到宝藏
                    if not treasure_collected and tuple(player_pos) == treasure_pos:
                        treasure_collected = True

                    # 检查是否到达出口（需已拿宝藏）
                    if treasure_collected and tuple(player_pos) == exit_pos:
                        game_won = True

        # 绘制
        draw_maze(maze, player_pos, treasure_pos, exit_pos, treasure_collected)

        if game_won:
            win_text = font.render("You Found the Treasure & Escaped! Press R to Replay", True, WHITE)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
    