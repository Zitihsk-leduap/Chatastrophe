from django.shortcuts import render
from .forms import *
from allauth.account.utils import send_email_confirmation
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.



def profile_view(request,username=None):
  if username:
    profile=get_object_or_404(User,username=username).profile
  else:
    try:

      profile=request.user.profile
    except:
      return redirect('account_login')
  return render(request,'Users/profile.html',{'profile':profile})


@login_required
def profile_edit_view(request):
  form = ProfileForm(instance=request.user.profile)

  if request.method=='POST':
    form=ProfileForm(request.POST,request.FILES,instance=request.user.profile)
    if form.is_valid():
      form.save()
      return redirect('profile')
  return render(request,'Users/profile_edit.html',{'form':form})


@login_required
def settings_view(request):
  return render(request,'Users/settings.html')



def profile_emailchange(request):

  if request.htmx:
    form=EmailForm(instance=request.user)
    return render(request,'partials/email_form.html',{'form':form})
  
  if request.method=='POST':
    form=EmailForm(request.POST,instance=request.user)
    
    if form.is_valid():
      #check if the email exist already
      email=form.cleaned_data['email']
      if User.objects.filter(email=email).exclude(id=request.user.id).exists():
        messages.warning(request,f'{email} is already in use.')
        return redirect('settings')
      
      form.save()


      send_email_confirmation(request,request.user)

      return redirect('settings')




  return redirect('home')


@login_required
def profile_email_verify(request):
  send_email_confirmation(request,request.user)
  return redirect('settings')


@login_required
def account_delete(request):
  user=request.user
  if request.method=='POST':
    logout(request)
    
    user.delete()
    return redirect('home')



  return render(request,'Users/account_delete.html')