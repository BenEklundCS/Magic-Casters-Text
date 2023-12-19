package com.beneklund.jcasters;

public class JCasters {
    Player player;
    IO io;

    // Constructor initializes the game
    public JCasters() {
        this.player = new Player("Name", 1, 1, 1, 1, 1, 1, 1);
        this.io = new IO();
    }

    public static void main(String[] args) {
        JCasters game = new JCasters(); // create a game instance / init
        int attk = game.player.getAttack();
        System.out.println(attk);
    }
}
