from PySide6 import QtWidgets
from ui.calculator import Ui_Form

from a_login_form import Window as LoginWidget
from b_ship_parameters import Window as ShipParametersWidget
from c_engine_settings import Window as EngineSettingsWidget
from d_profile_card import Window as ProfileCardWidget

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.LoginWidget = LoginWidget()
        self.ShipParametersWidget = ShipParametersWidget()
        self.EngineSettingsWidget = EngineSettingsWidget()
        self.ProfileCardWidget = ProfileCardWidget()

        l_left = QtWidgets.QVBoxLayout()
        l_left.addWidget(self.LoginWidget)
        l_left.addWidget(self.ProfileCardWidget)
        l_left.addWidget(self.ShipParametersWidget)

        l_main = QtWidgets.QHBoxLayout()
        l_main.addLayout(l_left)
        l_main.addWidget(self.EngineSettingsWidget)

        self.setLayout(l_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
