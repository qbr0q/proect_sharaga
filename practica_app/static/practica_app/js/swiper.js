let currentSlide = 0;
const slides = document.querySelector('.slides');
const totalSlides = document.querySelectorAll('.slide').length;

// Функция для отображения текущего слайда
function showSlide(index) {
    // Проверяем граничные условия
    if (index >= totalSlides) {
        currentSlide = 0; // Переход к первому слайду, если достигнут конец
    } else if (index < 0) {
        currentSlide = totalSlides - 1; // Переход к последнему слайду, если достигнуто начало
    } else {
        currentSlide = index;
    }

    // Рассчитываем смещение для перехода к текущему слайду
    const offset = -currentSlide * 100;
    slides.style.transform = `translateX(${offset}%)`;
}

// Функция для перехода к следующему слайду
function nextSlide() {
    showSlide(currentSlide + 1);
}

// Функция для перехода к предыдущему слайду
function prevSlide() {
    showSlide(currentSlide - 1);
}

// Автоматическая прокрутка (опционально)
let autoSlideInterval = setInterval(nextSlide, 5000);

// Остановка автоматической прокрутки при наведении на слайдер (опционально)
const slider = document.querySelector('.slider');
slider.addEventListener('mouseenter', () => {
    clearInterval(autoSlideInterval);
});

// Возобновление автоматической прокрутки при уходе курсора (опционально)
slider.addEventListener('mouseleave', () => {
    autoSlideInterval = setInterval(nextSlide, 5000);
});