**Ida-Pro-screen-recorder**

PyQt4/PyQt5 plugin for recording your screen while you use Ida Pro.

using modded version of [https://github.com/rdp/screen-capture-recorder-to-video-windows-free]()
Record full hd to mp4 using ffmpeg


**HowTo**

Its pretty important that you put Recorder.py in ida plugins folder, and recorder folder as a

subfolder to plugins folder \idafolder\plugins\recorder\

Add ffmpeg in  plugins/recorder/bin to Os PATH

Register filter with batch file located in plugins/recorder folder.

Qt-screen-capture.dll

Qt-screen-capture-x64.dll


after filters are registered you can check if filtersw are present.

`ffmpeg -list_devices true -f dshow -i dummy`

**OutPut**

`C:\Users\Storm Shadow>ffmpeg -list_devices true -f dshow -i dummy
ffmpeg version N-81036-g2b14204 Copyright (c) 2000-2016 the FFmpeg developers

[dshow @ 00000000026024a0] DirectShow video devices (some may be both video and audio devices)

[dshow @ 00000000026024a0]  "Qt-screen-capture"

[dshow @ 00000000026024a0]     Alternative name "@device_sw_{860BB310-5D01-11D0-BD3B-00A0C911CE86}\{4EA69364-2C8A-4AE6-A561-56E4B5044439}"`


Remember to un register filter and re register register filter if you move filters to another folder some day.


**Needed**

PyQt4 for 6.8

PyQt5 for 6.9

you should download the The Combined Community Codec Pack, its really minimal and have x64player and mp4 / mkv codecs.

http://www.cccp-project.net/

**Test quality**
https://www.youtube.com/watch?v=REt0VGSCDpw&feature=youtu.be

**Thx**

Roger for making capture filters

ffmpeg
