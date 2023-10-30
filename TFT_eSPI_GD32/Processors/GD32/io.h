#pragma once

#include "pins.h"

void pinMode(pin_size_t pinNumber, PinMode pinMode);
void digitalWrite(pin_size_t pinNumber, PinStatus status);
PinStatus digitalRead(pin_size_t pinNumber);
void digitalToggle(pin_size_t pinNumber);
