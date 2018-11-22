#!/bin/bash
sudo apt-get --quiet update || echo 'apt-get update failed. Continuing...'
sudo apt-get --assume-yes install python-pip build-essential python-dev python-twisted
python setup.py install
pip install -r requirements.txt
mkdir "$HOME/.subspace"
cp subspace-cli.py "$HOME/.subspace/subspace-cli.py"
cp subspaced.py "$HOME/.subspace/subspaced.py"
cp subspace.conf "$HOME/.subspace/subspace.conf"
sudo cp subspace.sh /usr/bin/subspace
sudo chmod +x /usr/bin/subspace         
echo "Subspace v0.2 installation complete"
