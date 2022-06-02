from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton

from package.api.level_game import Medium, Easy


class GameInterface(QWidget):
    def __init__(self, level_indice):
        super().__init__()
        self.level_indice = level_indice
        if self.level_indice == 'easy':
            self.level_tool = Easy()
        if self.level_indice == 'medium':
            self.level_tool = Medium()
        print(self.level_tool.the_number)

        self.interface = QVBoxLayout(self)
        self.interface.setContentsMargins(120, 75, 120, 150)
        self.info_box = QHBoxLayout()

        self.level = QLabel(f"Niveau {self.level_indice}")
        self.level.setAlignment(Qt.AlignHCenter)
        self.level.setFont(QFont("Arial", 14))

        self.quiz = QLabel(f"Quel est le nombre mystere ??? Interval [{self.level_tool.interval.get('start')},"
                           f"{self.level_tool.interval.get('end')}]")
        self.quiz.setAlignment(Qt.AlignCenter)

        self.info = QLineEdit("-- Appuyez Entrée pour valider")
        self.info.setContentsMargins(0, 10, 0, 10)
        self.info.setAlignment(Qt.AlignCenter)
        self.info.setEnabled(False)

        self.level_tool.number_essai -= 1
        self.info_chrono = QLabel(f"Essai restant : {self.level_tool.number_essai}")

        self.answer = QLineEdit()
        self.answer.setPlaceholderText("Nombre mystere")

        self.info_box.addWidget(self.info)
        self.info_box.addWidget(self.info_chrono)

        self.reload = QPushButton("Recommencer")
        self.reload.hide()

        self.interface.addWidget(self.level)
        self.interface.addWidget(self.quiz)
        self.interface.addLayout(self.info_box)
        self.interface.addWidget(self.answer)
        self.interface.addWidget(self.reload)

        self.answer.returnPressed.connect(self.verify)
        self.reload.clicked.connect(self.reload_page)

    def verify(self):
        try:
            if self.level_tool.number_essai == 0:
                self.info.setText("GAME OVER")
                self.answer.setEnabled(False)
                self.reload.show()
            else:
                print(self.answer.text(), self.level_tool.the_number)
                if self.level_tool.the_number == int(self.answer.text()):
                    self.info.setText("Good Game !!! Bien joué")
                    self.info.setStyleSheet("color: MediumSeaGreen;")
                    self.answer.setEnabled(False)
                    self.answer.setText(str(self.level_tool.the_number))
                elif self.level_tool.the_number <= int(self.answer.text()):
                    self.level_tool.number_essai -= 1
                    self.info_chrono.setText(f"Essai restant : {self.level_tool.number_essai}")
                    self.info.setText("-- Le nombre entrer est superieur")
                    self.info.setStyleSheet("color: Tomato;")
                    self.answer.clear()
                else:
                    self.level_tool.number_essai -= 1
                    self.info_chrono.setText(f"Essai restant : {self.level_tool.number_essai}")
                    self.info.setText("-- Le nombre entree est inferieur")
                    self.info.setStyleSheet("color: Tomato;")
                    self.answer.clear()

        except:
            self.info.setText("Entrer incorrect. Veuillez saisir un nombre.")
            self.info.setStyleSheet("color: Tomato;")

    def reload_page(self):
        print(self.level)
        if self.level_indice == 'easy':
            self.level_tool = Easy()
            self.info.setText("-- Appuyez Entrée pour valider")
            self.level_tool.number_essai -= 1
            self.info_chrono.setText(f"Essai restant : {self.level_tool.number_essai}")
            self.info.setStyleSheet("color: Gray;")
            self.answer.clear()
        if self.level_indice == 'medium':
            self.level_tool = Medium()
            self.info.setText("-- Appuyez Entrée pour valider")
            self.info.setStyleSheet("color: Gray;")
            self.level_tool.number_essai -= 1
            self.info_chrono.setText(f"Essai restant : {self.level_tool.number_essai}")
            self.answer.clear()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_menu()
        self.modify_style()
        self.setCentralWidget(GameInterface("easy"))

    def create_menu(self):
        self.main_menu = self.menuBar()
        self.menu_level = self.main_menu.addMenu("Niveau")

        self.easy = self.menu_level.addAction("Facile")
        self.medium = self.menu_level.addAction("Normal")

        self.help = self.main_menu.addAction("Aide")
        self.quit = self.main_menu.addAction("Quitter")

        self.easy.triggered.connect(self.show_easy)
        self.medium.triggered.connect(self.show_medium)

        self.help.triggered.connect(self.show_help)
        self.quit.triggered.connect(self.close)

    def modify_style(self):
        pass

    def show_help(self):
        self.setCentralWidget(QLabel("Hello"))

    def show_easy(self):
        self.setCentralWidget(GameInterface("easy"))

    def show_medium(self):
        self.setCentralWidget(GameInterface("medium"))
