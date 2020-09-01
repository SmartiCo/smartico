SmartiCo ESP8266 Core with rBoot
=================================

This is SmartiCo Core for ESP8266 with rboot support built in. It makes it super easy to use rBoot from comfort of Arduino IDE.

Installation
-------------

- Update the  {build.platform.path} in "platforms.txt" to point to the Arduino/ESP8266 core something like: C:\Users\Admin\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\2.7.2
- Update the {tools.esptool.esp8266path} in "platforms.txt" again, as done above. (Yes, its duplication but that's how IDE works)
- Ideally this shouldn't be needed but couldn't get the Arduino IDE working


RBoot
------
- This core already comes with RBoot bundled, which can be configured as per the project need. The configuration details can be found here: https://github.com/raburton/rboot
- Another good resource for understanding ESP8266 flash architecture is: https://www.pushrate.com/blog/articles/esp8266_boot.html
- Enable big memory support
    - Go to "platform.txt" of Arduino/ESP8266 core and note the value of {build.sdk} variable
    - Now go to the SDK directory, somewhere like: C:\Users\Admin\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\2.7.2\tools\sdk\lib\NONOSDK22x_190703
    - And run this command. You will find `xtensa-lx106-elf-objcopy` in "tools" directory, somewhere like C:\Users\Admin\AppData\Local\Arduino15\packages\esp8266\tools
    - Run the command: `xtensa-lx106-elf-objcopy -W Cache_Read_Enable_New libmain.a libmain2.a`
    - Rename the libmain.a to libmain1.a
    - Rename the libmain2.a to libmain.a
    - Copy the "rboot.h" and "bigmem/rboot-bigflash.c" in to the Arduino/ESP8266 core's main code base, somewhere like: C:\Users\Admin\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\2.7.2\cores\esp8266
    - Open the core_esp8266_main.cpp (found in same directory where you copied files in last step) and put following statement `#include "rboot-bigflash.c"`

Usage
--------
- Unlike Arduino/ESP8266 core, this core only supports commonly available ESP-12E module.
- You need to choose the appropriate Flash Configuratin from Arduino IDE (Tools --> Flash Size)
- You can also burn the bootloader using Arduino IDE (Tools --> Burn Bootloader). For this to work, make sure you have already built the rboot bootloader.


Notes
------
- For simplicity copied the variants from Arudino/ESP8266 core.
