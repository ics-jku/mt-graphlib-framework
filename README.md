# Metamorphic Testing

This repository is used to perform metamorphic testing of the GD32 ILI9341 Graphics library called TFT_eSPI, which is available at https://github.com/Bodmer/TFT_eSPI.   
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

## *Verifying Embedded Graphics Libraries leveraging Virtual Prototypes and Metamorphic Testing*

[Christoph Hazott, Florian Stögmüller and Daniel Große. Verifying Embedded Graphics Libraries leveraging Virtual Prototypes and Metamorphic Testing. In ASP-DAC, 2024.
](https://ics.jku.at/files/2024ASPDAC_MTGraphicsVerification.pdf)

```
@inproceedings{HSG:2024,
  author =        {Christoph Hazott and Florian St\"ogm\"uller and
                   Daniel Gro{\ss}e},
  booktitle =     {ASP Design Automation Conf.},
  title =         {Verifying Embedded Graphics Libraries leveraging
                   Virtual Prototypes and Metamorphic Testing},
  year =          {2024},
}
```

