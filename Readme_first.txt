������ ��������� ������ ������������� ������������ ����� Labirint.ru

� ����� data.py ��������� �������� ������, ������� ����� �������� Chrome/Firefox. ��� ������ �������� ����� ��������/������ ��������������� ���� ����������� ��� ���������� BROWSER. ��� �� ���������� ������ ��� ����������� � ����� �������� (���������� ������ �����������).

������� ������ � ����� conftets.py. ��� �� ���������� ������ ��� ������� �����.

�������������� �������� ������� ������� � ����� page_utils.py. ��� ��������� ������� ��������, ���������������, ������� �����, ��������, ��������� �������, ����� � �������� ������� �� ��������.

����� ��������� �� ����������:
1.	test_login.py - ��������� ���� � ������� (����� "test_login" �������� � ���������  cookies)
2.	test_login_cookies.py - ��������� ���� � ������� ��� ������ cookies
3.	test_no_cookies.py - ��������� �������� �� ������� �������� 
4.	test_logic_no_login.py - ��������� ������ ��������� ������� �����

����� ����� ��������� �� PyCharm ��� �� ���������� ������, ��� �������� ��������, ��������:
- python -m pytest -v .\tests\test_logic_no_login.py
- python -m pytest -v .\tests\test_logic_no_login.py -k "any_class"
- python -m pytest -v .\tests\test_logic_no_login.py::TestMoveToBasket:: test_move_book_to_basket
- python -m pytest -v .\tests\test_business_logic_no_login.py -k "class or test"
- python -m pytest -v .\tests\
