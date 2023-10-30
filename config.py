PATHS = {
    "BASE": "<METAMORPHIC_TESTING_CLONE_FOLDER>/",
    "SDK": "<HOME>/.platformio/packages/framework-nuclei-sdk/",
    "GCC": "<HOME>/.platformio/packages/toolchain-riscv-gcc-nuclei/bin/riscv-nuclei-elf-gcc",
    "GUI": "<RISCV_VP++_CLONE_FOLDER>/env/gd32/vp-breadboard/build/vp-breadboard",
    "VP": "<RISCV_VP++_CLONE_FOLDER>/vp/build/bin/gd32-vp",
    "TESTCASES": "<METAMORPHIC_TESTING_CLONE_FOLDER>/testcases/"
}
BUILD = {
    "COMPILE": "-c -Os -Wall -ffunction-sections -fdata-sections -fno-common -march=rv32imac -mabi=ilp32 -mcmodel=medlow -DPLATFORMIO=60105 -DDOWNLOAD_MODE=DOWNLOAD_MODE_FLASHXIP -DNO_RTOS_SERVICE -I. -I"+PATHS['BASE']+"TFT_eSPI_GD32 -I"+PATHS['SDK']+"NMSIS/Include -I"+PATHS['SDK']+"NMSIS/Core/Include -I"+PATHS['SDK']+"NMSIS/DSP/Include -I"+PATHS['SDK']+"NMSIS/NN/Include -I"+PATHS['SDK']+"SoC/gd32vf103/Common/Include -I"+PATHS['SDK']+"SoC/gd32vf103/Board/gd32vf103v_eval/Include",
    "LINK": "-T "+PATHS['SDK']+"SoC/gd32vf103/Board/gd32vf103v_eval/Source/GCC/gcc_gd32vf103_flashxip.ld -Os -ffunction-sections -fdata-sections -fno-common -Wl,--gc-sections -march=rv32imac -mabi=ilp32 -mcmodel=medlow -nostartfiles --specs=nano.specs --specs=nosys.specs -u _isatty -u _write -u _sbrk -u _read -u _close -u _fstat -u _lseek -L. -L"+PATHS['BASE']+"lib -L"+PATHS['SDK']+"NMSIS/Library/DSP/GCC -L"+PATHS['SDK']+"NMSIS/Library/NN/GCC -Wl,--start-group "+PATHS['BASE']+"lib/gd32vf103/libsoc_gd32vf103.a "+PATHS['BASE']+"lib/gd32vf103/Board/libboard_gd32vf103v_eval.a -lTFT_eSPI_GD32 -lgcc -lm -lstdc++ -Wl,--end-group",
}
