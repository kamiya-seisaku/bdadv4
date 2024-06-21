Python: Traceback (most recent call last):
  File "c:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 311, in __get__
    obj = instance._get_current_object()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request. Consult the documentation on testing for
information about how to avoid this problem.
