# LAB_DJANGO_AUTH


## Using your previous LAB “LAB_DJNAGO_ORM_3_RELATIONS”,

### Do the following:

- Add user Accounts (register, login, logout)
- Add group in the Admin for Managers , and assign some users as manager
- Limit the access to adding a doctor page to the users in the Managers group only.




     Username for admin page : AlaaAl
     password : 123456


      {% if request.user.is_authenticated %}
               

                  <li class="nav-item">
                    <a class="nav-link tx-color" href="">>Welcome {{ request.user.first_name }}</a>
                  </li>
                    <li class="nav-item">
                      <a class="nav-link tx-color" href="{% url 'Users:logout_user' %}">Logout</a>
                    </li>
                
                  {% else %}


