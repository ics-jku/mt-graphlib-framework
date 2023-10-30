#include "sleep.h"

#include "gd32vf103.h"

uint64_t millis(void) {
    return (uint64_t)(SysTimer_GetLoadValue() * (4000.F / SystemCoreClock));
}

uint64_t micros(void) {
    return (uint64_t)(SysTimer_GetLoadValue() * (4000000.0 / SystemCoreClock));
}

void sleep(uint64_t millis) { sleep_u(millis * 1000); }

void sleep_u(uint64_t micros) {
    volatile uint64_t then =
        SysTimer_GetLoadValue() + ((micros * SOC_TIMER_FREQ) / (1000 * 1000));
    while (SysTimer_GetLoadValue() < then) {
    }
}

void delay(uint64_t millis) { sleep(millis); }

void delayMicroseconds(uint64_t micros) {sleep_u(micros); }
