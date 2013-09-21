from django.http import HttpResponse,HttpResponseRedirect
from apps.api.models import UserProfile, Apology
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import simplejson
from apps.api.helpers import jsonp

def test(request):
    return HttpResponse('works!')

@jsonp
def signup(request):
    #sign up user
    resp = []
    status = 0
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        email = request.GET['email']
        print User.objects.filter(username=username).count()
        if User.objects.filter(username=username).count()==0:
            print 'aaaa'
            #create new user
            user = User.objects.create_user(
                username,
                email,
                password
            )
            #create acompanying user profile
            up = UserProfile.objects.create(user = user)
            #generate token
            token = up.getToken()
            #append tokent to response
            resp.append({'token':token})
            #update status
            status = 1
    else:
        #update status
        status = 2
    #append status to resp
    resp.append({'status':status})
    #return response
    return HttpResponse(
               simplejson.dumps(resp),
               mimetype='application/javascript')


@jsonp
def login(request):
    #login user
    resp = []
    status = 0
    if request.method == 'GET':
        username = request.GET['username']
        password = request.GET['password']
        #attempt authentication
        user = authenticate(
                    username = username,
                    password = password )
        if user is not None:
            #authentication success
            #retrieve user profile
            userProfile = UserProfile.objects.get(user = user)
            #get a token
            token = userProfile.getToken()
            #append token to resposne
            resp.append({'token':token})
            #update status
            status = 1
        else:
            #authenticaiton failed
            status = 2
    #append status to resp
    resp.append({'status':status})
    #return response
    return HttpResponse(
               simplejson.dumps(resp),
               mimetype='application/javascript')

        






      
