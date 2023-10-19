""" Chapter 1 module """
from chapter_one import intro_scene
from menus import title, main_menu

def main():
    """ Main function calling chapter1 intro_scene and title page """
    title()
    if main_menu() is True:
        intro_scene()
    else:
        quit()

if __name__ == "__main__":
    main()
