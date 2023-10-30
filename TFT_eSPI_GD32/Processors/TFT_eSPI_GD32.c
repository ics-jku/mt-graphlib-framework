        ////////////////////////////////////////////////////
        //       TFT_eSPI generic driver functions        //
        ////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////////////
// Global variables
////////////////////////////////////////////////////////////////////////////////////////

TFT_Interface _com = TFT_Interface();

/***************************************************************************************
** Function name:           pushBlock - for GD32
** Description:             Write a block of pixels of the same colour
***************************************************************************************/
void TFT_eSPI::pushBlock(uint16_t color, uint32_t len){

  while ( len-- ) {tft_Write_16(color);}
}

/***************************************************************************************
** Function name:           pushPixels - for GD32
** Description:             Write a sequence of pixels
***************************************************************************************/
void TFT_eSPI::pushPixels(const void* data_in, uint32_t len){

  uint16_t *data = (uint16_t*)data_in;

  if (_swapBytes) while ( len-- ) {tft_Write_16(*data); data++;}
  else while ( len-- ) {tft_Write_16S(*data); data++;}
}

/***************************************************************************************
** Function name:           writedata
** Description:             Send a 16 bit data value to the TFT
***************************************************************************************/
void TFT_eSPI::writedata16(uint16_t d){
  begin_tft_write();

  DC_D;        // Play safe, but should already be in data mode

  tft_Write_16(d);

  CS_L;        // Allow more hold time for low VDI rail

  end_tft_write();
}
