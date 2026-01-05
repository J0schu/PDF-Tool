from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)


class PageSelector(QWidget):

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(6, 4, 6, 4)

        self.label = QLabel(file_path)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

        row = QHBoxLayout()

        self.rb_all = QRadioButton("All")
        self.rb_custom = QRadioButton("Custom")
        self.rb_all.setChecked(True)

        self.custom_edit = QLineEdit()
        self.custom_edit.setPlaceholderText("1-3,5")
        self.custom_edit.setEnabled(False)
        self.custom_edit.setFixedWidth(90)

        self.rb_custom.toggled.connect(self.custom_edit.setEnabled)

        row.addWidget(self.rb_all)
        row.addWidget(self.rb_custom)
        row.addWidget(self.custom_edit)
        row.addStretch()

        layout.addLayout(row)

    # -------- API --------

    def get_mode(self) -> str:
        return "custom" if self.rb_custom.isChecked() else "all"

    def get_custom_text(self) -> str:
        return self.custom_edit.text()
