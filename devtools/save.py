import json
import os
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def save_project(project_name, code):
    data = load_projects()
    project = {
        "name": project_name,
        "code": code
    }
    data["projects"].append(project)
    save_projects(data)

def save_projects(data):
    if not os.path.exists('data'):
        os.makedirs('data')
    with open('data/projects.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_projects():
    try:
        with open('data/projects.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"projects": []}

def save_project_to_external(project_name, code):
    def save_file(path):
        with open(os.path.join(path, f'{project_name}.txt'), 'w') as file:
            file.write(code)
        popup.dismiss()

    def on_submit(instance, path):
        save_file(path)

    def on_create_new(instance):
        new_folder_popup = NewFolderPopup(save_file)
        new_folder_popup.open()

    file_chooser = FileChooserIconView()
    file_chooser.bind(on_submit=on_submit)
    create_new_button = Button(text='Create New Folder')
    create_new_button.bind(on_press=on_create_new)
    content = BoxLayout(orientation='vertical')
    content.add_widget(file_chooser)
    content.add_widget(create_new_button)
    popup = Popup(title='Select Folder', content=content, size_hint=(0.9, 0.9))
    popup.open()

class NewFolderPopup(Popup):
    def __init__(self, save_callback, **kwargs):
        super(NewFolderPopup, self).__init__(**kwargs)
        self.save_callback = save_callback
        self.title = 'Create New Folder'
        content = BoxLayout(orientation='vertical')
        self.folder_name = TextInput(hint_text='Folder Name')
        content.add_widget(self.folder_name)
        create_button = Button(text='Create')
        create_button.bind(on_press=self.create_folder)
        content.add_widget(create_button)
        self.add_widget(content)

    def create_folder(self, instance):
        folder_name = self.folder_name.text
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        self.save_callback(folder_name)
        self.dismiss()
