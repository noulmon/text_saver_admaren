# TEXT_SAVER: ADMAREN

### Introduction:
_**Text Saver**_ is a Django based application the provides API endpoints for save _**Text Saver**_ is a Django based application the provides API endpoints for save and retrieve short text snippets with a title
 and retrieve the same. The application uses JWT token for user authentication.

### Follow the steps to _run the application_:

1. Install all the required packages(python modules):

    ```pip install -r requirements.txt```

2. Migrate all the models to the database(Assuming that you've already setup the Database- PostgreSQL preferred)
 
    ```python manage.py migrate```
    
3. When the migrations are successfully completed, we can run the server:

    ```python manage.py runserver```
    
    If the steps are followed correctly, the server will be up and running.
 
 4. To gather all static files:
   
    ```python manage.py collectstatic```

 4. To login to admin panel, we have to create a superuser(input email and password):
 
    ```python manage.py createsuperuser```
    
    User can log into the **Admin Panel** using the following url(assuming that you are on local server):
    
        http://127.0.0.1:8000/admin/
    
    On signing in to the admin panel, admin users can:
    
        ```1. Add users```
        ```2. Add text snippets```

## API Documentation:
   - JSON file(postman collection): ``docs/api/TEXT_SAVER_ADMAREN.postman_collection.json``
   - Browsable Documentation: `https://documenter.getpostman.com/view/6826654/TVRg9AKj` 
   
## API Endpoints:
##### User:
1. User Login: `/user/login/` [POST] (new user will be created if email doesn't exists)
2. User token refresh: `/user/token-refresh/` [POST]

##### Text Snippets:
1. Overview: `/text_snippet/overview/` [GET]
2. Create: `/text_snippet/create/` [POST]
3. Detail: `/text_snippet/detail/<int:pk>/` [GET]
4. Update: `/text_snippet/update/<int:pk>/` [PATCH]
5. Delete: `/text_snippet/delete/<int:pk>/` [DELETE]

##### TAGs:
1. List: `/text_snippet/tag/list/` [GET]
2. Detail: `/text_snippet/tag/detail/<int:pk>/` [GET]
