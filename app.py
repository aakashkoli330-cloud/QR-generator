import os
import io
import uuid
import base64
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

qr_store = {}


@app.route("/")
def index():
    return render_template("index.html", qr=None, recent=[])


@app.route("/", methods=["POST"])
def generate():
    text = request.form.get("text", "").strip()
    fg = request.form.get("fg", "#000000")
    bg = request.form.get("bg", "#ffffff")
    size = request.form.get("size", "md")

    size_map = {"sm": 6, "md": 10, "lg": 14}
    box_size = size_map.get(size, 10)

    if not text:
        return render_template("index.html", qr=None, error="Please enter some text or URL.", recent=qr_store.get("_recent", []))

    import qrcode
    import qrcode.image.svg

    qr = qrcode.QRCode(version=1, box_size=box_size, border=4)
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg, back_color=bg)
    buf_png = io.BytesIO()
    img.save(buf_png, format="PNG")
    buf_png.seek(0)

    factory = qrcode.image.svg.SvgPathImage
    img_svg = qr.make_image(image_factory=factory, fill_color=fg, back_color=bg)
    svg_bytes = img_svg.to_string()
    if isinstance(svg_bytes, str):
        svg_bytes = svg_bytes.encode("utf-8")

    key = uuid.uuid4().hex
    qr_store[key] = {
        "png": buf_png.getvalue(),
        "svg": svg_bytes,
        "text": text,
        "fg": fg,
        "bg": bg,
    }

    recent = qr_store.get("_recent", [])
    recent.insert(0, {"text": text[:30], "key": key, "fg": fg, "bg": bg})
    qr_store["_recent"] = recent[:5]

    img_b64 = base64.b64encode(qr_store[key]["png"]).decode()
    return render_template("index.html", qr=img_b64, key=key, recent=recent)


@app.route("/download/<key>/<fmt>")
def download(key, fmt):
    data = qr_store.get(key)
    if not data:
        return "QR code not found or expired.", 404
    if fmt == "svg":
        return send_file(
            io.BytesIO(data["svg"]),
            mimetype="image/svg+xml",
            as_attachment=True,
            download_name="qrcode.svg"
        )
    return send_file(
        io.BytesIO(data["png"]),
        mimetype="image/png",
        as_attachment=True,
        download_name="qrcode.png"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
