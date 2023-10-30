/**
    The MIT License (MIT)

    A interface abstraction layer

    Copyright (C) 2019  Seeed Technology Co.,Ltd.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to
   deal in the Software without restriction, including without limitation the
   rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
   sell copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
   IN THE SOFTWARE.
*/
#include <TFT_Interface.h>

TFT_Interface::TFT_Interface() {}

TFT_Interface::~TFT_Interface() {}

void TFT_Interface::begin() {
    interface_begin();
    return;
}

void TFT_Interface::end() {
    interface_end();
    return;
}

byte TFT_Interface::transfer(uint8_t data) { return interface_transfer(data); }

uint16_t TFT_Interface::transfer16(uint16_t data) {
    return interface_transfer16(data);
}
void TFT_Interface::transfer(void* buf, int count) {
    return interface_transfer(buf, count);
}

void TFT_Interface::beginTransaction() {}
void TFT_Interface::endTransaction() {}

void TFT_Interface::writeCommand(uint8_t c) { interface_writeCommand(c); }

void TFT_Interface::writeData(uint8_t d) { interface_writeData(d); }
