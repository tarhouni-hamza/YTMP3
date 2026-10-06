# YouTube MP3 Downloader

A small Python script that downloads the audio of a YouTube video as an MP3 file.
Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [FFmpeg](https://ffmpeg.org/).

## Requirements

- Python 3.9+
- [FFmpeg](https://ffmpeg.org/download.html) installed and available in your `PATH`

| OS      | Install FFmpeg            |
|---------|---------------------------|
| Windows | `winget install ffmpeg`   |
| macOS   | `brew install ffmpeg`     |
| Ubuntu  | `sudo apt install ffmpeg` |

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/youtube-mp3-downloader.git
cd youtube-mp3-downloader
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Paste a YouTube link when asked. The MP3 is saved in the `downloads/` folder
(192 kbps, one video at a time).

## Troubleshooting

- **"FFmpeg not found"**: install FFmpeg, then restart your terminal.
- **Downloads suddenly fail**: YouTube changes often. Update the engine with
  `pip install -U yt-dlp`.

## Legal disclaimer

For personal use with content you own or have permission to download. Downloading
copyrighted material without permission may violate YouTube's Terms of Service and
copyright law in your country. You are responsible for how you use this software.

## License

[MIT](LICENSE)
