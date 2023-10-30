/**
 * The MIT License (MIT)
 *
 * title: a arduino library for GD32 EXMC
 *
 * Author: Seeed
 *
 * Copyright (C) 2019  Seeed Technology Co.,Ltd.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

#include "EXMC.h"

#include "gd32vf103_exmc.h"
#include "gd32vf103_gpio.h"
#include "gd32vf103_rcu.h"

EXMCClass::EXMCClass() {}

EXMCClass::~EXMCClass() {}

void EXMCClass::begin(uint32_t cmdPtrAddr, uint32_t datPtrAddr) {
    exmc_norsram_parameter_struct lcd_init_struct;
    exmc_norsram_timing_parameter_struct lcd_timing_init_struct;

    /* EXMC clock enable */
    rcu_periph_clock_enable(RCU_EXMC);
    rcu_periph_clock_enable(RCU_AF);
    /* GPIO clock enable */
    rcu_periph_clock_enable(RCU_GPIOD);
    rcu_periph_clock_enable(RCU_GPIOE);

    /* configure EXMC_D[0~15]*/
    /* PD14(EXMC_D0), PD15(EXMC_D1),PD0(EXMC_D2), PD1(EXMC_D3), PD8(EXMC_D13),
     * PD9(EXMC_D14), PD10(EXMC_D15) */
    gpio_init(GPIOD, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ,
              GPIO_PIN_0 | GPIO_PIN_1 | GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 |
                  GPIO_PIN_14 | GPIO_PIN_15);

    /* PE7(EXMC_D4), PE8(EXMC_D5), PE9(EXMC_D6), PE10(EXMC_D7), PE11(EXMC_D8),
       PE12(EXMC_D9), PE13(EXMC_D10), PE14(EXMC_D11), PE15(EXMC_D12) */
    gpio_init(GPIOE, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ,
              GPIO_PIN_7 | GPIO_PIN_8 | GPIO_PIN_9 | GPIO_PIN_10 | GPIO_PIN_11 |
                  GPIO_PIN_12 | GPIO_PIN_13 | GPIO_PIN_14 | GPIO_PIN_15);

    /* configure PD11(EXMC_A16) */
    gpio_init(GPIOD, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ, GPIO_PIN_11);

    /* configure NOE and NWE */
    gpio_init(GPIOD, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ,
              GPIO_PIN_4 | GPIO_PIN_5);

    /* configure EXMC NE0 */
    gpio_init(GPIOD, GPIO_MODE_AF_PP, GPIO_OSPEED_50MHZ, GPIO_PIN_7);

    lcd_timing_init_struct.bus_latency = 1;
    lcd_timing_init_struct.asyn_data_setuptime = 10;
    lcd_timing_init_struct.asyn_address_holdtime = 2;
    lcd_timing_init_struct.asyn_address_setuptime = 5;

    lcd_init_struct.norsram_region = EXMC_BANK0_NORSRAM_REGION0;
    lcd_init_struct.asyn_wait = DISABLE;
    lcd_init_struct.nwait_signal = DISABLE;
    lcd_init_struct.memory_write = ENABLE;
    lcd_init_struct.nwait_polarity = EXMC_NWAIT_POLARITY_LOW;
    lcd_init_struct.databus_width = EXMC_NOR_DATABUS_WIDTH_16B;
    lcd_init_struct.memory_type = EXMC_MEMORY_TYPE_SRAM;
    lcd_init_struct.address_data_mux = ENABLE;
    lcd_init_struct.read_write_timing = &lcd_timing_init_struct;

    exmc_norsram_init(&lcd_init_struct);

    exmc_norsram_enable(EXMC_BANK0_NORSRAM_REGION0);

    cmdPtr = reinterpret_cast<volatile uint16_t *>(cmdPtrAddr);
    datPtr = reinterpret_cast<volatile uint16_t *>(datPtrAddr);
}

void EXMCClass::end() { exmc_norsram_disable(EXMC_BANK0_NORSRAM_REGION0); }

uint8_t EXMCClass::command(uint8_t cmd) { return (*cmdPtr = cmd); }

uint8_t EXMCClass::transfer(uint8_t data) { return (*datPtr = data); }

uint16_t EXMCClass::transfer16(uint16_t data) { return (*datPtr = data); }

void EXMCClass::transfer(void *buf, uint32_t count) {
    uint8_t *buffer = reinterpret_cast<uint8_t *>(buf);
    for (uint32_t i = 0; i < count; i++) {
        *buffer = transfer(*buffer);
        buffer++;
    }
}
