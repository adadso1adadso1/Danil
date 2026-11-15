from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
import os

Window.clearcolor = (0.1, 0.1, 0.15, 1) # Темный фон

class TaskManager(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        # Файл для сохранения задач
        self.store = JsonStore('tasks.json')

        # Заголовок
        self.add_widget(Label(text="Мои задачи", font_size='24sp', size_hint_y=None, height=50, color=(1,1,1,1)))

        # Поле ввода
        self.input = TextInput(hint_text='Введите задачу...', multiline=False, size_hint_y=None, height=50, font_size='18sp')
        self.add_widget(self.input)

        # Кнопка добавить
        btn_add = Button(text="Добавить", size_hint_y=None, height=50, background_color=(0, 0.7, 0.3, 1))
        btn_add.bind(on_press=self.add_task)
        self.add_widget(btn_add)

        # Скролл для списка задач
        self.scroll = ScrollView()
        self.task_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.task_layout.bind(minimum_height=self.task_layout.setter('height'))
        self.scroll.add_widget(self.task_layout)
        self.add_widget(self.scroll)

        self.load_tasks()

    def add_task(self, instance):
        text = self.input.text.strip()
        if text:
            self.store.put(text, done=False)
            self.input.text = ''
            self.load_tasks()

    def delete_task(self, task_name):
        if self.store.exists(task_name):
            self.store.delete(task_name)
        self.load_tasks()

    def load_tasks(self):
        self.task_layout.clear_widgets()
        # Загружаем задачи в обратном порядке (новые сверху)
        for key in reversed(list(self.store.keys())):
            task_row = BoxLayout(size_hint_y=None, height=50, spacing=5)
            
            lbl = Label(text=key, color=(1,1,1,1), font_size='16sp')
            btn_del = Button(text="X", size_hint_x=None, width=50, background_color=(0.8, 0.2, 0.2, 1))
            btn_del.bind(on_press=lambda x, name=key: self.delete_task(name))
            
            task_row.add_widget(lbl)
            task_row.add_widget(btn_del)
            self.task_layout.add_widget(task_row)

class ManagerApp(App):
    def build(self):
        return TaskManager()

if __name__ == '__main__':
    ManagerApp().run()
