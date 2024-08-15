from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import subprocess
from devtools.ui import HomeScreen, EditorScreen
from devtools.shell import run_shell_command
from devtools.languages import translate_text
from devtools.settings import SettingsPopup
from devtools.save import save_project
from devtools.load import load_projects

class DevtoolsApp(App):
    def build(self):
        self.home_screen = HomeScreen()
        self.home_screen.bind(on_start_project=self.start_project)
        self.home_screen.bind(on_open_settings=self.open_settings)
        return self.home_screen

    def start_project(self, instance):
        self.editor_screen = EditorScreen()
        self.editor_screen.bind(on_run_code=self.run_code)
        self.editor_screen.bind(on_run_shell=self.run_shell_command)
        self.root.clear_widgets()
        self.root.add_widget(self.editor_screen)

    def open_settings(self, instance):
        settings_popup = SettingsPopup()
        settings_popup.open()

    def run_code(self, instance):
        try:
            code = self.editor_screen.editor.text
            process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            if output:
                print(output.decode())
            if error:
                print(error.decode())
        except Exception as e:
            print(f"Error: {e}")

    def run_shell_command(self, instance, command):
        run_shell_command(command)

    def save_current_project(self, instance):
        project_name = "Default Project"  # Vous pouvez ajouter une interface pour que l'utilisateur entre le nom du projet
        code = self.editor_screen.editor.text
        save_project(project_name, code)

    def load_project(self, instance):
        projects = load_projects()
        if projects:
            # Vous pouvez ajouter une interface pour que l'utilisateur choisisse un projet à charger
            first_project = projects["projects"][0]
            self.editor_screen.editor.text = first_project["code"]

if __name__ == '__main__':
    DevtoolsApp().run()
