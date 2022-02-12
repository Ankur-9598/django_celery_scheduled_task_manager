
from datetime import datetime, timedelta

from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from pytz import timezone

from tasks.models import Task, TaskReport


@shared_task(name="send_periodic_reportes_to_user")
def send_email_report():

    for user in User.objects.all():
        curr_user_task_report = TaskReport.objects.filter(user=user)

        # if user has created configuration and enabled it
        if curr_user_task_report.exists() and curr_user_task_report[0].enabled:

            task_report = TaskReport.objects.get(user=user)
            curr_time = datetime.now(tz=timezone('UTC'))

            # if report time has didn't reached yet..  continue
            if task_report.next_run_at > curr_time:
                continue
            
            # Get the email content and send the mail
            email_content = get_user_tasks_status(user)
            send_mail("Tasks Report for Today", email_content, "rt945471@gmail.com", [task_report.user_mail])

            # Update the next run at for the current user task report
            next_run_at = task_report.next_run_at + timedelta(days=1)
            curr_user_task_report.update(next_run_at=next_run_at)


def get_user_tasks_status(user):
    total_tasks = Task.objects.filter(user=user, deleted=False)
    pending_tasks = total_tasks.filter(completed=False).count()
    completed_tasks = total_tasks.count() - pending_tasks
    greeting = f"Hi {user.username},\n\nHere is your tasks report:\n\nTotal tasks added: {len(total_tasks)}\nPending tasks: {pending_tasks}\nCompleted tasks: {completed_tasks}\n\nThanks"
    return greeting

