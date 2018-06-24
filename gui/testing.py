from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,QTextEdit,QWidget,QPushButton

text = "In this text I want tt this word and only this word."

class MyHighlighter(QTextEdit):
    def __init__(self, text, patterns, parent=None):
        super(MyHighlighter, self).__init__(parent)
        # Setup the text editor
        self.setText(text)
        self.setGeometry(350, 100, 500, 600)
        # self.move(120,40)
        cursor = self.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        # Setup the regex engine
        for pattern in patterns:
            regex = QtCore.QRegExp(pattern)
            # Process the displayed document
            pos = 0
            index = regex.indexIn(self.toPlainText(), pos)
            while (index != -1):
                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
                cursor.mergeCharFormat(format)
                # Move to the next match
                pos = index + regex.matchedLength()
                index = regex.indexIn(self.toPlainText(), pos)



