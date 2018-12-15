import unittest
import hero
import main


class TestBaff(unittest.TestCase):
    def setUp(self):
        self.hero = hero.Hero()

    def test_base_hero_stats(self):
        stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }
        self.assertDictContainsSubset(stats, self.hero.get_stats())

    def test_berserk(self):
        h = main.Berserk(self.hero)
        stats = {
            "HP": 178,  # 128+50
            "Strength": 22,  # 15+7
            "Perception": 1,  # 4-3
            "Endurance": 15,  # 8+7
            "Charisma": -1,  # 2-3
            "Intelligence": 0,  # 3-3
            "Agility": 15,  # 8+7
            "Luck": 8  # 1+7
        }
        self.assertDictContainsSubset(stats, h.get_stats())
        self.assertEqual(h.get_positive_effects(), ['Berserk'])
        self.assertEqual(h.get_negative_effects(), [])

    def test_blessing(self):
        h = main.Blessing(self.hero)
        stats = {
            "Strength": 17,
            "Perception": 6,
            "Endurance": 10,
            "Charisma": 4,
            "Intelligence": 5,
            "Agility": 10,
            "Luck": 3
        }
        self.assertDictContainsSubset(stats, h.get_stats())
        self.assertEqual(h.get_positive_effects(), ['Blessing'])
        self.assertEqual(h.get_negative_effects(), [])

    def test_weakness(self):
        h = main.Weakness(self.hero)
        stats = {
            "Strength": 11,
            "Perception": 4,
            "Endurance": 4,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 4,
            "Luck": 1
        }
        self.assertDictContainsSubset(stats, h.get_stats())
        self.assertEqual(h.get_positive_effects(), [])
        self.assertEqual(h.get_negative_effects(), ['Weakness'])

    def test_evileye(self):
        h = main.EvilEye(self.hero)
        stats = {
            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": -9  # 1-10
        }
        self.assertDictContainsSubset(stats, h.get_stats())
        self.assertEqual(h.get_positive_effects(), [])
        self.assertEqual(h.get_negative_effects(), ['EvilEye'])

    def test_curse(self):
        h = main.Curse(self.hero)
        stats = {
            "Strength": 13,
            "Perception": 2,
            "Endurance": 6,
            "Charisma": 0,
            "Intelligence": 1,
            "Agility": 6,
            "Luck": -1
        }
        self.assertDictContainsSubset(stats, h.get_stats())
        self.assertEqual(h.get_positive_effects(), [])
        self.assertEqual(h.get_negative_effects(), ['Curse'])

    def test_two_buffs(self):
        h = main.Curse(main.Berserk(main.EvilEye(self.hero)))

        self.assertEqual(h.get_positive_effects(), ['Berserk'])
        self.assertEqual(h.get_negative_effects(), ['EvilEye', 'Curse'])


if __name__ == '__main__':
    unittest.main()