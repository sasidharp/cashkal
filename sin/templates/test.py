>>> import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)]
Type "copyright", "credits" or "license" for more information.

IPython 2.2.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

PyDev -- Python IDE for Eclipse
For help on using PyDev's Console see http://pydev.org/manual_adv_interactive_console.html
C:\Python34\python.exe 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)]
>>> import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'hello2.settings'; import django
>>> if django.get_version() < '1.5': from django.core import management; import hello2.settings as settings; management.setup_environ(settings)
>>> 
>>> import datetime
>>> import timedelta
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\IPython\core\interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-5-1bc6c9cf1546>", line 1, in <module>
    import timedelta
ImportError: No module named 'timedelta'
>>> import Timedelta
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\IPython\core\interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-6-6b57ce82abdd>", line 1, in <module>
    import Timedelta
ImportError: No module named 'Timedelta'
>>> import TimeDelta
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\IPython\core\interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-7-b095d3032507>", line 1, in <module>
    import TimeDelta
ImportError: No module named 'TimeDelta'
>>> from datetime import timedelta
>>> day=datetime.date.today()
>>> print(day)
2014-09-12
>>> day=day+timedelta(days=10)
>>> print(day)
2014-09-22
>>> day=day+timedelta(days=7)
>>> print(day)
2014-09-29
>>> finaldate=datetime.date.today()+timedelta(days=730)
>>> print(finaldate)
2016-09-11
>>> while day < finaldate:
...     print(date)
...     date = date + timedelta(days=7)
...     
Traceback (most recent call last):
  File "C:\Python34\lib\site-packages\IPython\core\interactiveshell.py", line 2883, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-17-5f76f1089977>", line 2, in <module>
    print(date)
NameError: name 'date' is not defined
