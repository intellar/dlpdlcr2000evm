#
#output_format:
#   1: DPI_OUTPUT_FORMAT_9BIT_666
#   2: DPI_OUTPUT_FORMAT_16BIT_565_CFG1
#   3: DPI_OUTPUT_FORMAT_16BIT_565_CFG2
#   4: DPI_OUTPUT_FORMAT_16BIT_565_CFG3
#   5: DPI_OUTPUT_FORMAT_18BIT_666_CFG1
#   6: DPI_OUTPUT_FORMAT_18BIT_666_CFG2
#   7: DPI_OUTPUT_FORMAT_24BIT_888
#
#rgb_order:
#   1: DPI_RGB_ORDER_RGB
#   2: DPI_RGB_ORDER_BGR
#   3: DPI_RGB_ORDER_GRB
#   4: DPI_RGB_ORDER_BRG
#
#output_enable_mode:
#   0: DPI_OUTPUT_ENABLE_MODE_DATA_VALID
#   1: DPI_OUTPUT_ENABLE_MODE_COMBINED_SYNCS
#
#invert_pixel_clock:
#   0: RGB Data changes on rising edge and is stable at falling edge
#   1: RGB Data changes on falling edge and is stable at rising edge.
#
#hsync/vsync/output_enable_polarity:
#   0: default for HDMI mode
#   1: inverted
#
#3hsync/vsync/oe phases:
#   0: DPI_PHASE_POSEDGE
#   1: DPI_PHASE_NEGEDGE
#  
#   
#   

dpi_output_format = 458773

output_format          = (dpi_output_format >>  0) & 0xf;
rgb_order              = (dpi_output_format >>  4) & 0xf;

output_enable_mode     = (dpi_output_format >>  8) & 0x1;
invert_pixel_clock     = (dpi_output_format >>  9) & 0x1;

hsync_disable          = (dpi_output_format >> 12) & 0x1;
vsync_disable          = (dpi_output_format >> 13) & 0x1;
output_enable_disable  = (dpi_output_format >> 14) & 0x1;

hsync_polarity         = (dpi_output_format >> 16) & 0x1;
vsync_polarity         = (dpi_output_format >> 17) & 0x1;
output_enable_polarity = (dpi_output_format >> 18) & 0x1;

hsync_phase            = (dpi_output_format >> 20) & 0x1;
vsync_phase            = (dpi_output_format >> 21) & 0x1;
output_enable_phase    = (dpi_output_format >> 22) & 0x1;
aa=0