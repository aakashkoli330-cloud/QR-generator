import os
import io
import uuid
import base64
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

qr_store = {}


@app.route("/")
def index():
    return render_template("index.html", qr=None)


@app.route("/", methods=["POST"])
def generate():
    text = request.form.get("text", "").strip()
    if not text:
        return render_template("index.html", qr=None, error="Please enter some text or URL.")

    import qrcode
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    key = uuid.uuid4().hex
    qr_store[key] = buf.getvalue()

    img_b64 = base64.b64encode(qr_store[key]).decode()
    return render_template("index.html", qr=img_b64, key=key)


@app.route("/download/<key>")
def download(key):
    data = qr_store.get(key)
    if not data:
        return "QR code not found or expired.", 404
    return send_file(
        io.BytesIO(data),
        mimetype="image/png",
        as_attachment=True,
        download_name="qrcode.png"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
