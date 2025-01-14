from django.shortcuts import render,get_object_or_404,redirect
from .models import ChatGroup,GroupMessage
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required
def chat_view(request):
  chat_group= get_object_or_404(ChatGroup,group_name="All-Chat")
  chat_messages = chat_group.chat_messages.all()[:20]
  form=ChatMessageCreateForm()

  if request.htmx:
    form=ChatMessageCreateForm(request.POST)
    if form.is_valid():
      message=form.save(commit=False)
      message.author=request.user
      message.group=chat_group
      message.save()
      context ={
        'message':message,
        'user':request.user
        
      }
      
      return render(request,'rt_chat/partials/chat_message_p.html',context)

  print(chat_messages)
  return render(request,'rt_chat/chat.html',{'chat_messages':chat_messages,'form':form})