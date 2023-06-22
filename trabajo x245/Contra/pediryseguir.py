import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Inicio de Sesión')
        self.setGeometry(300, 300, 300, 200)

        self.user_label = QLabel('Usuario:', self)
        self.user_label.move(20, 20)

        self.user_input = QLineEdit(self)
        self.user_input.move(80, 20)

        self.password_label = QLabel('Contraseña:', self)
        self.password_label.move(20, 60)

        self.password_input = QLineEdit(self)
        self.password_input.move(100, 60)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.submit_button = QPushButton('Iniciar Sesión', self)
        self.submit_button.move(100, 100)
        self.submit_button.clicked.connect(self.verify_credentials)

    def verify_credentials(self):
        usuario = self.user_input.text()
        contraseña = self.password_input.text()

        if verificar_credenciales(usuario, contraseña):
            self.close()
            self.usuario = usuario
            self.contraseña = contraseña
        else:
            self.user_input.setText('')
            self.password_input.setText('')
            QMessageBox.warning(self, 'Credenciales inválidas', 'Credenciales inválidas. Vuelve a intentarlo.')

def verificar_credenciales(usuario, contraseña):
    if usuario == "admin" and contraseña == "admin123":
        return True
    else:
        return False

if __name__ == '__main__':
    app = QApplication(sys.argv)

    while True:
        login_widget = LoginWidget()
        login_widget.show()
        app.exec_()

        if hasattr(login_widget, 'usuario') and hasattr(login_widget, 'contraseña'):
            break
        else:
            respuesta = QMessageBox.question(None, 'Salir', '¿Deseas salir del programa?',
                                             QMessageBox.Yes | QMessageBox.No)
            if respuesta == QMessageBox.Yes:
                sys.exit()

    apellido = input("Ingresa tu apellido: ")
    print("Usuario:", login_widget.usuario)
    print("Contraseña:", login_widget.contraseña)
    print("Apellido:", apellido)
