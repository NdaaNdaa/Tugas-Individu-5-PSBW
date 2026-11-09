from flask import Flask, abort, url_for, redirect, render_template

app = Flask(__name__)

# Daftar Username yang Terdaftar
username_terdaftar = ["ndaaa", "Hunter", "nanda123"]

# Daftar Data Member untuk Pengecekan "abort(404)"
data_member = {
    1: "ndaaa",
    2: "Hunter",
    3: "nanda123"
}

# Route untuk halaman Beranda
@app.route("/")
def beranda():
    return render_template("beranda.html")

# Route untuk kembali ke Halaman Beranda atau awal menggunakan redirect & url_for
@app.route("/awal")
def halaman_awal():
    return redirect(url_for("beranda"))

# Route untuk halaman Tentang
@app.route("/tentang")
def tentang():
    return render_template("tentang.html")

# Route untuk halaman Produk
@app.route("/produk")
def produk():
    return render_template("produk.html")

# Route untuk halaman Kontak
@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

# Dynamic Route Ke-1 : Memeriksa Username
@app.route("/cek/<username>")
def cek_username(username):

    # Kondisi 1 : Username Tidak Valid 
    if len(username) < 3 or len(username) > 15 or not username.isalnum():
        status = "tidak_valid" 

    # Kondisi 2 : Username Sudah Digunakan
    elif username in username_terdaftar:
        status = "sudah_dipakai"

    # Kondisi 3 : Username Tersedia
    else: 
        status = "tersedia"

    return render_template(
        "hasil_cek.html",
        username=username,
        status=status
    )

# Dynamic Route Ke-2 : Memeriksa Profil Member
@app.route("/user/<username>")
def profil_member(username):

    if username in username_terdaftar:
        return f"Member ditemukan ! Selamat Datang {username}"
    else:
        return "Member tidak Ditemukan ! Silahkan daftar terlebih dahulu."

@app.route("/member/<int:id>")
def detail_member(id):

    if id in data_member:
        return f"ID Member : {id} | Username : {data_member[id]}"
    else: 
        abort(404)

@app.route("/daftar-member")
def daftar_member():
    return render_template(
        "member.html",
        data_member=data_member
    )

# Custom Halaman Error 404
@app.errorhandler(404)
def halaman_tidak_ditemukan(error):
    return "Halaman tidak ditemukan Loh ya 😹.", 404
    
# Menjalankan Server Flask
if __name__=="__main__":
    app.run(debug=True)