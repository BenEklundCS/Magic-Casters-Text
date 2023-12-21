package com.beneklund.jcasters;

import java.util.ArrayList;

public class Action {
    private ArrayList<String> choices;
    private String prompt;

    Action(ArrayList<String> choices, String prompt) {
        this.choices = choices;
        this.prompt = prompt;
    }

    public String getPlayerChoice() {
        IO io = IO.getInstance();
        String choice;
        
        do {
            System.out.println(prompt);
            System.out.println(choices);
            io.printInputArrow();
            choice = io.getText();
            prompt = "Please enter a valid choice.";

        } while (!choices.contains(choice));
        
        return choice;
    }
}
