**Ida-Pro-screen-recorder**

PyQt4/PyQt5 plugin for recording your screen while you use Ida Pro.

using modded version of [https://github.com/rdp/screen-capture-recorder-to-video-windows-free]()
Record full hd to mp4 using ffmpeg


**HowTo**

Add ffmpeg in  plugins/recorder/bin to Os PATH

Register filter with batch file located in plugins/recorder folder.

Qt-screen-capture.dll

Qt-screen-capture-x64.dll

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
