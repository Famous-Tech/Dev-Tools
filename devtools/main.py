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
from devtools.save import save_project, save_project_to_external
from devtools.load import load_projects, load_project_from_external

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
        self.editor_screen.bind(on_save_project=self.save_current_project)
        self.editor_screen.bind(on_load_project=self.load_project)
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
        save_popup = SavePopup(self.editor_screen.editor.text)
        save_popup.open()

    def load_project(self, instance):
        load_popup = LoadPopup()
        load_popup.open()

class SavePopup(Popup):
    def __init__(self, code, **kwargs):
        super(SavePopup, self).__init__(**kwargs)
        self.code = code
        self.title = 'Save Project'
        content = BoxLayout(orientation='vertical')
        self.project_name = TextInput(hint_text='Project Name')
        content.add_widget(self.project_name)
        self.save_internal_button = Button(text='Save to Internal Storage')
        self.save_internal_button.bind(on_press=self.save_to_internal)
        content.add_widget(self.save_internal_button)
        self.save_external_button = Button(text='Save to External Storage')
        self.save_external_button.bind(on_press=self.save_to_external)
        content.add_widget(self.save_external_button)
        self.add_widget(content)

    def save_to_internal(self, instance):
        project_name = self.project_name.text
        save_project(project_name, self.code)
        self.dismiss()

    def save_to_external(self, instance):
        project_name = self.project_name.text
        save_project_to_external(project_name, self.code)
        self.dismiss()

class LoadPopup(Popup):
    def __init__(self, **kwargs):
        super(LoadPopup, self).__init__(**kwargs)
        self.title = 'Load Project'
        content = BoxLayout(orientation='vertical')
        self.file_chooser = FileChooserIconView()
        self.file_chooser.bind(on_submit=self.load_file)
        content.add_widget(self.file_chooser)
        self.add_widget(content)

    def load_file(self, instance, selection, touch):
        if selection:
            with open(selection[0], 'r') as file:
                code = file.read()
                self.editor_screen.editor.text = code
            self.dismiss()

if __name__ == '__main__':
    DevtoolsApp().run()
