# Introduction #

[Wikipedia](http://en.wikipedia.org/wiki/FFmpeg):
> [FFmpeg](http://ffmpeg.mplayerhq.hu/) is a computer program that can record, convert and stream digital audio and video in numerous formats. FFmpeg is a command line tool that is composed of a collection of free software / open source libraries. It includes libavcodec, an audio/video codec library used by several other projects, and libavformat, an audio/video container mux and demux library. The name of the project comes from the MPEG video standards group, together with "FF" for "fast forward".


# Details #

FFmpeg is basically what allows DamnVid to convert videos very easily, quickly, and on-the-fly. FFmpeg is cross-platform, meaning that it can run on any operating system. Whenever DamnVid starts a conversion, you will see a new "ffmpeg" process on your computer; do not kill it, as it is the process doing the actual conversion. If you want to prevent it from eating too much priority, you can decrease its priority/niceness.

# Configuration #

Here is DamnVid's FFmpeg configuration:
```
--enable-memalign-hack --enable-libxvid --enable-libx264 --enable-libgsm --enable-libfaac --enable-libfaad --enable-libmp3lame --enable-libvorbis --enable-libtheora --enable-pthreads --enable-gpl --enable-static --disable-shared (--enable-avisynth on Windows)
```

FFmpeg's source is available in DamnVid's SVN repository (http://damnvid.googlecode.com/svn/trunk/) or at the [FFmpeg website](http://ffmpeg.mplayerhq.hu/).

# Building FFmpeg #
Various FFmpeg building tutorials are available on Google. Building FFmpeg is not the real difficulty here, but it's rather to put together all the libraries it uses. Here's what DamnVid needs: `avisynth` / `libxvid` / `libx264` / `libgsm` / `libfaac` / `libfaad` / `liba52` / `libmp3lame` / `libvorbis(ogg)` / `libtheora`.
Build (`make`) each library and link it to FFmpeg using `./configure`. Then proceed with the final `make` and `make install`, and you're done!