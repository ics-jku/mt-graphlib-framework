#pragma once

#include <stdint.h>

uint64_t millis(void);
uint64_t micros(void);
void sleep_u(uint64_t micros);
void sleep(uint64_t millis);

void delay(uint64_t millis);
void delayMicroseconds(uint64_t micros);
