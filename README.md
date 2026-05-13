# QR Code Generator

A web-based QR code generator built with Python Flask. Enter text or a URL and get a downloadable QR code PNG instantly.

## Features

- Generate QR codes from any text or URL
- Clean, modern dark-themed UI
- One-click PNG download
- Responsive design (works on mobile)
- Deployed live at [qr-generator-e5x5.onrender.com](https://qr-generator-e5x5.onrender.com)

## Tech Stack

- **Backend:** Python, Flask, Gunicorn
- **QR Engine:** qrcode + Pillow
- **Frontend:** HTML, CSS (embedded)

## Local Development

`ash
pip install -r requirements.txt
python app.py
`

Visit \http://localhost:5000\ in your browser.

## License

MIT
