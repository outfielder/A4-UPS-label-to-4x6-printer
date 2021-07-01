
# UPS A4 PDF label processor to 4x6 Thermal printer 

This program takes in the regular A4 PDF labels given by UPS and converts them so that they can be printed using a regular 4x6 inch thermal printer. This is only for Windows based operating systems, however, can be easily adapted for other operating systems, so contributions are highly welcome!


## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Dependencies

This project requires you to download and install [IrfanView](https://www.irfanview.com/). Either of the 32-bit or the 64-bit version are fine to use.

If you want to use the python version of the program then you would need [Python3](https://www.python.org/downloads/) and the [opencv](https://pypi.org/project/opencv-python/) and the [pdf2image](https://pypi.org/project/pdf2image/) libraries.

## How to use

1. Install [IrfanView](https://www.irfanview.com/) and copy the full path of the IrfanView Windows executable (i_view32.exe or i_view64.exe file) using the "Copy Path" button in the Windows explorer ensuring you do not remove the quotation marks from the path.
2. Add the IrfanView path to the config.ini file.
3. Start the IrfanView program and open any image in it.
4. Click on file then on print.
5. Ensure your settings are the same as the settings shown below and make sure to save them without printing.
![App Screenshot](https://raw.githubusercontent.com/outfielder/munbyn-thermal-UPS/master/images/irfan_settings.PNG)
6. Add any UPS A4 PDF labels to the same folder as the program.
7. Ensure that the default printer on your computer is the label printer you wish to have the labels printed to. Refer to [this](https://support.microsoft.com/en-us/windows/how-to-set-a-default-printer-in-windows-10-e10cf8b8-e596-b102-bf84-c41022b5036f) article if you are unsure on how to do so.
8. Run the UPS_label.exe script and it should automatically process your UPS labels and send them to the printer. It it recommended to run the executable using cmd instead, so that you can see any errors should they arise.

**Please note:** For the sake of simplicity, the program will process any PDF in the same folder as it and send it to the printer, so ensure that you only have PDFs that you want processed and printed in the same folder as the program.
  
## Demo

[Here]() is a link to a YouTube video with a tutorial on how to install IrfanView and run this program.

  