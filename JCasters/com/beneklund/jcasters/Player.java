package com.beneklund.jcasters;

public class Player extends Entity {

    // Constructor

    Player(String name, int health, int maxHealth, int mana, int maxMana, int attack, int defense, int gold) {
        super(name, health, maxHealth, mana, maxMana, attack, defense, gold);
    }
}
