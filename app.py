from flask import Flask
from flasgger import Swagger
from routes.animal_routes import animal_bp
from routes.employee_routes import employee_bp

app = Flask(__name__)

swagger = Swagger(app)


app.register_blueprint(animal_bp, url_prefix='/animals')
app.register_blueprint(employee_bp, url_prefix='/employees')

@app.route('/')
def home():
    """
    Home page providing information about the zoo and the employees.
    ---
    responses:
      200:
        description: A simple welcome page for the zoo
    """
    return """
    <html>
        <head>
            <title>Safari Zoo Management System</title>
        </head>
        <body>
            <h1>Selamat Datang di Kebun Binatang Safari Kami!</h1>
            <p>Ini adalah sistem manajemen kebun binatang, di mana Anda bisa mengelola informasi tentang hewan dan karyawan.</p>
            <h2>Fitur:</h2>
            <ul>
                <li>Kelola data hewan: tambah, update, hapus, dan lihat daftar hewan.</li>
                <li>Kelola data karyawan: tambah, update, hapus, dan lihat daftar karyawan.</li>
            </ul>
            <h3>Akses API:</h3>
            <p>Anda bisa mengakses API untuk manajemen hewan di <a href="/animals">/animals</a> dan manajemen karyawan di <a href="/employees">/employees</a>.</p>
            <p>Untuk dokumentasi API lengkap, Anda bisa mengunjungi <a href="/apidocs">/apidocs</a>.</p>
        </body>
    </html>
    """
