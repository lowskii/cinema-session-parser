from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройки для работы в headless режиме
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Устанавливаем заголовки
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36")

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL сайта
url = 'https://www.kinosfera-baltika.ru/#/'
all_movies = {}

# Переход на сайт
driver.get(url)

try:
    # Ожидание появления нужного элемента
    dynamic_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "movies__item"))
    )

    # Ищем все элементы с карточками фильмов
    movies = driver.find_elements(By.CLASS_NAME, "movies__item")
    
    i = 0
    
    for movie in movies:
        # Получаем ID фильма
        movie_id = movie.find_element(By.CLASS_NAME, "movies__image").get_attribute("data-cb-id")

        # Находим название фильма
        name = movie.find_element(By.CLASS_NAME, "movies__title").text
        
        # Инициализируем список для хранения всех сеансов фильма
        sessions = []
        
        # Ищем все сеансы для данного фильма
        movie_sessions = movie.find_elements(By.CLASS_NAME, "shows__item")

        # Проходим по каждому сеансу
        for session in movie_sessions:
            try:
                # Извлекаем информацию о сеансе
                session_id = session.get_attribute("data-cb-id")  # Извлекаем ID сеанса
                time_session = session.find_element(By.CLASS_NAME, "shows__time").text
                price = session.find_element(By.CLASS_NAME, "shows__price").text
                session_type = session.find_element(By.CLASS_NAME, "shows__type").text
                
                session_info = {
                    'id': session_id,
                    'time': time_session,
                    'price': price,
                    'type': session_type
                }

                sessions.append(session_info)
                
            except Exception as session_error:
                print(f"Ошибка при обработке сеанса: {session_error}")
                continue
        
        # Добавляем фильм и его сеансы в общий словарь
        all_movies[i] = {'id': movie_id, 'name': name, 'sessions': sessions}
        i += 1
    
    # Выводим собранные данные о фильмах и сеансах
    for key, value in all_movies.items():
        print(f"{key}: {value}", end="\n")

except Exception as e:
    print(f"Ошибка: {e}")
finally:
    driver.quit()
