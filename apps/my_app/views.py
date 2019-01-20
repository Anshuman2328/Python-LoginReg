from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def main(request):
    return render(request, 'my_app/index.html')

def register(request):
    if request.method=='POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/my_app/')
        else:
            hashedpw = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt())
            just_registered = User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email=request.POST['email'], password=hashedpw.decode())
            request.session['username'] = just_registered.fname
            request.session['user_id'] = just_registered.id
    return redirect('/my_app/success')

def login(request):
    if request.method=='POST':
        user_logging_in = User.objects.filter(email=request.POST['lemail'])
        if len(user_logging_in) == 0:
            messages.error(request, "No matching user")
        elif not bcrypt.checkpw(request.POST['lpwd'].encode(), user_logging_in[0].password.encode()):
            messages.error(request, "Passwords do not match")
        else:
            request.session['username'] = user_logging_in[0].fname
            request.session['user_id'] = user_logging_in[0].id
            messages.error(request,'Successfully logged in ')
    return redirect('/my_app/success')

def success(request):   

	context = {
        'user': User.objects.get(id=request.session['user_id']),
        
        }
	return render(request, 'my_app/display.html', context)



































    
# 	msgs = User.objects.loginValidator(request.POST)
        # try to get the user out of the db based on the email submitted

    # if User.objects.get(id=request.session['logged_in']) == User.objects.last():
	# 	status = "registered"
	# else:
	# 	status = "logged in"
#     if len(msgs):
#         # print msgs
# 	else:
# 		user = User.objects.get(email=request.POST['login_email'])
# 		request.session['logged_in'] = user.id
# 		return redirect('/my_app/display')
	
# 	return redirect('/')
        # no matching users
#     User.objects.create(fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'])
# return redirect('/')

        # user = User.objects.last()
        # request.session['logged_in'] = user.id
        # print request.session['logged_in']


# Create your views here.
# def update(request, id):
#     # pass the post data to the method we wrote and save the response in a variable called errors
#     errors = Blog.objects.basic_validator(request.POST)
#         # check if the errors object has anything in it
#         if len(errors):
#             # if the errors object contains anything, loop through each key-value pair and make a flash message
#             for key, value in errors.items():
#                 messages.error(request, value)
#             # redirect the user back to the form to fix the errors
#             return redirect('/blog/edit/'+id)
#         else:
#             # if the errors object is empty, that means there were no errors!
#             # retrieve the blog to be updated, make the changes, and save
#             blog = Blog.objects.get(id = id)
#             blog.name = request.POST['name']
#             blog.desc = request.POST['desc']
#             blog.save()
#             messages.success(request, "Blog successfully updated")
#             # redirect to a success route
#             return redirect('/blogs')




    # context ={
    #     "allusers":User.objects.all(),
    #     # "fname" : request.session['fname']
    # }

    # return render(request, 'my_app/display.html', context)
