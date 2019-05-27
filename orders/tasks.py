from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def OrderCreated(order_id):

    order = Order.objects.get(id=order_id)
    print(order)
    subject = 'შეკვეთის ნომერი {}'.format(order.id)
    message = 'ძვირფასო {}, თქვენი შეკვეთა წარმატებით განხორციელდა. ' \
              'შეკვეთის ნომერი: {}'.format(order.name, order.id)
    mail_send = send_mail(subject, message, 'burgerstation@zukaburgers.com',
                          ['g.zakareishvili@gmail.com'])
    return mail_send