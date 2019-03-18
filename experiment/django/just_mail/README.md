# Just send a Django Mail

### Step 1: Install Django

- With pipenv:

```bash
$ pip install pipenv
$ pipenv install . --three
$ pipenv shell
```

- Without pipenv: please create a virtual environment and do `pip install django` inside the environment.

### Step 2: Configure

Ensure Email settings are correct.
```python
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "<HOST@EMAIL.COM>"
EMAIL_HOST_PASSWORD = "<HOST_EMAIL_PASSWORD>"
EMAIL_RECEIPIENT = ['<RECEPIRENT1@EMAIL.COM>', '<RECEPIRENT2@EMAIL.COM>']
```

### Step 3: Run-server

**Note: Please remember to activate environment**
```bash
$ python manage.py runserver
```

### Step 4: Send the mail!

Go to the address: `127.0.0.1:8000/send/` and wait for a couple of seconds and once you see the message on your browser, please proceed to check your inbox.
