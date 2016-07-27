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
  built with gcc 5.4.0 (GCC)
  configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-dxva2 --enable-libmfx --enable-nvenc --enable-avisynth --enable-bzlib --enable-libebur128 --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libfreetype --enable-libgme --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-libzimg --enable-lzma --enable-decklink --enable-zlib
  libavutil      55. 28.100 / 55. 28.100
  libavcodec     57. 50.100 / 57. 50.100
  libavformat    57. 42.100 / 57. 42.100
  libavdevice    57.  0.102 / 57.  0.102
  libavfilter     6. 47.100 /  6. 47.100
  libswscale      4.  1.100 /  4.  1.100
  libswresample   2.  1.100 /  2.  1.100
  libpostproc    54.  0.100 / 54.  0.100
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
