import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
#from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    #创建一个用于子弹的编组
    bullets = Group()

    #创建一个外星人
    #alien = Alien(ai_settings, screen)
    #创建一组外星人
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()