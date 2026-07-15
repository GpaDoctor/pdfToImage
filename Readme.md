1. mkdir file

2. python -m venv venv

3. Activate

Windows:  venv\Scripts\activate.bot
Linux:    source venv/bin/activate

3. pip install pdf2image

4. Install poppler

Link: https://github.com/oschwartz10612/poppler-windows

Mac:    brew install poppler
Linux:   Bash  sudo apt-get install poppler-utils
Windows:  winget install -e --id oschwartz10612.Poppler

5. Test

pdftoppm -h

6. Rmb change path in pdfToImageCon.py

7. python pdfToImageCon.py
