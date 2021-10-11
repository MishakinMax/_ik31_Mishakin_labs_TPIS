## Lab_2: Автоматизація. Знайомство з CI/CD.
### Хід Роботи.
1. Створив папку lab_2 з _README.md_ файлом
2. Інсталював `pipenv` та створив ізольоване середовище для Python за допомогою наступних команд
```bash
pip install pipenv
pipenv --python 3.7
pipenv shell
```
3. Встановив бібліотеку `requests`та бібліотеку `ntplib` за допомогою наступних команд
```bash
pipenv install requests
pipenv install ntplib
```
4. Створив файл `app.py` та скопіював туди код
5. Переконайтесь що програма працює правильно.
```bash
python app.py
```
Результат виконання
```bash

========================================
Результат без параметрів:
No URL passed to function
========================================
Результат з правильною URL:
Time is:  07:38:15 PM
Date is:  10-11-2021
success
```


6. Встановив бібліотеку `pytest` за допомогою наступних команди
```bash
pipenv install pytest
```
7. Приклади тестів, які знаходяться в окремій папці `tests`, запусутив та переконався що вони виконались успішно:
```bash
pytest tests/tests.py
```
Результат виконання
```bash
collected 5 items

tests\tests.py .....                                                                                             [100%]

================================================== 5 passed in 0.82s ==================================================
```

8. :exclamation: (Захист) Функцію яка перевіряє час доби AM/PM та повертає: Доброго дня/ночі;
```bash
def home_work(t = datetime.today().strftime("%I:%M %p")):
    return (("Доброї ночі") if ("PM" in t) else ("Доброго дня"))
```

9. :exclamation: (Захист) Тест що буде перевіряє правильність виконання функції;
```bash
    def test_home_work(self):
        self.assertEqual(home_work("08:55 PM"), "Доброї ночі")
        self.assertEqual(home_work("08:55 AM"), "Доброго дня")
```

10. Я Перенаправив результат виконання тестів у файл `results.txt` а також додав результат виконання програми у кінець цього ж файл, за допомогою наступних команд
```bash
    pytest tests/tests.py > results.txt
    python app.py >> results.txt
```
11. зроблено коміт із змінами до репозиторію.
12. Заповнюємо `Makefile` необхідними командами для повної автоматизації процесу СІ проекту
- директива install 
```bash
    @echo "Installing pipenv and dependencies."
	pip install pipenv
	pipenv --python 3.8.10
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest
```
- директива test 
```bash
    @echo "Start tests."
	pipenv run pytest tests/tests.py > results.txt
```
- директива run
```bash
    @echo "Run Python app."
	pipenv run python3 app.py >> results.txt
```
- директива deploy
```bash
    @echo "Adding and Committing results.txt to git."
	git add results.txt
	git commit -m "Automate commit by MakeFile"
	git push 
```

13. Закомітив зміни `Makefile` та перейшов на віртуальну машину Ubuntu;
14. Склонуйте git репозиторій на віртуальну машину Ubuntu. Перейдіть у папку лабораторної роботи та запустіть make:
```bash
make
```
- Результат виконання команди `make` є створене ізольоване середовище (venv), виконані тести, запущена програма та закомічений файл у git; 
15. Відредагував _README.md_ у цьому репозиторію. Створіть таблицю у персональному репозиторію. Створив пул-реквест до основного репозиторію.