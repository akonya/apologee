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
            up = UserProfile.objects.create(user = user, name=username)
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


@jsonp
def sorry(request):
    #submit appology
    resp = []
    status = 0
    if request.method == 'GET':
        token = request.GET['token']
        sentTo = request.GET['sendto']
        #get user profile corrisponding to token 
        up_list1 = UserProfile.objects.filter(token = token)
        #get user profile corrisponding to sendto
        up_list2 = UserProfile.objects.filter(name = sentTo) 
        #check to make sure token active
        if up_list1.count() == 1 and up_list2.count() == 1:
            #token valid
            status = 1
            up1 = up_list1[0]
            up2 = up_list2[0]
            if Apology.objects.filter(sentFrom = up1, sentTo = up2).count() == 0:
                #if apology does not exist
                #create apology
                ap1 = Apology.objects.create(sentFrom = up1, sentTo = up2)
                #check to see if appology pair exists
                ap_list = Apology.objects.filter(sentFrom = up2, sentTo = up1)
                if ap_list.count() != 0:
                    #appology pair exists
                    ap2 = ap_list[0]
                    #accept applogies
                    ap1.accept()
                    ap2.accept()
                    #update status
                    status = 3
        else:
            #token invalid
            status = 2
    #append status to resp
    resp.append({'status':status})
    #return response
    return HttpResponse(
               simplejson.dumps(resp),
               mimetype='application/javascript')

        






      
