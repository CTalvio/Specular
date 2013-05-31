import unittest
import pygame
import sprites


class TestGameEngine(unittest.TestCase):

    def setUp(self):
        screen = pygame.display.set_mode((0,0))

    def tearDown(self):
        pygame.quit()

    def test_movement(self):
        move = sprites.calculate_angular_movement((0, 0), 0, 0)
        self.assertEqual(move, (0, 0))


class TestPlayer(unittest.TestCase):

    def setUp(self):
        screen = pygame.display.set_mode((0,0))

    def tearDown(self):
        pygame.quit()

    def test_creation(self):
        player = sprites.Player((0,0))
        self.assertEqual(player.life, 3)


class TestEnemies(unittest.TestCase):

    def setUp(self):
        screen = pygame.display.set_mode((0,0))

    def tearDown(self):
        pygame.quit()

    def test_creation_lv1(self):
        enemy = sprites.Enemy((0, 0), 4, sprites.enemy_lv1, 1)
        self.assertEqual(enemy.score, 4)

    def test_creation_lv2(self):
        enemy = sprites.Enemy((0, 0), 6, sprites.enemy_lv2, 0)
        self.assertEqual(enemy.score, 6)


suite = unittest.makeSuite(TestPlayer,'test')

if __name__ == "__main__":
    unittest.main()