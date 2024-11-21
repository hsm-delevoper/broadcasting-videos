echo "Updating the package list..."
sudo apt update


echo "Installing FFmpeg..."
sudo apt install -y ffmpeg

echo "Installing Python and PIP..."
sudo apt install -y python3 python3-pip


echo "Installing the necessary Python libraries..."
pip3 install numpy

if command -v ffmpeg &> /dev/null; then
    echo "FFmpeg has been successfully installed!"
    ffmpeg -version
else
    echo "Error: FFmpeg is not installed."
fi


if command -v python3 &> /dev/null; then
    echo "Python has been successfully installed!"
    python3 --version
else
    echo "Error: Python is not installed."
fi


if command -v pip3 &> /dev/null; then
    echo "PIP has been successfully installed!"
    pip3 --version
else
    echo "Error: PIP is not installed."
fi

echo "The installation is complete!"
read -p "Do you want to launch Script of streaming? (y/n): " choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    echo "Running the script..."
    python3 streaming.py
else
    echo "The script will not run."
fi