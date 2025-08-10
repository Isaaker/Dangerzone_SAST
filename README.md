# Dangerzone_SAST

## Status:

[![Semgrep](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml/badge.svg)](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml)


## About

This action allows to integrate [Dangerzone like a SAST](https://github.com/freedomofpress/dangerzone), with this you can scann common documents like:

- PDF (.pdf)
- Microsoft Word (.docx, .doc)
- Microsoft Excel (.xlsx, .xls)
- Microsoft PowerPoint (.pptx, .ppt)
- ODF Text (.odt)
- ODF Spreadsheet (.ods)
- ODF Presentation (.odp)
- ODF Graphics (.odg)
- Hancom HWP (Hangul Word Processor) (.hwp, .hwpx)
- EPUB (.epub)
- Jpeg (.jpg, .jpeg)
- GIF (.gif)
- PNG (.png)
- SVG (.svg)
- other image formats (.bmp, .pnm, .pbm, .ppm)

Depending on the selected mode, this action will show an security alert or generate a safe copy of the document.

## Installation

Here there is an example github action you can use on your own repo:

```
name: SAST Dangerzone
jobs:
  sast_dangerzone:
    permissions:                                                                         
      contents: read
  uses:
  secrets: 
    token: ${{ secrets.GITHUB_TOKEN }}
```


## License
The code is under **Creative Commons Attribution-ShareAlike 4.0 International Public License**, view the [license here](https://spotify.piscinadeentropia.es/license)

![Creative Commons Attribution-ShareAlike 4.0 International Public License Logo](https://github.com/Isaaker/Spotify-AdsList/raw/main/docs/images/License-Image.jpeg)

## Contributing

To learn more about how to contribute to this repository, I recommend you read [CONTRIBUTING.md](https://spotify.piscinadeentropia.es/contributing)
