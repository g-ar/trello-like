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

    Body

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

    Headers

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

  Headers

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

- ``DELETE``

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Logged out"
        }

``board/``
~~~~~~~~~~

- ``POST``
    Add a board for the logged in user

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "board_name": "Home"
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Board added"
        }

- ``GET``

  - Request

    Headers: Token

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": [
            {
              "list_ids": "[]",
              "board_id": 2,
              "board_name": "SW"
            },
            {
              "list_ids": "[]",
              "board_id": 3,
              "board_name": "Home"
            }
          ],
          "message": "Board details"
        }

  - Making a get request to ``board/<board_id>`` gets details of only the requested board id

- ``PUT``
    Update the board details

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "board_id": 3,
          "board_name": "Home Tasks"
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Board updated"
        }

- ``DELETE``
    Delete all the boards mentioned in ``board_ids``

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "board_ids": [2, 3]
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Boards deleted"
        }

``list/``
~~~~~~~~~

- ``POST``

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "list_name": "Doing",
          "board_id": 2
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "List added"
        }

- ``GET``
    Retrieves all the lists that are visible for the logged in user

  - Request

    .. code:: text
        

        Token: <the token>

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": [
            {
              "list_id": 2,
              "card_ids": "[2]",
              "list_name": "Doing"
            },
            {
              "list_id": 3,
              "card_ids": "[3]",
              "list_name": "Doing"
            }
          ],
          "message": "List details"
        }

- ``PUT``
    Can be used to update the list entries

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "list_id": 2,
          "list_name": "Done"
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "List updated"
        }

- ``DELETE``
    Used to delete the entries in the database

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "list_ids": [1, 2],
          "board_id": 1
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Lists deleted"
        }

``card/``
~~~~~~~~~

- ``POST``
    Add a new card entry by posting the details. ``list_id`` indicates the list it's part of.

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "card_name": "Authentication",
          "card_desc": "Providing basic token authentication",
          "card_due_date": "2017-01-10",
          "card_status": false,
          "list_id": 2
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Card added"
        }

- ``GET``

  - Request

    .. code:: text
        

        Token: <the token>

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": [
            {
              "card_due_date": "2017-01-10",
              "card_id": 2,
              "card_status": false,
              "card_desc": "Providing basic token authentication",
              "card_name": "Authentication"
            },
            {
              "card_due_date": "2017-02-10",
              "card_id": 3,
              "card_status": false,
              "card_desc": "Sow and reap!",
              "card_name": "Gardening"
            }
          ],
          "message": "Card details"
        }

- ``PUT``

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "card_name": "Gardening",
          "card_desc": "Sow and reap.",
          "card_id": 3
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Card updated"
        }

- ``DELETE``
    Delete the card ids that are part of the list id, given in the message body

  - Request

    .. code:: text
        

        Content-Type: application/json
        Token: <the token>

    .. code:: js
        

        {
          "card_ids": [4, 5],
          "list_id": 3
        }

  - Response

    .. code:: js
        

        {
          "success": true,
          "payload": null,
          "message": "Cards deleted"
        }

Database Tables
---------------

Users
~~~~~

.. code:: text
    

    |---------+-----------+-------+---------------+-----------|
    | user_id | user_name | email | password_hash | board_ids |
    |---------+-----------+-------+---------------+-----------|
    |         |           |       |               |           |
    |---------+-----------+-------+---------------+-----------|

- ``board_ids`` keep track of the list of the boards that the user can access

- The boards can be displayed according to the order of the list

Token
~~~~~

.. code:: text
    

    |---------+--------------|
    | user_id | access_token |
    |---------+--------------|
    |         |              |
    |---------+--------------|

- Whenever user logs in, a token is generated and mapped to that ``user_id``

Boards
~~~~~~

.. code:: text
    

    |----------+------------+----------|
    | board_id | board_name | list_ids |
    |----------+------------+----------|
    |          |            |          |
    |----------+------------+----------|

- When ``list_ids`` are the lists that's part of a given ``board_id``. When a new list is added, that id is appended to ``list_ids``

Lists
~~~~~

.. code:: text
    

    |---------+-----------+----------|
    | list_id | list_name | card_ids |
    |---------+-----------+----------|
    |         |           |          |
    |---------+-----------+----------|

- ``card_ids`` is the list of the cards that's part of this list

- The order in which the cards are to be displayed is suggested by this

Cards
~~~~~

.. code:: text
    

    |---------+-----------+-----------+---------------+-------------|
    | card_id | card_name | card_desc | card_due_date | card_status |
    |---------+-----------+-----------+---------------+-------------|
    |         |           |           |               |             |
    |---------+-----------+-----------+---------------+-------------|

- ``card_due_date`` is in YYYY-MM-DD format

- ``card_status`` is boolean

Notes
-----

- Moving cards from one list to another can be done by sending two ``PUT`` requests, with the updated ``card_ids`` in the message body for each ``list_id``

  - E.g. if ``list_id`` 2 has ``card_ids`` [1, 4, 5], and ``list_id`` 3 has ``card_ids`` [3, 6], and if ``card_id`` 4 is to be moved to ``list_id`` 3, send different ``PUT`` requests to ``list/`` with the following message body

    - Request 1

      .. code:: js
          

          {
            "list_id": 2,
            "card_ids": [1, 5]
          }

    - Request 2

      .. code:: js
          

          {
            "list_id": 2,
            "card_ids": [3, 6, 4]
          }

  - The order of the cards is maintained, when a ``GET`` request is made

  - The same logic goes to lists and boards as well

To do
-----

- Implement better authorization mechanism like OAuth

- Use a different database, as sqlite is more suited for higher read rates and low writes

- Complete validations of all kinds of requests

- Cascade the deletion of lists and cards when it's no longer a part of any board, or perhaps do a garbage collection once a day
