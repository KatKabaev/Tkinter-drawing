# Программа для создания изображений на основе TKinter

Данная программа представляет собой пример использования библиотеки TKinter для создания графического интерфейса.
<br>
<br>

## Класс DrawingApp

### Конструктор класса принимает один параметр:

- **root**: Это корневой виджет Tkinter, который служит контейнером для всего интерфейса приложения.

### Внутри конструктора выполняются следующие ключевые действия:

- Устанавливается заголовок окна приложения.

- Создается объект изображения (self.image) с использованием библиотеки Pillow. Это изображение служит виртуальным холстом, на котором происходит рисование. Изначально оно заполнено белым цветом.

- Инициализируется объект ImageDraw.Draw(self.image), который позволяет рисовать на объекте изображения.

- Создается виджет Canvas Tkinter, который отображает графический интерфейс для рисования. Размеры холста установлены в 600x400 пикселей.

- Создается объект целочисленных значений(self.brush_size) для хранение текущего значения размера кисти.

- Вызывается метод self.setup_ui(), который настраивает элементы управления интерфейса.

- Привязываются обработчики событий к холсту для отслеживания движений мыши при рисовании () и сброса состояния кисти при отпускании кнопки мыши ().

### Метод setup_ui(self)

Этот метод отвечает за создание и расположение виджетов управления:

- Кнопки "Выбрать цвет", "Кисть", "Ластик", "Размер кисти", "Размер холста", "Текст", "Изменить фон", "Очистить" и "Сохранить".

- Вызывает метод create_brush_size_menu.

### Метод eraser(self):

Меняет цвет пера на "white" при нажатии на кнопку ластика.

### Метод brush(self):

Меняет цвет кисти на "black" при нажатии на кнопку кисти.

### Метод create_brush_size_menu(self, parent, sizes)

- parent: Родительский виджет, внутри которого будет создано меню и шкала.
  
- sizes: Список доступных размеров кисти.

- Создает меню для выбора размера кисти и шкалу для его изменения.

### Метод update_brush_size(self, new_size)

Обновляет размер кисти.

### Метод size_canvas(self):

Обновляет размер холста.
        
### Метод paint(self, event)

Функция вызывается при движении мыши с нажатой левой кнопкой по холсту. Она рисует линии на холсте Tkinter и параллельно на объекте Image из Pillow:

- event: Событие содержит координаты мыши, которые используются для рисования.

- Линии рисуются между текущей и последней зафиксированной позициями курсора, что создает непрерывное изображение.

### Метод reset(self, event)

Сбрасывает последние координаты кисти. Это необходимо для корректного начала новой линии после того, как пользователь отпустил кнопку мыши и снова начал рисовать.

### Метод clear_canvas(self)

Очищает холст, удаляя все нарисованное, и пересоздает объекты Image и ImageDrawдля нового изображения.

### Метод choose_color(self)

Открывает стандартное диалоговое окно выбора цвета и устанавливает выбранный цвет как текущий для кисти.

### Метод add_text(self):

Добавляет текст на холст.

### Метод place_text(self, event):

Размещает введенный текст на холсте.

### Метод change_bg_color(self):

Изменяет цвет фона холста.
        
### Метод save_image(self)

Позволяет пользователю сохранить изображение, используя стандартное диалоговое окно для сохранения файла. Поддерживает только формат PNG. В случае успешного сохранения выводится сообщение об успешном сохранении.


### Использование приложения

Пользователь может рисовать на холсте, выбирать цвет и размер кисти, очищать холст и сохранять в формате PNG.

<p align="center">
<img src="https://github.com/KatKabaev/Tkinter-drawing/blob/main/images/img1.png">
