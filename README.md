# По структуре приложения:
* Представление и его логика в [app.py](app.py)
* Все функции описывающие работу команд и собирающие данные находятся в [utils.py](utils.py)
* Схема сериализации данных из квери запроса в [models.py](models.py)
* Константы описаны в [constants.py](constants.py)

___
# Примеры запросов для обработки:
### ip-адреса всех POST запросов
`http://127.0.0.1:8080/perform_query?cmd1=filter&value1=POST&cmd2=map&value2=0&file_name=apache_logs.txt`
### методы по которым были обращения к Apache серверу
`http://127.0.0.1:8080/perform_query?cmd1=map&value1=5&cmd2=unique&value2=&file_name=apache_logs.txt`
### первые 5 строк по c url-ом http://semicomplete.com
`http://127.0.0.1:8080/perform_query?cmd1=filter&value1=http://semicomplete.com/&cmd2=limit&value2=5&file_name=apache_logs.txt`

___
# По критериям выполнения:
- [ ]  Использован файловый дескриптор как генератор.
- [ ]  Применены функции map, filter, sorted, list, set (или dict, или counter).
- [ ]  Решение позволяет конструировать запрос, например, **cmd1=filter&value1=POST, cmd2=limit&value2=5.**
- [ ]  Использованы lambda-функции.