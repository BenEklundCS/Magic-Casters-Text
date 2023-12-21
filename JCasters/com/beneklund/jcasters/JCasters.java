package com.beneklund.jcasters;

import java.util.ArrayList;
import java.util.Arrays;

public class JCasters {
    private Player player;
    private IO io;

    // Constructor initializes the game
    public JCasters() {
        this.player = new Player("Name", 1, 1, 1, 1, 1, 1, 1);
        this.io = IO.getInstance();
    }

    public static void main(String[] args) {
        JCasters game = new JCasters(); // create a game instance / init
        game.io.clearTerminal();
        game.io.mainMenu();
        
        game.io.clearTerminal();
        
        
        ArrayList<String> list = new ArrayList(Arrays.asList("N", "S", "E", "W"));
        Action action = new Action(list,  "Please enter a direction: ");
        String string = action.getPlayerChoice();
        System.out.println(string);

        Player p = new Player("Name",1,1,1,1,1,1,1);
        String name = p.getName();
        System.out.println(name);
    }
}
