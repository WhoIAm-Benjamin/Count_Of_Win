""" Программа, которая подсчитает победы и выведет их на экран """

import sys
import design, design_players
# import keyboard
# noinspection PyUnresolvedReferences
from PySide2 import QtWidgets, QtCore, QtGui

player1 = ''
player2 = ''

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    global player1, player2
    player1_scope = 0
    player2_scope = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win1_button.clicked.connect(self.winner1)
        self.win2_button.clicked.connect(self.winner2)

    def naming(self):
        self.name1.setVisible(True)
        self.name2.setVisible(True)
        self.name1.setText(player1)
        self.name2.setText(player2)

    def winner1(self):
        self.player1_scope += 1
        if len(str(self.player1_scope)) < 10:
            self.win1.setText(str(self.player1_scope))
        else:
            self.win1.setText(str(self.player1_scope)[1:])

    def winner2(self):
        self.player2_scope += 1
        if len(str(self.player2_scope)) < 10:
            self.win2.setText(str(self.player2_scope))
        else:
            self.win2.setText(str(self.player2_scope)[1:])


class App1(QtWidgets.QMainWindow, design_players.Ui_Players):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.compile_names_button.clicked.connect(self.compile)

    # def keyPressEvent(self, event):
    #     print(event.__eq__)
    #     if event == 'alt':
    #          print('SUPER')

    def compile(self):
        global player1, player2
        player1 = self.player1_name.displayText().capitalize()
        player2 = self.player2_name.displayText().capitalize()
        App.naming(my_MainWindow)
        players.destroy()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    my_MainWindow = App()
    my_MainWindow.show()
    players = App1()
    players.show()
    sys.exit(app.exec_())
