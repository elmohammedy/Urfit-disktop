import  sys
from  PyQt5.QtWidgets import QApplication, QWidget

a= QApplication(sys.argv)
root= QWidget()
root.show()
sys.exit(a.exec_())