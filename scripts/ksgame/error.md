[500 error] caused by: "NameError: name 'self' is not defined"
  File "c:\codes\bdadv4\scripts\ksgame\flask_server.py", line 106, in video_feed
    return Response(self.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
                    ^^^^

127.0.0.1 - - [16/Jul/2024 22:49:05] "GET / HTTP/1.1" 304 -
[2024-07-16 22:49:05,400] ERROR in app: Exception on /feed [GET]
Traceback (most recent call last):
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\codes\bdadv4\scripts\ksgame\flask_server.py", line 106, in video_feed
    return Response(self.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
                    ^^^^
NameError: name 'self' is not defined
127.0.0.1 - - [16/Jul/2024 22:49:05] "GET /feed HTTP/1.1" 500 -






[Logs]------------------------------
Read prefs: "C:\Users\kazuo\AppData\Roaming\Blender Foundation\Blender\4.1\config\userpref.blend"
Read blend: "c:\codes\bdadv4\game.blend"
showTxt: txt=register
showTxt: previous_txt=
register
 * Serving Flask app 'flask_server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:6999
 * Running on http://192.168.3.6:6999
Press CTRL+C to quit
127.0.0.1 - - [16/Jul/2024 22:48:38] "GET /socket.io/?EIO=4&transport=polling&t=P2xpM8n HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2024 22:48:38] "POST /socket.io/?EIO=4&transport=polling&t=P2xpMEJ&sid=edcY9uqn-nFeTsdIAAAA HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2024 22:48:38] "GET /socket.io/?EIO=4&transport=polling&t=P2xpMEM&sid=edcY9uqn-nFeTsdIAAAA HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2024 22:48:38] "GET /socket.io/?EIO=4&transport=polling&t=P2xpMJM&sid=edcY9uqn-nFeTsdIAAAA HTTP/1.1" 200 -
GPUTexture: Blender Texture Not Loaded!
GPUTexture: Blender Texture Not Loaded!
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
127.0.0.1 - - [16/Jul/2024 22:49:04] "GET /socket.io/?EIO=4&transport=websocket&sid=edcY9uqn-nFeTsdIAAAA HTTP/1.1" 200 -showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
127.0.0.1 - - [16/Jul/2024 22:49:05] "GET / HTTP/1.1" 304 -
[2024-07-16 22:49:05,400] ERROR in app: Exception on /feed [GET]
Traceback (most recent call last):
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 872, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 870, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask\app.py", line 855, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\codes\bdadv4\scripts\ksgame\flask_server.py", line 106, in video_feed
    return Response(self.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
                    ^^^^
NameError: name 'self' is not defined
127.0.0.1 - - [16/Jul/2024 22:49:05] "GET /feed HTTP/1.1" 500 -
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
127.0.0.1 - - [16/Jul/2024 22:49:05] "GET /socket.io/?EIO=4&transport=polling&t=P2xpSxv HTTP/1.1" 200 -
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
127.0.0.1 - - [16/Jul/2024 22:49:06] "POST /socket.io/?EIO=4&transport=polling&t=P2xpSyL&sid=WZkjiBvE-Wu6K8nHAAAC HTTP/1.1" 200 -
127.0.0.1 - - [16/Jul/2024 22:49:06] "GET /socket.io/?EIO=4&transport=polling&t=P2xpSyS&sid=WZkjiBvE-Wu6K8nHAAAC HTTP/1.1" 200 -
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
in handle_message1
in handle_message2
in handle_message4
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
in handle_message1
in handle_message2
in handle_message4
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
showTxt: txt=in key_sm, input_key=A
showTxt: previous_txt=
in key_sm, input_key=A
in handle_message1
in handle_message2
in handle_message4
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=in key_sm, input_key=D
showTxt: previous_txt=
in key_sm, input_key=D
showTxt: txt=unregister
showTxt: previous_txt=
unregister
Traceback (most recent call last):
  File "c:\codes\bdadv4\game.blend\__main__.py", line 74, in modal
    self.cancel(context)
  File "c:\codes\bdadv4\game.blend\__main__.py", line 157, in cancel
    unregister()
  File "c:\codes\bdadv4\game.blend\__main__.py", line 174, in unregister
    fsw.socketio.stop()
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\flask_socketio\__init__.py", line 726, in stop
    func = flask.request.environ.get('werkzeug.server.shutdown')
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 311, in __get__
    obj = instance._get_current_object()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request. Consult the documentation on testing for
information about how to avoid this problem.
Error: Python: Traceback (most recent call last):
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 311, in __get__
    obj = instance._get_current_object()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\bin\blender-4.1.0-windows-x64\4.1\python\Lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that needed
an active HTTP request. Consult the documentation on testing for
information about how to avoid this problem.

