package com.beneklund.jcasters;

public class Goblin extends Monster {

    Goblin(String name, int health, int maxHealth, int mana, int maxMana, int attack, int defense, int gold) {
        super(name, health, maxHealth, mana, maxMana, attack, defense, gold);
    }

    public void attack() {
        return;
    }
}

