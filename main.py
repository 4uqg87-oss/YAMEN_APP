from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.025, 0.015, 0.03, 1)

class YamenApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="[color=ff3030]البقاء للأقوى YAMEN[/color]",
            markup=True,
            font_size=28,
            size_hint_y=None,
            height=80
        )

        subtitle = Label(
            text="CYBER • FREE FIRE REPORT CENTER",
            color=(0.8, 0.2, 0.2, 1),
            size_hint_y=None,
            height=40
        )

        self.player_id = TextInput(
            hint_text="أدخل ID اللاعب",
            multiline=False,
            size_hint_y=None,
            height=55
        )

        self.details = TextInput(
            hint_text="اكتب تفاصيل الإساءة أو المشكلة",
            multiline=True
        )

        report_button = Button(
            text="حفظ البلاغ",
            size_hint_y=None,
            height=55
        )
        report_button.bind(on_press=self.save_report)

        self.status = Label(
            text="جاهز لاستقبال البلاغات"
        )

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(self.player_id)
        layout.add_widget(self.details)
        layout.add_widget(report_button)
        layout.add_widget(self.status)

        return layout

    def save_report(self, instance):
        player_id = self.player_id.text.strip()
        details = self.details.text.strip()

        if not player_id or not details:
            self.status.text = "يرجى إدخال ID والتفاصيل"
            return

        with open("reports.txt", "a", encoding="utf-8") as file:
            file.write(
                f"ID: {player_id}\nDetails: {details}\n---\n"
            )

        self.status.text = "تم حفظ البلاغ على الجهاز"
        self.player_id.text = ""
        self.details.text = ""

YamenApp().run()
