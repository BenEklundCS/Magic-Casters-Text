package com.beneklund.jcasters;

public class JCasters {
    Player player;
    IO io;
    public static void main(String[] args) {
        MagicCasters game = new JCasters(); // create a game instance
        game.init();
    }
    // Helper function for game initialization
    private void init() {
        io = new IO(); // Initialize IO
        io.mainMenu();
        io.lineBreak();
        io.printText("Hello my name is Benjamin James Eklund and this is a super long string. I'm taking a final " +
                       "exam this morning, and I'm hoping to do really well!");
        // Player initialization
        player = new Player("Name", 1, 1, 1, 1,
                1, 1, 1);

    }
}
