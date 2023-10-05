sudo apt-get update
sudo apt-get install git python3-dev python3-pip
sudo pip3 install smbus2
git clone https://github.com/pololu/motoron-rpi.git
cd motoron-rpi
sudo python3 setup.py install
pip install evdev
