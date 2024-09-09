### Парсер данных о сеансах кино

## Установка зависимостей

### 1. Установка Google Chrome (для Linux без графического интерфейса)
   - Скачайте последнюю версию браузера Chrome:
     ```bash
     wget -nc https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
     ```
   - Установите браузер с помощью команды:
     ```bash
     sudo apt install -f ./google-chrome-stable_current_amd64.deb
     ```

### 2. Установка библиотек `selenium` и `webdriver-manager`
   - Установите зависимости с помощью pip:
     ```bash
     pip install selenium webdriver-manager
     ```