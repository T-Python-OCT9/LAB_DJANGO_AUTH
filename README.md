# LAB_DJNAGO_ORM_3_RELATIONS

# LAB_DJANGO_AUTH


## Using your previous LAB “LAB_DJNAGO_ORM_3_RELATIONS”,

### Do the following:

- Add user Accounts (register, login, logout)
- Add group in the Admin for Managers , and assign some users as manager
- Limit the access to adding a doctor page to the users in the Managers group only.




## Create a Clinic Website , the clinic has the following :
- Home page to display all the doctors in your clinic .
- detail page for doctor, when clicked the doctor detail page is displayed.
- search page for doctors by name.


### A patient can do the following:
- Browse the doctors and view the doctor's detail page.
- View the previous appointments on the doctor's page.
- Book an appointment with a date on that doctor.


### Models

- Doctor model should have
- - name
- - description
- - specialization (use text choices)
- - experience_years
- - rating



- Appointment Model
- - Relation with doctor
- - patient_name
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended


### styling
- Use bootstrap CSS library or similar for styling the website . 
- Use some images to represent the clinic building and facilities as a gallery.


### Bonus
When patient books an appointmnet with the doctor , check if the doctor is free on that date & time.
