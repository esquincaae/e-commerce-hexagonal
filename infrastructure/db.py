from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """
    Inicializa la base de datos con la aplicación Flask.
    Se espera que la configuración de la aplicación ya contenga
    los detalles necesarios para la conexión de la base de datos.
    """
    db.init_app(app)

    with app.app_context():
        db.create_all()
