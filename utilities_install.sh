#!/bin/bash
# Usage: curl https://raw.githubusercontent.com/JinZhuAW/PokemonGuessingGame/main/utilities_install.sh | bash
# echo "Bash script to install all three packages Joe will present in the class."

#Image scraper

pip install ImageScraper

#Terminal Image Viewer(tiv)

sudo apt install -y imagemagick
git clone https://github.com/stefanhaustein/TerminalImageViewer.git
cd TerminalImageViewer/src/main/cpp
sudo apt install -y g++
make
sudo make install

#imgp

sudo apt-get install -y python3-pil
sudo apt install -y imgp
