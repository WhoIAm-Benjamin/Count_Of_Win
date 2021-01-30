""" Program, which count of win and write them on screen """

import sys
from time import sleep
# import keyboard

import design
import design_players
import end_winner_design
from PySide2 import QtWidgets  # , QtCore, QtGui


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    """ Class of MainWindow
    :param QtWidgets.QMainWindow: Main window widget;
    :param design.Ui_MainWindow: design for that;
    """
    player1_scope = 0
    player2_scope = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.win1_button.clicked.connect(self.winner1)
        self.win2_button.clicked.connect(self.winner2)
        self.exit_btn.clicked.connect(self.sleeping)

    def naming(self, player1, player2):
        """ Change names of players
        :param self: object of app;
        :param player1: name of player #1;
        :param player2: name of player #2
        """
        self.name1.setVisible(True)
        self.name2.setVisible(True)
        self.name1.setText(player1)
        self.name2.setText(player2)

    def winner1(self):
        """ +1 point for first player
        :param self: object of app;
        """
        self.player1_scope += 1
        if len(str(self.player1_scope)) < 10:
            self.win1.setText(str(self.player1_scope))
        else:
            self.win1.setText(str(self.player1_scope)[1:])

    def winner2(self):
        """ +1 point for second player
        :param self: object of app;
        """
        self.player2_scope += 1
        if len(str(self.player2_scope)) < 10:
            self.win2.setText(str(self.player2_scope))
        else:
            self.win2.setText(str(self.player2_scope)[1:])

    def sleeping(self):
        print('CLASS')
        winners.show()
        winners.win_def()
        try:
            self.destroy()
        except NameError:
            pass
        # sleep(7)
        winners.destroy()


# noinspection PyUnresolvedReferences
class FirstApp(QtWidgets.QWidget, design_players.Ui_Players):
    """ Class of First App
    :param QtWidgets.QWidget: Widget of app;
    :param design_players.Ui_Players: design for that;
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.compile_names_button.clicked.connect(self.compile)

    def compile(self):
        """ Definition for compile names of players and translated them for MainWindow
        :param self: object of app;
        :return: names;
        """
        player1 = self.player1_name.displayText().capitalize()
        player2 = self.player2_name.displayText().capitalize()
        MainApp.naming(my_MainWindow, player1, player2)
        players.destroy()


# noinspection PyUnresolvedReferences
class AppWin(QtWidgets.QWidget, end_winner_design.Ui_end_winner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def win_def(self):
        point1 = MainApp.player1_scope
        point2 = MainApp.player2_scope
        if point1 > point2:
            self.end_of_win.setText(MainApp.name1)
        elif point2 > point1:
            self.end_of_win.setText(MainApp.name2)
        else:
            self.end_of_win.setText('Дружба')



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    winners = AppWin()
    my_MainWindow = MainApp()
    my_MainWindow.show()
    players = FirstApp()
    players.show()
    sys.exit(app.exec_())
