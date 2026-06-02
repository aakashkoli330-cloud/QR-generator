# QR Code Generator

A web-based QR code generator built with Python Flask. Enter text or a URL, customize colors and size, and download your QR code as PNG or SVG instantly.

## Context

QR codes are everywhere — product packaging, business cards, restaurant menus, event tickets. This tool was built to provide a simple, fast way to generate QR codes without signing up for a paid service or dealing with bloated online generators.

It's designed for developers, designers, small business owners, and anyone who needs a QR code quickly. The entire app runs as a single Flask server with no database or external API dependencies.

## Features

- Generate QR codes from any text or URL
- Custom dot color and background color via color picker
- Three size options: Small, Medium, Large
- Download as PNG or SVG vector format
- Copy QR code image to clipboard
- Recent history of generated codes (last 5)
- Clean tool-like UI with two-column layout
- Responsive design (works on mobile)
- Deployed live at [qr-generator-e5x5.onrender.com](https://qr-generator-swov.onrender.com)

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask, Gunicorn |
| QR Engine | qrcode + Pillow (PNG), qrcode SVG factory (SVG) |
| Frontend | HTML, CSS (separate file), Vanilla JS |
| Deployment | Render (Web Service) |
| Version Control | Git, GitHub |

## How It Works

1. Enter text or paste a URL
2. Choose colors and size
3. Submit the form — Flask generates the QR code server-side
4. Download PNG or SVG, or copy the image to clipboard

QR codes are stored in memory during your session and served for download. No data is persisted to disk or a database.

## Project Structure

```
qr-generator/
├── app.py              # Flask application (routes, QR generation)
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version for Render
├── static/
│   └── style.css       # All styling (separate from HTML)
├── templates/
│   └── index.html      # HTML template with Jinja2
├── .gitignore
└── README.md
```

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` in your browser.

## Deployment

The app is configured for Render. Push to GitHub and connect:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

## License

MIT
