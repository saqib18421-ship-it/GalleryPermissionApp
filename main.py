from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform


class GalleryPermissionApp(App):

    def build(self):

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.status = Label(
            text="GALLERY ACCESS REQUIRED",
            font_size=22
        )

        layout.add_widget(self.status)

        self.btn = Button(
            text="REQUEST PERMISSION",
            size_hint=(1, 0.2)
        )

        self.btn.bind(
            on_press=self.request_access
        )

        layout.add_widget(self.btn)

        return layout

    def request_access(self, instance):

        if platform == "android":

            from android.permissions import request_permissions
            from jnius import autoclass

            Version = autoclass("android.os.Build$VERSION")
            sdk = Version.SDK_INT

            if sdk >= 33:
                permissions = [
                    "android.permission.READ_MEDIA_IMAGES",
                    "android.permission.READ_MEDIA_VIDEO"
                ]
            else:
                permissions = [
                    "android.permission.READ_EXTERNAL_STORAGE"
                ]

            request_permissions(
                permissions,
                self.permission_result
            )

        else:
            self.status.text = "RUN ON ANDROID"

    def permission_result(self, permissions, grants):

        if all(grants):
            self.status.text = "ACCESS GRANTED\nPermission Active"
        else:
            self.status.text = "PERMISSION DENIED"


GalleryPermissionApp().run()

