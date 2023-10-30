#pragma once

#include <stdint.h>

#include "gd32vf103_gpio.h"
#include "gd32vf103_spi.h"
#include "io.h"

class GD32_SPI {
    uint32_t _spi_dev;
    uint32_t _cs;
    uint32_t _sck;
    uint32_t _miso;
    uint32_t _mosi;
    spi_parameter_struct* _config;

   public:
    GD32_SPI(uint32_t spi_dev, uint32_t cs, uint32_t sck, uint32_t miso,
             uint32_t mosi, spi_parameter_struct* config);
    ~GD32_SPI();
    void begin();
    uint16_t transfer(uint16_t data);
    uint16_t transfer16(uint16_t data);
    void send(uint16_t data);
    uint16_t receive();
};
