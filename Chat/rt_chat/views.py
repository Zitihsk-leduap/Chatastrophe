from django.shortcuts import render,get_object_or_404
from .models import ChatGroup,GroupMessage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def chat_view(request):
  chat_group= get_object_or_404(ChatGroup,group_name="All-Chat")
  chat_messages = chat_group.chat_messages.all()[:20]
  print(chat_messages)
  return render(request,'rt_chat/chat.html',{'chat_messages':chat_messages})