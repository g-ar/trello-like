APIs
----

``register/``
~~~~~~~~~~~~~

- ``POST``
    Post details to register a new user

  - Request
    Headers

    .. code:: text
        

        Content-Type: application/json

    .. code:: js
        

        {
          "email": "jane@doe.com",
          "password": "mightypass",
          "user_name": "janed"
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "User added"
        }

- ``GET``
    Get the user details of the logged in user (``login/``)

  - Request
    Header

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": {
            "boards": [],
            "email": "jane@doe.com",
            "user_name": "janed"
          },
          "message": "User details"
        }

- ``DELETE``
  Log out and delete from database the current logged in user
  Header

  .. code:: text
      

      Content-Type: application/json
      Token: :shatok

``login/``
~~~~~~~~~~

- ``POST``

  - Request

    .. code:: text
        

        Content-Type: application/json

    .. code:: js
        

        {
          "email": "jane@doe.com",
          "password": "mightypass"
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": {
            "Token": "2d122a160cd91b4b087e4fd9092ae6610ac35e3e"
          },
          "message": "Logged in"
        }
