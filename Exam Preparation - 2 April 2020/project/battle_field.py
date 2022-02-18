from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        attacker.health += sum(c.health_points for c in attacker.card_repository.cards)
        enemy.health += sum(c.health_points for c in enemy.card_repository.cards)

        if attacker.health <= 0 or enemy.health <= 0:
           raise ValueError('Player is dead!')

        if attacker.__class__.__name__ == 'Beginner':
              attacker.health += 40
              for c in attacker.card_repository.cards:
                  c.damage_points += 30

        if enemy.__class__.__name__ == 'Beginner':
              enemy.health += 40
              for c in enemy.card_repository.cards:
                  c.damage_points += 30

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)

