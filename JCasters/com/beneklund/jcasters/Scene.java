package com.beneklund.jcasters;

import java.util.ArrayList;

class Scene {

    private ArrayList<Action> actions;
    private ArrayList<String> plot; // ["Initial text", ACTION, "Text..." etc]
    
    
    Scene(ArrayList<Action> actions, ArrayList<String> storyText) {
        this.actions = actions;
        this.storyText = storyText;
    }

}