# Backend

WebsiteApp:

This is a fullt function website project with Logout/login functionality, dynamic data(Some cards like Quick, Affordable, Always available)
The user and data is stored in Postgresql.

To run the website:
1. Open the folder containing manage.py in cmd.
2. Run: python manage.py runserver

Website Navigation:
1. '/': This is the index.html or home page.
2. 'login': The login page.
3. '/register': The page for user resitration or new account creation.
4. '/logout': The logout page. This redirects users to Home page after logging out.
5. '/admin': This is a defalut page created by django to manage users and database.

If you are unable to loin into admin run: python manae.py createsuperuser

