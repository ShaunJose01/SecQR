
from flask import render_template, redirect, request
import secrets
import qrcode

@app.route("/")
def index():
    return render_template('layout.html')

@app.route("/gen_qrcode", methods=["POST", "GET"])
def index_page():
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.data.data
            image_name = f"{secrets.token_hex(10)}.png"
            qrcode_loc = f"{app.config['UPLOAD_PATH']}/{image_name}"

            try:
                my_qrcode = qrcode.make(str(data))
                my_qrcode.save(qrcode_loc)
            except Exception as e:
                print(e)

            return render_template('gen_qr.html', title='Generated')
    else:
        return render_template("gen_qr.html", title='Index Page',form=form)
