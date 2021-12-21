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

from PySide6 import QtCore, QtNetwork

logger = logging.getLogger(__name__)

class MyModel(QtCore.QObject):
    """
        This is where the abstract model lives. This could be a database with some added
        functionality, or a physics engine which continually calculates the positions of the
        bodies in a planetary system. This is the core of the app if you will, what the app
        is about. Making visual sense of the abstract data in the Model is the job of
        the View and Presenter. 
    """


    answer_timeout = QtCore.Signal() # connector to presenter
    received_prf = QtCore.Signal(int) # connector to presenter


    def __init__(self):
        super(MyModel, self).__init__()

        # Using pyside implementation of udp socket instead...
        self.address = QtNetwork.QHostAddress('169.254.37.4')
        self.port = 5000

        self.udp_socket = QtNetwork.QUdpSocket()
        self.udp_socket.bind(self.port)
        self.udp_socket.readyRead.connect(self.onReceive) # when incoming data call the function 
       
        self.send_time = None

        #self.send('Jesus Lever!')


    def send(self, prf):      # Function for sending the PRF to Arduino 
        self.udp_socket.writeDatagram(str(prf).encode(), self.address, self.port)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000) # Set timer 1000ms
        self.timer.start()
        self.timer.timeout.connect(self.timeout)
        
        
        

    def timeout(self): 
        self.timer.stop()
        print('Fick inget svar inom 1000ms....')
        self.answer_timeout.emit() # sending signal via connector


    def onReceive(self):
        self.timer.stop()
        while (self.udp_socket.hasPendingDatagrams()):
            datagram, address, port = self.udp_socket.receiveDatagram()
            prf = int(datagram.decode())
            print('Tog emot prf: %d' % prf)
            self.received_prf.emit(prf) # sending signal via connector
                
    
    def quit(self):
        """
            This method gets called before the app exits, to give us a chance to exit cleanly
            if this is deemed necessary.
        """
        pass    # Here, nothing needs to be saved or dealt with before exit, so we just
                # pass on the opportunity


