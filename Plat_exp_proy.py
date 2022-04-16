from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDialog, QMessageBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.layout = QVBoxLayout()
        self.label_1 = QLabel("Bienvenido a la plataforma de análisis de esquizofrenia en etapas tempranas.")
        self.label_1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label_1.setFont(QtGui.QFont("Arial", 15))
        self.layout.addWidget(self.label_1)
        
        self.label_2 = QLabel("ATENCIÓN:\nEste sistema solo debe usarse como apoyo para el dignóstico del paciente.")
        self.label_2.setAlignment(Qt.AlignLeft | Qt.AlignBottom)
        self.label_2.setFont(QtGui.QFont("Arial", 7))
        self.label_2.setStyleSheet('color:red')
        self.layout.addWidget(self.label_2)

        self.setLayout(self.layout)
        
        self.title = "Soporte para diagnóstico de esquizofrenia"
        self.top = 50
        self.left = 50
        self.width = 550
        self.height = 520
        self.iconName = "assets/esq.png"

        self.InitWindow()
        self.BotonSalir()
        self.BotonExaminar()
        self.BotonPacientes()

        self.show()

    def InitWindow(self):
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('assets/brain.jpg'))
        self.label.setGeometry(0,30,700,500)
        
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def BotonSalir(self):
        button = QPushButton("Salir", self)
        button.move(575,465)
        button.setIcon(QtGui.QIcon("assets/salir.png"))
        button.clicked.connect(self.ClickExit)

    def BotonExaminar(self):
        button = QPushButton("Examinar", self)
        button.move(375,465)
        button.setIcon(QtGui.QIcon("assets/analizar.png"))
        button.clicked.connect(self.ClickAnalizar)

    def BotonPacientes(self):
        button = QPushButton("Pacientes", self)
        button.move(475,465)
        button.setIcon(QtGui.QIcon("assets/pacientes.png"))
        button.clicked.connect(self.ClickPacientes)

    def ClickExit(self):
        sys.exit()

    def ClickPacientes(self):
        print("Under construction...")

    def ClickAnalizar(self):
        message = QMessageBox.question(self, "Pregunta FE", "El paciente padece de epilepsia, tiene algun tumor o tiene absesos cerebrales?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if message == QMessageBox.Yes:
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")

        else:
            message = QMessageBox.question(self, "Pregunta FE", "El paciente padece de diabetes, problemas cardiovasculares, obesidad, riesgo de VIH o hipertension?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if message == QMessageBox.Yes:
                QMessageBox.about(self, "Resultado", "Trate primero estas enfermedades y si las alucinaciones o delirios continuan despues de un mes, vuelva a consultar")
            else:
                message = QMessageBox.question(self, "Pregunta FE", "El paciente tiene familiares que hayan padecido o tengan esquizofrenia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if message == QMessageBox.Yes:
                    fam[0] = 1
                    #/////////////////Factores Negativos////////////////
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene aplanamiento afectivo?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        apla[0] = 1
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene alogia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        alo[0] = 1
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene abulia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        abu[0] = 1
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene deficit de atencion?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        def_ate[0] = 1
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene apatia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        apat[0] = 1
                    message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene mas de seis meses con estos sintomas?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        time_neg[0] = 1
                    #///////////////////////////////////////////////////
                else:
                    message = QMessageBox.question(self, "Pregunta FE", "El paciente tiene depresion?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        dep[0] = 1
                    message = QMessageBox.question(self, "Pregunta FE", "El paciente es obsesivo compulsivo?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        obs[0] = 1
                    message = QMessageBox.question(self, "Pregunta FE", "El paciente padece ansiedad?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        ans[0] = 1

                    #/////////////Factores Positivos////////////

                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene delirios?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        deli[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene alucinaciones?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        alu[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene lenguaje desorganizado?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        leng_des[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene comportamiento catatonico?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        comp_cat[0] = 1

                    if (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0):
                        #/////////////////Factores Negativos////////////////
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene aplanamiento afectivo?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            apla[0] = 1
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene alogia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            alo[0] = 1
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene abulia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            abu[0] = 1
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene deficit de atencion?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            def_ate[0] = 1
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene apatia?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            apat[0] = 1
                        message = QMessageBox.question(self, "Pregunta FN", "El paciente tiene mas de seis meses con estos sintomas?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            time_neg[0] = 1

                        
                        #///////////////////////////////////////////////////
                    else:
                        message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene mas de un mes con estos sintomas?",
                                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if message == QMessageBox.Yes:
                            time_pos[0] = 1 

        if (time_neg[0] == 0 and apla[0] == 0 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")
            print(total)
        elif (time_neg[0] == 0 and alo[0] == 0 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")
            print(total)
        elif (time_neg[0] == 0 and abu[0] == 0 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")
            print(total)
        elif (time_neg[0] == 0 and def_ate[0] == 0 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")
            print(total)
        elif (time_neg[0] == 0 and apat[0] == 0 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente no tiene esquizofrenia")
            print(total)

        elif (time_neg[0] == 0 and alo[0] == 1 and abu[0] == 1 and apat[0] == 1 and apla[0] == 1 and def_ate[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            message = QMessageBox.question(self, "Pregunta RMG", "El paciente tiene reduccion de materia gris?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if message == QMessageBox.Yes:
                if deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0:
                     QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
                     print("1")
                else:
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene delirios?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        deli[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene alucinaciones?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        alu[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene lenguaje desorganizado?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        leng_des[0] = 1
                    message = QMessageBox.question(self, "Pregunta FP", "El paciente tiene comportamiento catatonico?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if message == QMessageBox.Yes:
                        comp_cat[0] = 1

                    if deli[0] == 1 or alu[0] == 1 or leng_des[0] == 1 or comp_cat[0] == 1:
                        QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa psicotica")
                        print("1")
                    else:
                        QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
                        print("1")

        elif (time_neg[0] == 1 and apla[0] == 1 and abu[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)
        elif (time_neg[0] == 1 and apla[0] == 1 and def_ate[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)
        elif (time_neg[0] == 1 and apla[0] == 1 and apat[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)
        elif (time_neg[0] == 1 and apla[0] == 1 and alo[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)
        elif (time_neg[0] == 1 and apat[0] == 1 and abu[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)
        elif (time_neg[0] == 1 and alo[0] == 1 and abu[0] == 1 and (deli[0] == 0 and alu[0] == 0 and leng_des[0] == 0 and comp_cat[0] == 0)):
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica")
            total = max(apla[1], alo[1], abu[1], def_ate[1], apat[1]) + time_neg[1]
            print(total)

        elif (time_pos[0] == 1 and (deli[0] == 1 or alu[0]==1 or leng_des[0] == 1 or comp_cat[0] == 1)):
            total = max(deli[1], alu[1], leng_des[1], comp_cat[1]) + time_pos[1]
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa psicotica" )
            print(total)
        elif (time_pos[0] == 0 and (deli[0] == 1 or alu[0]==1 or leng_des[0] == 1 or comp_cat[0] == 1)):
            total = max(deli[1], alu[1], leng_des[1], comp_cat[1]) - time_pos[1]
            QMessageBox.about(self, "Resultado", "El paciente tiene esquizofrenia en la etapa prodromica" )
            print(total)
                    
total = 0
fam = [0, 0.1] #Familiares que la padecen
dep = [0, 0.2] #Tiene depresion
obs = [0, 0.2] #Es obsesivo compulsivo
ans = [0, 0.2] #Tiene ansiedad

deli = [0, 0.6] #Delirios
alu = [0, 0.6] #Alucinaciones
leng_des = [0, 0.4] #Lenguaje desorganizado
comp_cat = [0, 0.4] #Comportamiento catatonico
time_pos = [0, 0.2] #0 es menos a 31 dias y 1 mayor

apla = [0, 0.2] #Aplanamiento afectivo
alo = [0, 0.2] #Alogia
abu = [0, 0.2] #Abulia
def_ate = [0, 0.2] #Deficit de atencion
apat = [0, 0.2] #Apatia
time_neg = [0, 0.2] #0 es menos a 31 dias y 1 mayor

red_mat = 0
    
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
