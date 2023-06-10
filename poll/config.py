close_options = ['Да', 'Нет']
questions = [
    {'text': 'Как вас зовут?', 'type': 'opened', 'options': None, 'right_answer': None},
    {'text': '➖ Вы знакомы с группой "Анизотропия"?', 'type': 'closed',
     'options': ['Да', 'Нет'], 'right_answer': 'Да'},
    {'text': '➖ Вам нравится рок"?', 'type': 'closed',
     'options': ['Да', 'Нет'], 'right_answer': 'Да'},
    {'text': '➖ Вам нравится их музыка?', 'type': 'closed',
     'options': ['Да', 'Нет'], 'right_answer': 'Да'},
    {'text': '➖ Сколько всего участников группы?', 'type': 'multiple_choice',
     'options': ['4', '3', '5', '2'], 'right_answer': '4'},
    {'text': '➖ Кто является основателем группы?', 'type': 'multiple_choice',
      'options': ['Иван', 'Никита', 'Лера', 'Алик'], 'right_answer': 'Иван'},
    {'text': '➖ Слышали ли вы их музыку?', 'type': 'closed',
     'options': ['Да', 'Нет'], 'right_answer': 'Да'},
    {'text': '➖ Если нет, то хотите ли послушать?', 'type': 'closed',
     'options': ['Да', 'Нет'], 'right_answer': 'Да'},
    {'text': '➖ Как называется их первый альбом?', 'type': 'multiple_choice',
     'options': ['Абсолют','Ангелы', '404', 'Аномалия'], 'right_answer': 'Абсолют'},
    {'text': '➖ Сколько песен они выпустили на данный момент?', 'type': 'multiple_choice',
      'options': [ '3','1', '5', '15'], 'right_answer': '3'},
    {'text': '➖ Укажите, к какой возрастной категории вы относитесь?:', 'type': 'multiple_choice',
      'options': ['10-20', '20-30', '30-40', '40-50', '50-60', '60+'], 'right_answer': '10-20'}
]