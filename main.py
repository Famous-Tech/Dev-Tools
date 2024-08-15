from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import subprocess
from android import Intent

class DevtoolsApp(App):
    def build(self):
        # ...

    def update_syntax_highlighting(self, instance, text):
        # ...

    def run_code(self, instance):
        code = self.editor.text
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())

    def share_project(self, instance):
        code = self.editor.text
        intent = Intent(Intent.ACTION_SEND)
        intent.setType('text/plain')
        intent.putExtra(Intent.EXTRA_TEXT, code)
        self.ctx.startActivity(Intent.createChooser(intent, 'Share Project'))

    def run_shell_command(self, instance, text):
        # ...

