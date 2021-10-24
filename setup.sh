clear
echo "downloading files..."
sleep 1
sudo apt-get install npm nodejs python3
clear
sudo dnf install npm nodejs python3
clear
sudo pacman -S npm nodejs python3
clear
sudo npm init
clear
npm install discord.js@12.0.0 --save-dev
clear
python3 main.py
clear
rm main.py
clear
echo "now you can launch it by writing node index.js"
echo "enjoy!"
rm setup.sh
