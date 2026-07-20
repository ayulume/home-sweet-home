import shutil
import sys
import os

def intro():
    print("Welcome to the Home Sweet Home dotfiles install wizard!\n")
    print("This program will guide you through the installation of the Home Sweet Home dotfiles.\n")
    confirmation = input("Do you wish to install the Home Sweet Home dotfiles? (y/n) ")
    return confirmation.lower() == 'y'

def main():
    if not intro():
        print("Installation aborted.")
        sys.exit(1)

    # Check if pacman is present
    if shutil.which("pacman"):
        print("Cloning/Installing: Paru, base-devel...")
        os.system("sudo pacman -S --noconfirm --needed git base-devel")
        os.system("git clone https://aur.archlinux.org/paru.git")
        os.chdir("paru")
        os.system("makepkg -si --noconfirm")
        os.chdir("..")

        print("Installing some apps...")
        os.system("sudo pacman -S --noconfirm niri kitty waybar swaybg zsh mako xdg-desktop-portal-gnome xwayland-satellite neovim fastfetch nautilus")
        os.system("paru -S --noconfirm vicinae bibata-modern-classic")

        print("Cloning: Home-Sweet-Home")
        os.system("git clone https://github.com/seqyu/home-sweet-home.git")
        os.chdir("home-sweet-home")

        print("Copying some more files where they belong")
        os.makedirs(os.path.expanduser("~/.config"), exist_ok=True)
        os.system("sudo cp -rf .config/* ~/.config/")
        os.system("sudo cp -rf .themes ~/")
        os.makedirs(os.path.expanduser("~/Pictures"), exist_ok=True)
        os.system("sudo cp -rf wallpaper.png ~/Pictures/wallpaper.png")
        print("The installation was successful. You can now log out and start Niri.")
        print("Main keybinds you should know:")
        print("Super+Space: Open the app launcher")
        print("Super+Q: Quit the selected application")
        print("Super+arrow keys: Select a window")
        print("Ctrl+Super+arrow keys: Move your windows")
        print("Super+T: Open a terminal window")
        print("Super+F: Fullscreen a window")
        print("Super+Shift+E: Log out")
        print("Default keyboard layout: US")
        sys.exit(0)
    else:
        print("The installation was unsuccessful.")
        print("The Home Sweet Home installer is intended to be used on Arch Linux-based systems. Please install the dotfiles manually or switch to an Arch Linux-based distribution.")
        sys.exit(1)

if __name__ == "__main__":
    main()
