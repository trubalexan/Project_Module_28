Данная коллекция тестов предназначена тестирования сайта Labirint.ru

В файле data.py находятся исходные данные, включая выбор драйвера Chrome/Firefox. Для выбора драйвера нужно добавить/убрать соответствующий знак комментария для переменной BROWSER. Там же находиться данные для авторизации и адрес страницы (необходимы данные авторизации).

Драйвер описан в файле conftets.py. Там же установлен таймер для каждого теста.

Дополнительные полезные утилиты описаны в файле page_utils.py. Они позволяют открыть страницу, проскролировать, навести мышку, кликнуть, проверить корзину, найти и кликнуть элемент на странице.

Тесты разделены по категориям:
1.	test_login.py - тестирует вход в систему (метод "test_login" получает с сохраняет  cookies)
2.	test_login_cookies.py - проверяет вход в систему при помощи cookies
3.	test_no_cookies.py - проверяет элементы на главной странице 
4.	test_logic_no_login.py - проверяет работу некоторых функций сайта

Тесты можно запускать из PyCharm или из коммандной строки, без указания драйвера, например:
- python -m pytest -v .\tests\test_logic_no_login.py
- python -m pytest -v .\tests\test_logic_no_login.py -k "any_class"
- python -m pytest -v .\tests\test_logic_no_login.py::TestMoveToBasket:: test_move_book_to_basket
- python -m pytest -v .\tests\test_business_logic_no_login.py -k "class or test"
- python -m pytest -v .\tests\
