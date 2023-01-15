### HTTP / HTTPS
- Frontend requests, Backend responds
- Connection closes

#### What if real time data transfer needed?
Here comes `Websockets` comes into play

### Websockets (Can be achieved with the channel package in django)
- Backend continuously listen to events which takes place in backend.
- It can also send response to frontend without them making any request.
- And data are sent on its own to frontend
- Eg., chat messages

NB: `Signals` can be used for internal tasks. Works as triggers.

### Using Websockets in Django
- `pip install channels`
- Add `channels` in INSTALLED_APPS of [settings.py](/chatproject/settings.py) file
- Then perform makemigrations and migrate
- Add this in [settings.py](/chatproject/settings.py) file : `ASGI_APPLICATION = "chatproject.asgi.application"`. As channels won't work in WSGI, ASGI is needed.
- Create a file called [asgi.py](/chatproject/asgi.py) in project root dir.
- Create a file called [routing.py](/chatproject/routing.py) in the project root dir.
- Create a file called [consumers.py](/chatproject/consumers.py) in the project root dir.
- NB: What `urls.py is to views.py`, `routing.py is same to consumers.py`.
- Make an API from models to views to urls.
- Open url which has websockets enabled and see the changes happen without refreshing.
