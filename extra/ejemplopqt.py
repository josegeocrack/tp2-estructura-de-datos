import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt #nucleo del sistema, se necesita para funcionar
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget #elementos que vamos a crear, todos son widgets (ejemplo botón, checkbox, barra de carga, cuadro de texto, imagen, ventana)

#REMINDER
#cualquier elemento de la interfaz que yo vata a querer ver, modificar, escribir o algo desde alguna funcion, lo guardo como varibale de clase con el self.

#primer elemento q necesitamos si o si --> contenedor=ventana, una clase

class Ventanaprincipal(QMainWindow): #parent=quien la creó, para q si creo una ventna con mi ventana, no mueran los hijos
    
#arriba de todo defino las funciones de acciones de eventos y después creo el init dentro del cual voy a usar mis funciones
#FUNCIONES DE ACCIONES:

#BOTÓN CLICK --> AGREGAR ACCIÓN !! como hacer para ejecutar una funcion cuando toco el botón
    #al boton le puedo hacer doble click, mantener apretado, hacer click == eventos que suceden  cuando interactup con el boton
    #diferentes elementos tienen diferentes eventos que le pueden suceder
    def botoncambiartitulo_click(self):
        nuevotitulo=self.campotexto.toPlainText() #-->agarro lo que entra como texto al campo de texto y lo levanto para que quede de título
        self.setWindowTitle(nuevotitulo) #-->quiero que esto suceda cuando toco el botón
        self.campotexto.clear() #una vez que ejeutes lo de arriba y toques el botón, se borra lo q había en el campo de texto
    
#EJEMPLO 2 BOTON ALERT MESSAGE (para hacerlo buscar en internet pqt alert message)
    def mostrarcreds_click(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('More information')
        msg.setWindowTitle("Error")
        msg.exec_()

#EJEMPLO 3 ACTIVAR/DESACTIVAR BOTÓN (para hacer que no te deje tocar el boton si el campo de texto está vacio)
    #text changed porque quiero que esta función ocurra cada vez que cambia el texto, osea escribis una letra y se ejecuta y se fija q hace 
    def campotexto_textchanged(self):
        texto=self.campotexto.toPlainText()
        #desactivar el boton si la longitud del texto es vacío(pero para eso necesito hacer que el boton sea un self asi puedo modificarlo)
        if len(texto)==0:
            self.campotexto.setEnabled(False)
        else:
            self.campotexto.setEnabled(True)


#CREACIÓN DE MI CLASE VENTANA, INIT PARA EDITARLA
    def __init__(self) -> None:
        super().__init__()
        #para agregarle un título
        self.setWindowTitle("Mi primer programa con UI")
        #self.setWindowOpacity(1)
        #para cambiar su tamaño inicial --> posicion en x, posicion y, ancho, alto
        self.setGeometry(300,300, 500, 700)

#creación de un LAYOUT (vertical u horizontal) --> es un widget v u h depende de si agrego elemento a mi ventana, si quiero uno abajo del otro o al lado del otro
        #para layout HORIZONTAL
        #layoutprincipal=QHBoxLayout()

        #para layout VERTICAL: (todo esto medio por default)
        layoutprincipal=QVBoxLayout() #que mi ventana ponga elementos verticalmente
        #Establezco que el widget que contiene el layout sea el widget principal de mi ventana
        #creo un widget que tenga el layout que quiero, y hago que mi ventana muestre el layout de ESE widget que yo armé
        widgetlayout=QWidget()
        widgetlayout.setLayout(layoutprincipal) #que el layout de este widget sea el de mi ventana
        self.setCentralWidget(widgetlayout) #que el layout de mi ventana dependa de ese widget, entonces abro mi ventana y veo lo que tiene ese layout q cree

#creación de un LABEL que agrego al widget/layout (se agrega abajo de lo que ya haya)
        label1=QLabel("Bienvenidos al programa") #--> label es un texto que aparece en pantalla
        layoutprincipal.addWidget(label1) #agrego mi widget al layout (en este caso un texto)
        # label2=QLabel("Bienvenidos al programa") #--> label es un texto que aparece en pantalla
        # layoutprincipal.addWidget(label2) #agrego mi widget al layout (en este caso un texto)

#LO QUE QUIERO HACER ACÁ ABAJO -->le pido al usuario el nombre que quiere para la ventana, toca un boton y se cambia el nombre de la ventana

#creación de un SUBLAYOUT/LABEL con el que se accione
    #creo un sublayout que sea horizontal y que sea insertar algo: + un cuadro de texto para insertar 
    #creo el label que le dice lo que tiene q hacer al usuario
        layoutcambionombre=QHBoxLayout()
        layoutcambionombre.addWidget(QLabel("Inserte el nuevo nombre de la ventana: ")) #-->pongo el label directo ahí porq desp no necesito modificarlo
        layoutprincipal.addLayout(layoutcambionombre) #-->tengo que mostrar este widget en el principal !! porque si no nos los voy a ver
    #creo un campo de texto donde el usuario pueda meter el texto que quiera
    #lo voy a crear como una variable de CLASE para que se pueda usar en la funcion botonclick que está fuera del init   
        self.campotexto=QTextEdit()
        self.campotexto.textChanged.connect(self.campotexto_textchanged) #cada vez que el texto cambia, ya se que metés o sacás una letra, se va a llamar a la función que permite que el botón ande o deje de andar
        #campotexto.adjustSize()
        layoutcambionombre.addWidget(self.campotexto)
        
    #creo un botón        
        self.botoncambiartitulo=QPushButton()
        self.botoncambiartitulo.setText("CAMBIAR EL TÍTULO")
    #cuando clickeo, quiero que suceda algo, conecto el botón a una acción
        self.botoncambiartitulo.clicked.connect(self.botoncambiartitulo_click)
    #lo agrego al principal, no al horizontal, quiero que quede abajo
        layoutprincipal.addWidget(self.botoncambiartitulo)

#OTRO EJEMPLO BOTÓN
        mostrarcreditos=QPushButton()
        mostrarcreditos.setText("Mostrar créditos")
        mostrarcreditos.clicked.connect(self.mostrarcreds_click)
        layoutprincipal.addWidget(mostrarcreditos)

#PROGRAMA PRINCIPAL
if __name__=="__main__":
    app=QApplication(sys.argv) #creo la aplicacion con esto siempre, para que funcione pqt necesitamos crear esto
    window=Ventanaprincipal() #defino y creo mi ventana, la plantilla de mi ventana
    window.show() #para que funcione la tengo que abrir sí o sí
    app.exec() #para que el código siga corriendo mientras la ventana siga abierta, si no termina y no muestra la ventana