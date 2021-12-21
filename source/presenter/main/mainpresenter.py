"""
Copyright (C) 2021 Oscar Franzén <oscarfranzen@protonmail.com>

This file is part of PySide6 Simple Example Project.

PySide6 Simple Example Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySide6 Simple Example Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySide6 Simple Example Project.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
import random

from PySide6 import QtCore, QtGui, QtWidgets

logger = logging.getLogger(__name__)

class MainPresenter(QtCore.QObject):
    """
        The Presenter object contains the intelligence of the GUI. That is, here
        resides the interactions between the widgets in the View object. The Presenter
        acts upon signals sent from both the View and the Model.

        The Presenter object has access to both the View and Model objects, so its
        actions takes the form of method calls to these.
    """

    update_calendar = QtCore.Signal(list)

    def __init__(self, model, view, app):
        super(MainPresenter, self).__init__()

        # Store view, model and app.
        self.model = model
        self.view = view
        self.app = app

        self.view.mainwindow.PS871_Button.setChecked(True) 
        self.view.mainwindow.Stallbar_Button.pressed.connect(self.stallbarPressed)
        self.view.mainwindow.dial.setEnabled(False)

        self.connectSignals()

        self.view.mainwindow.show()     # The mainwindow is not visible on the screen until this command.



    def connectSignals(self):
        """
            Here we connect the signals from the MainWindow object to methods in the
            MainPresenter object.
        """
        
        self.view.mainwindow.PS871_Button.pressed.connect(self.PS871Pressed)
        self.view.mainwindow.Stallbar_Button.pressed.connect(self.stallbarPressed)
        self.view.mainwindow.Slump_Button.pressed.connect(self.slumpGenPressed)

        self.view.mainwindow.dial.valueChanged.connect(self.model.send)    # connector to View Dial value change


    def quit(self):
        """
            This method should always be called when exiting the app. If data needs
            to be saved, or the user needs to be asked for some action prior to exiting,
            here is where it should happen.
        """
        pass
        

    def prf(self, prf):
        #This method gets called when a new prf is received on the udp socket in 
        # the model object.
        if(prf==0):
            self.view.mainwindow.LED.setStyleSheet('border: 0px solid black;  background-color : red')
            self.view.mainwindow.LED.setText('STOP')
        else:
            self.view.mainwindow.LED.setStyleSheet('border: 0px solid black;  background-color : green')
            self.view.mainwindow.LED.setText('RUNNING')
            self.view.mainwindow.lcdNumber.display(prf)
        

    def noAnswer(self):
        # This method is called when, after a new prf i sent to the arduino, an answer
        # is not received within 1s.
        print('Inget Svar')
        self.view.mainwindow.LED.setStyleSheet('border-style: outset; border-width: 0px; border-radius: 10px;  padding: 2px; background-color : yellow')
        self.view.mainwindow.LED.setText('COM')
    

    def PS871Pressed(self):
        self.view.mainwindow.Stallbar_Button.setChecked(False)
        self.view.mainwindow.Slump_Button.setChecked(False) 
        self.view.mainwindow.dial.setEnabled(False) 
        self.model.send(750)      

    def stallbarPressed(self):
        self.view.mainwindow.PS871_Button.setChecked(False)
        self.view.mainwindow.Slump_Button.setChecked(False)
        #self.view.mainwindow.dial.setValue(500)
        self.model.send(self.view.mainwindow.dial.value())
        self.view.mainwindow.dial.setEnabled(True)
        

    def slumpGenPressed(self):
        # Dostuff
        self.view.mainwindow.PS871_Button.setChecked(False)
        self.view.mainwindow.Stallbar_Button.setChecked(False)
        self.view.mainwindow.dial.setEnabled(False)
        random_int = random.randint(500, 1000)
        self.model.send(random_int)
        print('Slumpgenererad prf: %d' % random_int )
        