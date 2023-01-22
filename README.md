# Backend

**WebsiteApp:**

This is a fullt function website project with Logout/login functionality, dynamic data(Some cards like Quick, Affordable, Always available)
The user and data is stored in Postgresql.

The skeleton for the dynamic data is in models.py file.

To run the website:
1. Open the folder containing manage.py in cmd.
2. Run: python manage.py runserver

Website Navigation:
1. '/': This is the index.html or home page.
2. 'login': The login page.
3. '/register': The page for user resitration or new account creation.
4. '/logout': The logout page. This redirects users to Home page after logging out.
5. '/admin': This is a defalut page created by django to manage users and database.

If you are unable to login into admin run: python manage.py createsuperuser

**Blog:**
It is a Website which has blog articles which are sorted on newest first basis.
The data is stored in db.sqlite3 file which can be access in '/admin' site.

**Weather Website**
It is a website which (POST) calls a weather API from OpenWeather and tells the temperature, humidity, pressure of a city.
