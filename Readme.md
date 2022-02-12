The specification for this program is as follows,

## Specification

You are asked to build the same project we worked on [Django REST_API Task manager](https://github.com/Ankur-9598/django_with_REST) and add two new features to it.

1) Move all our code to use template blocks with a base template named `base.html`
2) Create a user-configurable report, The user can configure when he would like to receive his email reports ( in a day ) ( like 10PM or 11AM or any other valid time ) or if he wants to disable reports altogether. A background job would ensure that the user would get his reports at the specified time
3) The reports should contain a breakdown based on the task's status. ie, it should show the number of tasks with all the possible statuses


## Routes for report
1. ```/report``` :- For creating the report configuration
2. ```/update-report``` :- For updating the report configuration

The background jobs are executed with the help of celery workers.

## Run Locally

To install the requirements for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

