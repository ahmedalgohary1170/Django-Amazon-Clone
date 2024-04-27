from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import SignupForm,UserActivateForm
from .models import Profile 
from products.models import Product,Brand,Review
from orders.models import Order


# Create your views here.
def signup(request):

    # if request.user.is_authenticated:
    #     return redirect('/')



    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save(commit = False)
            user.is_active = False

            form.save()

            profile = Profile.objects.get(user__username=username)

            send_mail(
                "Activate Your Account ",
                f"Welcome {username}/nUse This Code {profile.code} To Activate Your Account",
                "ahmedalgohary1170@gmail.com",
                [email],
                fail_silently=False,
              
            )

            return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form':form})






def user_activate(request,username):


    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code ==profile.code:
                profile.code = ''
                user = User.objects.get(username=username)

                user.is_active = True

                
                user.save()
                profile.save()
                

                return redirect('/accounts/login')

    else:
        form = UserActivateForm()
    return render(request,'accounts/activate.html',{'form':form})

def dashboard(request):
    users = User.objects.all().count()
    products = Product.objects.all().count()
    reviews =  Review.objects.all().count()
    orders = Order.objects.all().count()
    brands = Brand.objects.all().count()
    return render(request,"accounts/dashboard.html",{
        "users":users,
        "products":products,
        "reviews":reviews,
        "orders":orders,
        "brands":brands
    })