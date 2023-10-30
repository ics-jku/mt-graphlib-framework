# Metamorphic Testing

This repository is used to perform metamorphic testing of the GD32 ILI9341 Graphics library (https://git.ics.jku.at/florianstoegmueller/TFT_eSPI_GD32).   
It contains a Pyhton script which performs following step:   
1. Generate a test case
2. Compile the test case using the RISC-V (Nuclei) GCC
3. Run the test case on the VP and GUI (this produces screenshots)
4. Compare the screenshots
5. Store Results

## Prerequisites
- PlatformIO with working RISC-V (Nuclei) GCC
- Working Python3 environment 

## Requirements
- Metamorphic Testing repository
- GD32 VP + GUI

## HowTo
1. Clone Metamorphic repository
```
git clone https://github.com/ics-jku/metamorphic_testing.git
```
2. Clone RISCV-VP++ repository
```
git clone https://github.com/ics-jku/riscv-vp-plusplus.git
```
3. Install packages and build RISCV-VP++ according to README of RISCV-VP++
```
sudo apt install ...
make -j
```
4. Build GUI for display
```
cd /env/gd32/vp-breadboard
mkdir build
cd build
cmake ..
make
```
6. Edit "config.py" with your personal folder locations

Replace tokens in "<>" tags with your pathes e.g.
```
"BASE": "<METAMORPHIC_TESTING_CLONE_FOLDER>/",
"BASE": "/home/user/metamorphic_testing/",
```
5. Execute MT environment
```
python3 Main.py
```


