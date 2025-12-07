import pygame
import sys
import random

pygame.init()

# 屏幕设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("太空射击 - Space Shooter")
clock = pygame.time.Clock()
FPS = 60

# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 150, 255)

# 字体
font = pygame.font.SysFont(None, 36)

class Player:
    def __init__(self):
        self.width = 50
        self.height = 40
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - self.height - 20
        self.speed = 6
        self.lives = 3

    def move(self, dx):
        self.x += dx * self.speed
        # 边界限制
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

    def draw(self, surface):
        # 绘制飞船（三角形+矩形）
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
        pygame.draw.polygon(surface, BLUE, points)
        pygame.draw.rect(surface, BLUE, (self.x + 15, self.y + self.height, 20, 10))

    def get_rect(self):
        return pygame.Rect(self.x + 10, self.y, self.width - 20, self.height)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.radius = 3

    def update(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (self.x, self.y), self.radius)

    def is_off_screen(self):
        return self.y < 0

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(-100, -40)
        self.speed = random.uniform(1.0, 3.0)

    def update(self):
        self.y += self.speed

    def draw(self, surface):
        # 绘制敌机（倒三角）
        points = [
            (self.x + self.width // 2, self.y + self.height),
            (self.x, self.y),
            (self.x + self.width, self.y)
        ]
        pygame.draw.polygon(surface, RED, points)

    def is_off_screen(self):
        return self.y > HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x + 5, self.y, self.width - 10, self.height)

def main():
    player = Player()
    bullets = []
    enemies = []
    score = 0
    enemy_spawn_timer = 0
    game_over = False

    running = True
    while running:
        dt = clock.tick(FPS)

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        # 重启游戏
                        main()
                        return
                    elif event.key == pygame.K_q:
                        running = False
                else:
                    if event.key == pygame.K_SPACE:
                        # 发射子弹（从飞船顶部中心）
                        bullets.append(Bullet(player.x + player.width // 2, player.y))

        if not game_over:
            # 玩家移动
            keys = pygame.key.get_pressed()
            dx = 0
            if keys[pygame.K_LEFT]:
                dx = -1
            if keys[pygame.K_RIGHT]:
                dx = 1
            player.move(dx)

            # 生成敌人
            enemy_spawn_timer += dt
            if enemy_spawn_timer > 800:  # 每800毫秒生成一个
                enemies.append(Enemy())
                enemy_spawn_timer = 0

            # 更新子弹
            for bullet in bullets[:]:
                bullet.update()
                if bullet.is_off_screen():
                    bullets.remove(bullet)

            # 更新敌人
            for enemy in enemies[:]:
                enemy.update()
                if enemy.is_off_screen():
                    enemies.remove(enemy)

            # 碰撞检测：子弹 vs 敌人
            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if bullet.get_rect().colliderect(enemy.get_rect()):
                        if bullet in bullets:
                            bullets.remove(bullet)
                        if enemy in enemies:
                            enemies.remove(enemy)
                        score += 1
                        break  # 一颗子弹只打一个敌人

            # 碰撞检测：玩家 vs 敌人
            player_rect = player.get_rect()
            for enemy in enemies[:]:
                if player_rect.colliderect(enemy.get_rect()):
                    enemies.remove(enemy)
                    player.lives -= 1
                    if player.lives <= 0:
                        game_over = True

        # 绘制
        screen.fill(BLACK)

        # 绘制玩家
        player.draw(screen)

        # 绘制子弹
        for bullet in bullets:
            bullet.draw(screen)

        # 绘制敌人
        for enemy in enemies:
            enemy.draw(screen)

        # 显示分数和生命
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))

        if game_over:
            go_text = font.render("GAME OVER! Press R to Restart or Q to Quit", True, WHITE)
            screen.blit(go_text, (WIDTH // 2 - go_text.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
