from django.shortcuts import render

# Create your views here.

swiper_info = [
    {'img_of_lp': 'practica_app/media/python.jpg', 'lp': 'Python',
     'details': 'Мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией'},
    {'img_of_lp': 'practica_app/media/go.jpg', 'lp': 'Go',
     'details': 'Компилируемый многопоточный язык программирования, разработанный внутри компании Google.'},
    {'img_of_lp': 'practica_app/media/js.jpg', 'lp': 'JavaScript',
     'details': 'мультипарадигменный язык программирования. Поддерживает объектно-ориентированный, императивный и функциональный стили.'},
]

courses_info = [
    {
        'img': 'practica_app/media/javascript_course_img.jpg',
        'details': 'Изучите основы JavaScript, включая синтаксис, DOM-манипуляции и асинхронное программирование.',
        'name': 'JavaScript для начинающих',
        'time': '25 часов',
        'price': '7 499 ₽'
    },
    {
        'img': 'practica_app/media/go_course_img.jpg',
        'details': 'Освойте Go (Golang) — современный язык для создания высокопроизводительных приложений.',
        'name': 'Go: Программирование для профессионалов',
        'time': '30 часов',
        'price': '8 999 ₽'
    },
    {
        'img': 'practica_app/media/python_course_img.jpg',
        'details': 'Погрузитесь в мир Python: от основ до продвинутых концепций, таких как машинное обучение.',
        'name': 'Python: От новичка до эксперта',
        'time': '40 часов',
        'price': '9 999 ₽'
    },
    {
        'img': 'practica_app/media/java_course_img.jpg',
        'details': 'Изучите Java — мощный язык для создания корпоративных приложений и Android-разработки.',
        'name': 'Java: Основы и продвинутые темы',
        'time': '35 часов',
        'price': '8 499 ₽'
    },
    {
        'img': 'practica_app/media/cpp_course_img.jpg',
        'details': 'Освойте C++ для разработки высокопроизводительных приложений и игр.',
        'name': 'C++: Программирование для разработчиков',
        'time': '45 часов',
        'price': '10 999 ₽'
    },
    {
        'img': 'practica_app/media/ruby_course_img.jpg',
        'details': 'Изучите Ruby — элегантный и простой язык для веб-разработки и создания скриптов.',
        'name': 'Ruby: Основы и веб-разработка',
        'time': '20 часов',
        'price': '6 999 ₽'
    },
    {
        'img': 'practica_app/media/php_course_img.jpg',
        'details': 'Освойте PHP для создания динамических веб-сайтов и работы с базами данных.',
        'name': 'PHP: Веб-разработка с нуля',
        'time': '25 часов',
        'price': '7 299 ₽'
    },
    {
        'img': 'practica_app/media/swift_course_img.jpg',
        'details': 'Изучите Swift для разработки приложений под iOS и macOS.',
        'name': 'Swift: Разработка под Apple',
        'time': '30 часов',
        'price': '8 999 ₽'
    }
]

def main_page(request):
    return render(request, 'practica_app/main_page.html', context={'lps_info': swiper_info,
                                                                   'courses_info': courses_info})