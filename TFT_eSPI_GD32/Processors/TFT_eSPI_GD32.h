        ////////////////////////////////////////////////////
        //       TFT_eSPI GD32 driver functions        //
        ////////////////////////////////////////////////////

// This is a driver for GD32VF103 boards, it supports SPI and 16bit parallel interface displays

#ifndef _TFT_eSPI_GD32VF103H_
#define _TFT_eSPI_GD32VF103H_

#include <math.h>

#include "../TFT_Interface.h"
#include "../gd32_libopt.h"
#include "GD32/GD32_SPI.h"
#include "GD32/Print.h"
#if defined(TOUCH)
#include "GD32/GD32_SPI.h"
#endif

// Processor ID reported by getSetup()
#define PROCESSOR_ID 0x0000

// Include processor specific header
// None

// Processor specific code used by SPI bus transaction startWrite and endWrite functions
#define SET_BUS_WRITE_MODE // Not used
#define SET_BUS_READ_MODE  // Not used

// Code to check if DMA is busy, used by SPI bus transaction startWrite and endWrite functions
#define DMA_BUSY_CHECK // Not used so leave blank

// To be safe, SUPPORT_TRANSACTIONS is assumed mandatory
#if !defined (SUPPORT_TRANSACTIONS)
  #define SUPPORT_TRANSACTIONS
#endif

// Initialise processor specific SPI functions, used by init()
#define INIT_TFT_DATA_BUS

// If smooth fonts are enabled the filing system may need to be loaded
#ifdef SMOOTH_FONT
  // Call up the filing system for the anti-aliased fonts
  //#define FS_NO_GLOBALS
  //#include <FS.h>
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Define the DC (TFT Data/Command or Register Select (RS))pin drive code
////////////////////////////////////////////////////////////////////////////////////////
#ifndef TFT_DC
  #define DC_C // No macro allocated so it generates no code
  #define DC_D // No macro allocated so it generates no code
#else
  #define DC_C digitalWrite(TFT_DC, LOW)
  #define DC_D digitalWrite(TFT_DC, HIGH)
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Define the CS (TFT chip select) pin drive code
////////////////////////////////////////////////////////////////////////////////////////
#ifndef TFT_CS
  #define CS_L // No macro allocated so it generates no code
  #define CS_H // No macro allocated so it generates no code
#else
  #define CS_L digitalWrite(TFT_CS, LOW)
  #define CS_H digitalWrite(TFT_CS, HIGH)
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Make sure TFT_RD is defined if not used to avoid an error message
////////////////////////////////////////////////////////////////////////////////////////
#ifndef TFT_RD
  #define TFT_RD -1
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Define the WR (TFT Write) pin drive code
////////////////////////////////////////////////////////////////////////////////////////
#ifdef TFT_WR
  #define WR_L digitalWrite(TFT_WR, LOW)
  #define WR_H digitalWrite(TFT_WR, HIGH)
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Define the touch screen chip select pin drive code
////////////////////////////////////////////////////////////////////////////////////////
#if !defined TOUCH_CS || (TOUCH_CS < 0)
  #define T_CS_L // No macro allocated so it generates no code
  #define T_CS_H // No macro allocated so it generates no code
#else
  #define T_CS_L digitalWrite(TOUCH_CS, LOW)
  #define T_CS_H digitalWrite(TOUCH_CS, HIGH)
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Make sure TFT_MISO is defined if not used to avoid an error message
////////////////////////////////////////////////////////////////////////////////////////
#ifndef TFT_MISO
  #define TFT_MISO -1
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Macros to write commands/pixel colour data to a SPI ILI948x TFT
////////////////////////////////////////////////////////////////////////////////////////

#define tft_Write_8(C)   _com.transfer(C)
#define tft_Write_16(C)  _com.transfer16(C)
#define tft_Write_16S(C) _com.transfer16(((C)>>8) | ((C)<<8))

#define tft_Write_32(C)            \
tft_Write_8(C >> 24);              \
tft_Write_8((C & 0xFFFFFF) >> 16); \
tft_Write_8((C & 0xFFFF) >> 8);    \
tft_Write_8(C & 0xFF)

#define tft_Write_32C(C,D)         \
tft_Write_8((uint8_t) ((C) >> 8)); \
tft_Write_8((uint8_t) ((C)));      \
tft_Write_8((uint8_t) ((D) >> 8)); \
tft_Write_8((uint8_t) ((D)));

#define tft_Write_32D(C)           \
tft_Write_8((uint8_t) ((C) >> 8)); \
tft_Write_8((uint8_t) ((C)));      \
tft_Write_8((uint8_t) ((C) >> 8)); \
tft_Write_8((uint8_t) ((C)));

#ifndef tft_Write_16N
  #define tft_Write_16N tft_Write_16
#endif

////////////////////////////////////////////////////////////////////////////////////////
// Macros to read from display using SPI or software SPI
////////////////////////////////////////////////////////////////////////////////////////
#if defined (TFT_SDA_READ)
  // Use a bit banged function call for STM32 and bi-directional SDA pin
  #define TFT_eSPI_ENABLE_8_BIT_READ // Enable tft_Read_8(void);
  #define SCLK_L digitalWrite(TFT_SCLK, LOW)
  #define SCLK_H digitalWrite(TFT_SCLK, LOW)
#else
  // Use a SPI read transfer
  #define tft_Read_8() _com.transfer(0)
#endif


#endif // Header end
