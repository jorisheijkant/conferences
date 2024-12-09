# Transcribe conferences

A quick tool to load in end-of-year conferences and transcribe them. Possibly later some AI-analysis tools will be added.

## Prerequisites

This tool is written in python. Please use a seperate python environment like conda to install the dependencies, which are listed in the `requirements.txt`. Run `pip install requirements.txt` to install.

### Downloading the conferences

The shows are on youtube, use a tool like `yt-dlp` to download them, for instance using the command `yt-dlp -x --audio-format mp3 [URL]`. Place these mp3's in the `audio_source/` folder.

### Transcribing

Use the `python transcribe_all.py` command to transcribe the shows. N.B.: this will take a long time, preferably use a computer with a decent graphics card (cuda-enabled is a bonus). The transcriptions will be output to the `texts/` folder.
