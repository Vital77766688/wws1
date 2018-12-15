from abc import ABC, abstractmethod
from hero import Hero


class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    def get_stats(self):
        return self.base.get_stats()

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractPositive(AbstractEffect):

    def get_positive_effects(self):
        positive_effects = self.base.get_positive_effects()
        positive_effects.append(type(self).__name__)
        return positive_effects


class AbstractNegative(AbstractEffect):

    def get_negative_effects(self):
        negative_effects = self.base.get_negative_effects()
        negative_effects.append(type(self).__name__)
        return negative_effects


class Berserk(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        characteristics = {
            "Strength": 7,
            "Endurance": 7,
            "Agility": 7,
            "Luck": 7,
            "Perception": -3,
            "Charisma": -3,
            "Intelligence": -3,
            "HP": 50
        }

        for key, value in characteristics.items():
            stats[key] += value

        return stats


class Blessing(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        characteristics = {
            "Strength": 2,
            "Perception": 2,
            "Endurance": 2,
            "Charisma": 2,
            "Intelligence": 2,
            "Agility": 2,
            "Luck": 2
        }

        for key, value in characteristics.items():
            stats[key] += value

        return stats


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        characteristics = {
            "Strength": -4,
            "Endurance": -4,
            "Agility": -4
        }

        for key, value in characteristics.items():
            stats[key] += value

        return stats


class EvilEye(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        characteristics = {
            "Luck": -10
        }

        for key, value in characteristics.items():
            stats[key] += value

        return stats


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        characteristics = {
            "Strength": -2,
            "Perception": -2,
            "Endurance": -2,
            "Charisma": -2,
            "Intelligence": -2,
            "Agility": -2,
            "Luck": -2
        }

        for key, value in characteristics.items():
            stats[key] += value

        return stats