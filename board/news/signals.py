from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post
from sign.models import MyUser



@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, **kwargs):
    
    users = MyUser.objects.filter(mailing = True)
    html_content = render_to_string('email_template.html', { 'head': instance.head_of_post, 'text':instance.article_text[:50], 'article_id':instance.id})
   
    for user in users:
        
                msg = EmailMultiAlternatives(
                subject=f'Здравствуй, {user.username}. Новая новость на нашем сайте!',
                body=html_content,
                from_email='TestDjango1@yandex.ru',
                to=[user.email,])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print('Усшено отправлено',user.username)

        