import os
import sys

from PySide6.QtCore import QDate, QDir, Qt, QUrl, Slot, Signal
from PySide6.QtGui import QAction, QGuiApplication, QDesktopServices, QIcon, QImage, QPixmap
from PySide6.QtMultimedia import (QCamera, QImageCapture,
                                  QMediaCaptureSession,
                                  QMediaDevices)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QTabWidget, QToolBar, QVBoxLayout, QWidget)

from notification import NotificationWindow

class ImageView(QWidget):
    save_signal = Signal(QPixmap, str)

    def __init__(self, previewImage=None, fileName=None):
        super().__init__()

        self._file_name = fileName
        try:
            self.pixmap = QPixmap.fromImage(previewImage)
            self._image_label = QLabel()
            self._image_label.setPixmap(self.pixmap)
            main_layout = QVBoxLayout(self)
            main_layout.addWidget(self._image_label)

            top_layout = QHBoxLayout()
            self._file_name_label = QLabel(QDir.toNativeSeparators(fileName))
            self._file_name_label.setTextInteractionFlags(Qt.TextBrowserInteraction)

            top_layout.addWidget(self._file_name_label)
            top_layout.addStretch()
            # 路径button
            copy_button = QPushButton("复制路径")
            copy_button.setFixedSize(100, 35)
            copy_button.setToolTip("复制图片路径到剪贴板")
            top_layout.addWidget(copy_button)
            copy_button.clicked.connect(self.copy)
            # 打开button
            launch_button = QPushButton("打开图片")
            launch_button.setFixedSize(100, 35)
            top_layout.addWidget(launch_button)
            launch_button.clicked.connect(self.launch)
            # 传递button
            pass_button = QPushButton("完成拍摄")
            pass_button.setFixedSize(100, 35)
            top_layout.addWidget(pass_button)
            pass_button.clicked.connect(self.emitImage)
            main_layout.addLayout(top_layout)
        except Exception as e:
            pass

    @Slot(QPixmap, str)
    def emitImage(self):
        print("emit_image")
        self.save_signal[QPixmap, str].emit(self.pixmap, self._file_name)

    @Slot()
    def copy(self):
        NotificationWindow.success(self, "成功", "已复制到剪贴板", time=2000)
        QGuiApplication.clipboard().setText(self._file_name_label.text())

    @Slot()
    def launch(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self._file_name))


class camera_window(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.main_win = parent
        self._capture_session = None
        self._camera = None
        self._camera_info = None
        self._image_capture = None
        self.setStyleSheet(parent.styleSheet())
        available_cameras = QMediaDevices.videoInputs()
        self.setWindowIcon(QIcon(u"./images/摄像头.png"))
        if available_cameras:
            self._camera_info = available_cameras[0]
            self._camera = QCamera(self._camera_info)
            self._camera.errorOccurred.connect(self._camera_error)
            self._image_capture = QImageCapture(self._camera)
            self._image_capture.imageCaptured.connect(self.image_captured)
            self._image_capture.imageSaved.connect(self.image_saved)
            self._image_capture.errorOccurred.connect(self._capture_error)
            self._capture_session = QMediaCaptureSession()
            self._capture_session.setCamera(self._camera)
            self._capture_session.setImageCapture(self._image_capture)

        self._current_preview = QImage()
        tool_bar = QToolBar()
        tool_bar.setMovable(False)
        self.addToolBar(tool_bar)
        self._take_picture_action = QAction(QIcon(u"./images/摄像头.png"), "&Take Picture", self,
                                            shortcut="Ctrl+T",
                                            triggered=self.take_picture)
        self._take_picture_action.setToolTip("打开摄像头 (Ctrl+T)")
        self._open_folder_action = QAction(QIcon(u"./images/打开文件夹.png"), "&Open Folder", self,
                                           shortcut="Ctrl+O",
                                           triggered=self._openFolder)
        self._open_folder_action.setToolTip("打开文件夹 (Ctrl+O)")
        self._clear_folder_buffer = QAction(QIcon(u"./images/删除.png"), "&Delete photos", self,
                                            shortcut="Delete",
                                            triggered=self._deleteFolder)
        self._clear_folder_buffer.setToolTip("清除本地拍摄图片 (Delete)")
        tool_bar.addActions([self._take_picture_action, self._open_folder_action, self._clear_folder_buffer])
        self._tab_widget = QTabWidget()
        self.setCentralWidget(self._tab_widget)

        self._camera_viewfinder = QVideoWidget()
        self._tab_widget.addTab(self._camera_viewfinder, "画面捕捉")

        if self._camera and self._camera.error() == QCamera.NoError:
            name = self._camera_info.description()
            self.setWindowTitle(f"摄像头 (当前设备：{name})")
            self.show_status_message(f"启动: '{name}'")
            self._capture_session.setVideoOutput(self._camera_viewfinder)
            self._take_picture_action.setEnabled(self._image_capture.isReadyForCapture())
            self._image_capture.readyForCaptureChanged.connect(self._take_picture_action.setEnabled)
            self._camera.start()
        else:
            self.setWindowTitle("摄像头")
            self._take_picture_action.setEnabled(False)
            self.show_status_message("摄像头不可用")

    def _openFolder(self):
        try:
            os.startfile(f"{os.path.split(sys.argv[0])[0]}/photos")
        except FileNotFoundError as e:
            os.makedirs(f"{os.path.split(sys.argv[0])[0]}/photos")
            os.startfile(f"{os.path.split(sys.argv[0])[0]}/photos")

    def _deleteFolder(self):
        try:
            os.remove(f"{os.path.split(sys.argv[0])[0]}/photos")
        except PermissionError as e:
            NotificationWindow.error(self, "错误", f"<font color=red>{e}<请手动删除></font>", time=10000,
                                     callback=os.startfile(f"{os.path.split(sys.argv[0])[0]}/photos"))

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    def closeEvent(self, event):
        if self._camera and self._camera.isActive():
            self._camera.stop()
        event.accept()

    def next_image_file_name(self):
        date_string = QDate.currentDate().toString("yyyyMMdd")
        pattern = f"{os.path.split(sys.argv[0])[0]}/photos/camera_{date_string}_{{:03d}}.jpg"
        try:
            os.makedirs(os.path.split(pattern)[0])
        except:
            pass
        n = 1
        while True:
            result = pattern.format(n)
            if not os.path.exists(result):
                print(result)
                return result
            n = n + 1
        return None

    @Slot()
    def take_picture(self):
        self._current_preview = QImage()
        self._image_capture.captureToFile(self.next_image_file_name())

    @Slot(int, QImage)
    def image_captured(self, id, previewImage):
        self._current_preview = previewImage

    @Slot(int, str)
    def image_saved(self, id, fileName):
        index = self._tab_widget.count()
        self.image_view = ImageView(self._current_preview, fileName)
        self.image_view.save_signal[QPixmap, str].connect(self.main_win._passImageFromCamera)
        self._tab_widget.addTab(self.image_view, f"图像 #{index}")
        self._tab_widget.setCurrentIndex(index)

    @Slot(int, QImageCapture.Error, str)
    def _capture_error(self, id, error, error_string):
        print(error_string, file=sys.stderr)
        NotificationWindow.error(self, "错误", error_string)
        self.show_status_message(error_string)

    @Slot(QCamera.Error, str)
    def _camera_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        NotificationWindow.error(self, "错误", error_string)
        self.show_status_message(error_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = camera_window()
    available_geometry = main_win.screen().availableGeometry()
    main_win.resize(available_geometry.width() / 3, available_geometry.height() / 2)
    main_win.show()
    sys.exit(app.exec())
