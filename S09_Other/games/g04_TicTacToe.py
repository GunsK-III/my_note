import pygame
import sys
import math

# 初始化 pygame
pygame.init()

# 常量
WIDTH, HEIGHT = 600, 700
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE
LINE_WIDTH = 15
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
CIRCLE_RADIUS = CELL_SIZE // 3
SPACE = CELL_SIZE // 4

# 颜色
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (66, 66, 66)
BUTTON_HOVER_COLOR = (50, 50, 50)

# 设置屏幕
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("井字棋 - Tic Tac Toe (人机对战)")
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 40)

# 游戏状态
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
player = 'O'  # 人类先手
game_over = False
winner = None

def draw_board():
    screen.fill(BG_COLOR)
    # 画网格线
    for i in range(1, BOARD_SIZE):
        # 垂直线
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), LINE_WIDTH)
        # 水平线
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (col * CELL_SIZE + CELL_SIZE // 2,
                                    row * CELL_SIZE + CELL_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                # 左上到右下
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                                 (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                                 CROSS_WIDTH)
                # 右上到左下
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE),
                                 (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE),
                                 CROSS_WIDTH)

def check_winner(board):
    # 检查行
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    # 检查列
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    # 检查对角线
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ''
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ''
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '':
                board[row][col] = 'X'
                score = minimax(board, 0, False)
                board[row][col] = ''
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = 'X'

def reset_game():
    global board, player, game_over, winner
    board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player = 'O'
    game_over = False
    winner = None

def draw_status():
    if game_over:
        if winner:
            text = f"{'AI (X)' if winner == 'X' else 'You (O)'} Wins!"
        else:
            text = "It's a Draw!"
        status_text = font.render(text, True, TEXT_COLOR)
        screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, WIDTH + 20))
    else:
        turn_text = "Your Turn (O)" if player == 'O' else "AI Thinking... (X)"
        status_text = small_font.render(turn_text, True, TEXT_COLOR)
        screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, WIDTH + 20))

def draw_restart_button():
    button_rect = pygame.Rect(WIDTH // 2 - 80, HEIGHT - 60, 160, 50)
    mouse_pos = pygame.mouse.get_pos()
    color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    restart_text = small_font.render("Restart", True, TEXT_COLOR)
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT - 50))
    return button_rect


# 主循环
running = True
while running:
    draw_board()
    draw_figures()
    draw_status()
    button_rect = draw_restart_button()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

        if not game_over and player == 'O':
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if mouseY < WIDTH:  # 点击在棋盘内
                    clicked_row = mouseY // CELL_SIZE
                    clicked_col = mouseX // CELL_SIZE
                    if board[clicked_row][clicked_col] == '':
                        board[clicked_row][clicked_col] = 'O'
                        winner = check_winner(board)
                        if winner or is_board_full(board):
                            game_over = True
                        else:
                            player = 'X'  # 切换到 AI

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                reset_game()

    # AI 自动下棋
    if not game_over and player == 'X':
        ai_move()
        winner = check_winner(board)
        if winner or is_board_full(board):
            game_over = True
        else:
            player = 'O'

    pygame.display.flip()

pygame.quit()
sys.exit()
