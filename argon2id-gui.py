#****************************************************************************
# Filename      : argon2id-gui.py
# Created       : Sun Apr 14 2024
# Author        : Zolo
# Github        : https://github.com/zolodev
# Description   : Password hashing using Argon2
#****************************************************************************



import random
import sys

from argon2 import PasswordHasher
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)


class Argon2Hasher(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.passwordInput = QLineEdit()
        self.hashOutput = QLineEdit()
        self.hashOutput.setReadOnly(True)
        self.verifyLabel = QLabel()

        hashButton = QPushButton('Hash Password')
        hashButton.clicked.connect(self.hashPassword)

        verifyButton = QPushButton('Verify Password')
        verifyButton.clicked.connect(self.verifyPassword)

        layout.addWidget(QLabel('Enter Password:'))
        layout.addWidget(self.passwordInput)
        layout.addWidget(hashButton)
        layout.addWidget(QLabel('Hashed Password:'))
        layout.addWidget(self.hashOutput)
        layout.addWidget(verifyButton)
        layout.addWidget(self.verifyLabel)

        self.setLayout(layout)

    def hashPassword(self):
        #ph = PasswordHasher(time_cost=random.randint(2,10))
        ph = PasswordHasher(
            time_cost=random.randint(2,100),  # Number of iterations
            memory_cost=random.randint(512,100000),  # Defines the memory usage
            parallelism=random.randint(2,100),  # Defines the degree of parallelism
            hash_len=random.randint(16,1000),  # Length of the hash in bytes
            salt_len=random.randint(16,512),  # Length of the random salt in bytes
            encoding='utf-8'  # Encoding of the string
        )
        password = self.passwordInput.text()
        hash = ph.hash(password)
        self.hashOutput.setText(hash)

    def verifyPassword(self):
        ph = PasswordHasher()
        password = self.passwordInput.text()
        hash = self.hashOutput.text()

        try:
            ph.verify(hash, password)
            self.verifyLabel.setText("Password is correct!")
        except:
            self.verifyLabel.setText("Password is incorrect!")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    hasher = Argon2Hasher()
    hasher.show()

    sys.exit(app.exec_())
