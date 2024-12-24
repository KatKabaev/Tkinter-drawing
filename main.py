import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw


class DrawingApp:
    """
    Класс для приложения рисования с возможностью сохранения изображения.
    """

    def __init__(self, root):
        """
        Инициализация приложения.

        :param root: Корневой виджет.
        """

        self.brush_size_scale = None
        self.root = root
        self.root.title("Рисовалка с сохранением в PNG")

        # Создание нового изображения
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Создание холста, видимого для пользователя
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        # Хранение текущего значения размера кисти
        self.brush_size = tk.IntVar()
        self.brush_size.set(1)

        self.setup_ui()

        # Переменные, отслеживающие последние координаты x и y, на которых пользователь отпустил мышь
        self.last_x, self.last_y = None, None
        self.pen_color = 'black'

        # Привязка события к холсту
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)


    def setup_ui(self):
        """
        Создание пользовательского интерфейса.
        """

        # Создается фрейм (контейнер для виджетов)
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X)

        # Создание кнопок
        clear_button = tk.Button(control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT)

        color_button = tk.Button(control_frame, text="Выбрать цвет", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

        save_button = tk.Button(control_frame, text="Сохранить", command=self.save_image)
        save_button.pack(side=tk.LEFT)

        brush_size_label = tk.Label(control_frame, text="Размер кисти:")
        brush_size_label.pack(side=tk.LEFT)

        brush_size_frame = tk.Frame(control_frame)
        brush_size_frame.pack(side=tk.LEFT)

        sizes = [1, 2, 5, 10]
        self.create_brush_size_menu(brush_size_frame, sizes)


    def create_brush_size_menu(self, parent, sizes):
        """
        Создает меню для выбора размера кисти и шкалу для его изменения.
        :param parent: Родительский виджет, внутри которого будет создано меню и шкала.
        :param sizes: Список доступных размеров кисти.
        """

        size_menu = tk.OptionMenu(parent, self.brush_size, *sizes, command=self.update_brush_size)
        size_menu.pack(side=tk.LEFT)

        self.brush_size_scale = tk.Scale(parent, from_=1, to=10, orient=tk.HORIZONTAL,
                                         variable=self.brush_size, length=100,
                                         command=self.update_brush_size)
        self.brush_size_scale.pack(side=tk.LEFT)


    def update_brush_size(self, new_size):
        """
        Обновляет размер кисти.
        :param new_size: Новое значение размера кисти.
        """

        self.brush_size.set(new_size)


    def paint(self, event):
        """
        Рисование линии на холсте.

        :param event: Событие, содержащее координаты для рисования линии.
        """

        if self.last_x and self.last_y:
            width = self.brush_size_scale.get()
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                    width=width, fill=self.pen_color,
                                    capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.last_x, self.last_y, event.x, event.y], fill=self.pen_color,
                           width=width)

        self.last_x = event.x
        self.last_y = event.y


    def reset(self, event):
        """
         Сброс последних координат.

         :param event: Событие, которое инициирует сброс.
         """

        self.last_x, self.last_y = None, None


    def clear_canvas(self):
        """
        Очистка холста и сброс изображения.
        """

        self.canvas.delete("all")
        self.image = Image.new("RGB", (600, 400), "white")
        self.draw = ImageDraw.Draw(self.image)


    def choose_color(self):
        """
        Выбор цвета кисти.
        """

        self.pen_color = colorchooser.askcolor(color=self.pen_color)[1]


    def save_image(self):
        """
        Функция для сохранения изображения.
        """

        # Запрашиваем у пользователя путь для сохранения файла
        file_path = filedialog.asksaveasfilename(filetypes=[('PNG files', '*.png')])

        # Проверяем, был ли выбран путь и сохраняем
        if file_path:
            if not file_path.endswith('.png'):
                file_path += '.png'
            self.image.save(file_path)
            messagebox.showinfo("Информация", "Изображение успешно сохранено!")


def main():
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()