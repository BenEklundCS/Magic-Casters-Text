package com.beneklund.jcasters;

public class Entity {
    private String name;
    private int health;
    private int maxHealth;
    private int mana;
    private int maxMana;
    private int attack;
    private int defense;
    private int gold;

    Entity(String name, int health, int maxHealth, int mana, int maxMana, int attack, int defense, int gold) {
        this.name = name;
        this.health = health;
        this.maxHealth = maxHealth;
        this.mana = mana;
        this.maxMana = maxMana;
        this.attack = attack;
        this.defense = defense;
        this.gold = gold;
    }


    public String getName() {
        return name;
    }
    public int getHealth() {
        return health;
    }
    public int getMaxHealth() {
        return maxHealth;
    }
    public int getMana() {
        return mana;
    }
    public int getMaxMana() {
        return maxMana;
    }
    public int getAttack() {
        return attack;
    }
    public int getDefense() {
        return defense;
    }
    public int getGold() {
        return gold;
    }

    // Setters

    public void setName(String name) {
        this.name = name;
    }
    public void setHealth(int health) {
        this.health = health;
    }
    public void setMaxHealth(int maxHealth) {
        this.maxHealth = maxHealth;
    }
    public void setMana(int mana) {
        this.mana = mana;
    }
    public void setMaxMana(int maxMana) {
        this.maxMana = maxMana;
    }
    public void setAttack(int attack) {
        this.attack = attack;
    }
    public void setDefense(int defense) {
        this.defense = defense;
    }
    public void setGold(int gold) {
        this.gold = gold;
    }
}
