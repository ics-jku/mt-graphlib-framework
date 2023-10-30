#include "GD32_SPI.h"

GD32_SPI::GD32_SPI(uint32_t spi_dev, uint32_t cs, uint32_t sck, uint32_t miso,
                   uint32_t mosi, spi_parameter_struct* config)
    : _spi_dev{spi_dev}, _cs{cs}, _sck{sck}, _miso{miso}, _mosi{mosi}, _config{config} {
    begin();
}

GD32_SPI::~GD32_SPI() {}

void GD32_SPI::begin() {
    /******* RCU *******/
    rcu_periph_clock_enable(RCU_AF);
    switch (_spi_dev) {
        case SPI0:
            rcu_periph_clock_enable(RCU_SPI0);
            break;
        case SPI1:
            rcu_periph_clock_enable(RCU_SPI1);
            break;
        case SPI2:
            rcu_periph_clock_enable(RCU_SPI2);
            break;

        default:
            break;
    }

    /******* GPIO *******/
    pinMode(_cs, OUTPUT);          // CS
    pinMode(_sck, OUTPUT_AF_PP);   // SCK
    pinMode(_miso, INPUT);         // MISO
    pinMode(_mosi, OUTPUT_AF_PP);  // MOSI

    /******* SPI *******/
    spi_i2s_deinit(_spi_dev);
    spi_init(_spi_dev, _config);

    spi_enable(_spi_dev);
}

uint16_t GD32_SPI::transfer(uint16_t data) {
    while (spi_i2s_flag_get(_spi_dev, SPI_FLAG_TBE) != SET)
        ;

    spi_i2s_data_transmit(_spi_dev, data);

    while (spi_i2s_flag_get(_spi_dev, SPI_FLAG_RBNE) != SET)
        ;

    return spi_i2s_data_receive(_spi_dev);
}

uint16_t GD32_SPI::transfer16(uint16_t data) {
    return transfer(data) << 8 | transfer(data);
}

void GD32_SPI::send(uint16_t data) {
    while (spi_i2s_flag_get(_spi_dev, SPI_FLAG_TBE) != SET)
        ;

    spi_i2s_data_transmit(_spi_dev, data);
}

uint16_t GD32_SPI::receive() {
    while (spi_i2s_flag_get(_spi_dev, SPI_FLAG_RBNE) != SET)
        ;

    return spi_i2s_data_receive(_spi_dev);
}
