Plugin for CudaText.
It allows to format VBScript code.
If selection is made (only normal selection supported) then only selection is formatted, otherwise entire file is formatted.
Plugin gives commands in menu "Plugins".

Plugin has config file, which can be edited using two "Configure" commands:
- "Configure": opens config-file from plugin's folder, which is used when local file doesn't exist.
- "Configure (local)": opens config-file from the folder of currently active editor file. If local file doesn't exist, command suggests to copy global file into local name, and then opens it.

Author: Alexey Torgashin (CudaText)
License: MIT
