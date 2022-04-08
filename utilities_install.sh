#!/bin/bash
# Usage: curl https://raw.githubusercontent.com/kris-classes/restart-s1-2022-JinZhuAW/main/utilities_install.sh | bash
# echo "Bash script to install all three packages Joe will present in the class."

#Image Scraper

pip install ImageScraper

#Terminal Image Viewer(tiv)

sudo apt install imagemagick
git clone httpshttps://github.com/stefanhaustein/TerminalImageViewer.git
cd TerminalImageViewer/src/main/cpp
make
sudo make install

#imgp

sudo apt-get install -y python3-pil
sudo apt install -y imgp
