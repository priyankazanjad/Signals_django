from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete,pre_init,post_init
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def login_success(sender,request,user, **kwargs):
    print('__________________________________')
    print('user logged in----signal')
    print('sender:',sender)
    print('request:',request)
    print('user:',user)
    print(f'kwargs:{kwargs}')

@receiver(user_logged_out, sender=User)
def log_out(sender,request,user, **kwargs):
    print('__________________________________')
    print('user logged out----good bye')
    print('sender:',sender)
    print('request:',request)
    print('user:',user)
    print(f'kwargs:{kwargs}')

@receiver(user_login_failed)
def login_failed(sender,request,credentials, **kwargs):
    print('__________________________________')
    print('user login failed----error')
    print('sender:',sender)
    print('request:',request)
    print('credentials:',credentials)
    print(f'kwargs:{kwargs}')

@receiver(pre_save,sender=User)
def before_save(sender,instance, **kwargs):
    print('__________________________________')
    print('pre save signal called')
    print('sender:',sender)
    print('instance:',instance)
    print(f'kwargs:{kwargs}')

@receiver(post_save,sender=User)
def login_failed(sender,instance,created, **kwargs):
    if created:
        print('__________________________________')
        print('post save signal called')
        print('new record')
        print('sender:',sender)
        print('instance:',instance)
        print('created',created)
        print(f'kwargs:{kwargs}')
    else:
        print('__________________________________')
        print('post save signal called')
        print('updated record')
        print('sender:', sender)
        print('instance:', instance)
        print('created', created)
        print(f'kwargs:{kwargs}')

@receiver(pre_delete,sender=User)
def before_delete(sender,instance, **kwargs):
    print('__________________________________')
    print('before delete signal called')
    print('sender:',sender)
    print('instance:',instance)
    print(f'kwargs:{kwargs}')

@receiver(post_delete,sender=User)
def after_delete(sender,instance, **kwargs):
    print('__________________________________')
    print('after delete signal called')
    print('sender:',sender)
    print('instance:',instance)
    print(f'kwargs:{kwargs}')

@receiver(pre_init,sender=User)
def before_init(sender,*args, **kwargs):
    print('__________________________________')
    print('befor init')
    print('sender:',sender)
    print(f'args: {args}')
    print(f'kwargs:{kwargs}')

@receiver(post_init,sender=User)
def after_init(sender,*args, **kwargs):
    print('__________________________________')
    print('befor init')
    print('sender:',sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')

#user_logged_in.connect(login_success,sender=User)