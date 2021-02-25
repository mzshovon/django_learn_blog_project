from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, UserImageUpdate 
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account succesfully created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegistrationForm()
    return render(request,'user/register.html',{'form':form})

@login_required
def profile(request):

    if request.method == 'POST' :
        user_field_form = UserUpdateForm(request.POST, instance = request.user)
        user_image_update = UserImageUpdate(request.POST,
                                            request.FILES, 
                                            instance = request.user.profile)

        if user_field_form.is_valid() and user_image_update.is_valid():
            user_field_form.save()
            user_image_update.save()
            messages.success(request, f'Your profile successfully updated!')
            return redirect('profile')
        else:
            messages.warning(request, f'Wrong input fields! Try again!')
            return redirect('profile')
    else:
        user_field_form = UserUpdateForm
        user_image_update = UserImageUpdate
    context = {
        'u_form': user_field_form,
        'p_form': user_image_update
    }
    return render(request, 'user/profile.html', context)