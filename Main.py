from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Line, Rectangle, Ellipse
from kivy.core.window import Window
import math

class LadaRoad(Widget):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.offset = 0
        self.frame = 0
        self.start_time = 0
        Clock.schedule_interval(self.update, 1/30)

    def update(self, dt):
        self.start_time += dt
        self.offset += 5
        self.frame += 1
        self.redraw()

    def redraw(self):
        self.canvas.clear()
        w, h = Window.width, Window.height
        with self.canvas:
            Color(0.1, 0.1, 0.2)
            Rectangle(pos=(0, 0), size=(w, h))
            Color(0.2, 0.2, 0.2)
            Rectangle(pos=(0, 0), size=(w, h / 3))
            Color(0.6, 0.6, 0.6)
            for i in range(-1, int(w/100) + 2):
                x = (i * 100 + self.offset) % (w + 100) - 100
                Rectangle(pos=(x, h/6 - 5), size=(50, 10))
            car_x, car_y = w / 2 - 150, h / 3 - 20
            Color(0.95, 0.95, 0.95) 
            Rectangle(pos=(car_x, car_y), size=(300, 100)) 
            Color(0.8, 0.8, 0.8) 
            Rectangle(pos=(car_x + 60, car_y + 100), size=(180, 60))
            Color(0.1, 0.2, 0.4)
            Rectangle(pos=(car_x + 70, car_y + 105), size=(70, 45))
            Rectangle(pos=(car_x + 160, car_y + 105), size=(70, 45))
            if self.start_time < 2.0:
                Color(1, 1, 0)
            else:
                if (self.frame // 15) % 2 == 0:
                    Color(1, 1, 0)
                else:
                    Color(0.4, 0.4, 0.4)
            Rectangle(pos=(car_x + 290, car_y + 30), size=(20, 30))
            Color(0.9, 0.1, 0.1)
            Rectangle(pos=(car_x - 10, car_y + 30), size=(10, 30))
            Color(0.05, 0.05, 0.05) 
            Ellipse(pos=(car_x + 40, car_y - 30), size=(60, 60))
            Ellipse(pos=(car_x + 200, car_y - 30), size=(60, 60))
            Color(0.7, 0.7, 0.7)
            angle = self.frame * 0.2
            cx1, cy1 = car_x + 40 + 30, car_y - 30 + 30
            Line(points=[cx1 + 20*math.cos(angle), cy1 + 20*math.sin(angle), cx1 - 20*math.cos(angle), cy1 - 20*math.sin(angle)], width=3)
            cx2, cy2 = car_x + 200 + 30, car_y - 30 + 30
            Line(points=[cx2 + 20*math.cos(angle), cy2 + 20*math.sin(angle), cx2 - 20*math.cos(angle), cy2 - 20*math.sin(angle)], width=3)

class LadaApp(App):
    def build(self):
        return LadaRoad()

if __name__ == '__main__':
    LadaApp().run()
