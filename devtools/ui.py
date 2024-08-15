from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Welcome to Devtools', font_size=30))
        self.add_widget(Label(text='Select an option to get started', font_size=20))
        start_button = Button(text='Start New Project')
        start_button.bind(on_press=self.dispatch_start_project)
        self.add_widget(start_button)
        settings_button = Button(text='Open Settings')
        settings_button.bind(on_press=self.dispatch_open_settings)
        self.add_widget(settings_button)

    def dispatch_start_project(self, instance):
        self.dispatch('on_start_project')

    def dispatch_open_settings(self, instance):
        self.dispatch('on_open_settings')

    def on_start_project(self, *args):
        pass

    def on_open_settings(self, *args):
        pass

class EditorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(EditorScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.editor = TextInput(multiline=True)
        self.add_widget(self.editor)
        run_button = Button(text='Run Code')
        run_button.bind(on_press=self.dispatch_run_code)
        self.add_widget(run_button)
        shell_input = TextInput(hint_text='Enter shell command')
        shell_input.bind(on_text_validate=self.dispatch_run_shell)
        self.add_widget(shell_input)
        save_button = Button(text='Save Project')
        save_button.bind(on_press=self.dispatch_save_project)
        self.add_widget(save_button)
        load_button = Button(text='Load Project')
        load_button.bind(on_press=self.dispatch_load_project)
        self.add_widget(load_button)

    def dispatch_run_code(self, instance):
        self.dispatch('on_run_code')

    def dispatch_run_shell(self, instance):
        self.dispatch('on_run_shell', instance.text)

    def dispatch_save_project(self, instance):
        self.dispatch('on_save_project')

    def dispatch_load_project(self, instance):
        self.dispatch('on_load_project')

    def on_run_code(self, *args):
        pass

    def on_run_shell(self, *args):
        pass

    def on_save_project(self, *args):
        pass

    def on_load_project(self, *args):
        pass
