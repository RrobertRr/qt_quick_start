from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView      # Für das Einbinden von view.qml
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("view.qml")

view.setSource(url)
view.show()
app.exec_()