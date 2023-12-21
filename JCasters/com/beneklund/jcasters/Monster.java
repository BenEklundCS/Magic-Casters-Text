package com.beneklund.jcasters;

// Abstract class for monsters in the game, I can create subclasses for monsters (Goblin, Shadow Figure, Etc)

public abstract class Monster extends Entity {

    Monster(String name, int health, int maxHealth, int mana, int maxMana, int attack, int defense, int gold) {
        super(name, health, maxHealth, mana, maxMana, attack, defense, gold);
    }

}