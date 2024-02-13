import sys

from qtpy.QtCore import QObject
from qtpy.QtWidgets import QMessageBox

from .messaging import catch_exception


class QAboutDialog(QObject):
    def __init__(self, parent, appcontext):
        super().__init__()
        self.appcontext = appcontext
        self._parent = parent

    @catch_exception("Failed to show about dialog")
    def show(self):
        """Build and show the about window"""
        version = self.appcontext.build_settings["full_version"]
        author = self.appcontext.build_settings["author"]
        environment = self.appcontext.build_settings["environment"]
        copyright = self.appcontext.build_settings["copyright"]
        app_name = self.appcontext.build_settings["app_name"]

        text = f"""<center>
                    <h1>{app_name}</h1>
                    </center>
                    <p>Version: {version}<br/>
                    Author: {author}<br/>
                    Enviroment: {environment}<br/>
                    Copyright &copy; {copyright}<br/>
                    Python: {sys.version}</p>
                    """

        QMessageBox.about(self._parent, "About", text)
