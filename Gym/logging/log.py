from django.utils import timezone 

def loging(username,request,action):
    now = timezone.now() 
    if action == 'login' or 'register':
        f = open('auth.log','a+')
        f.write('%s,%s,%s\n'%(username,now,action))
        f.close()
    if action == 'action':
        f = open('action.log','a+')
        f.write('%s,%s,%s\n'%(username,now,action))
        f.close()    
    print('DONE')