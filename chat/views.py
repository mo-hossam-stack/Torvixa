from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def chat_view(request, chatroom_name='public-chat'):
    chat_group = get_object_or_404(ChatGroup, group_name=chatroom_name)
    chat_messages = chat_group.chat_messages.all()[:30]
    return render(request, 'chat/chat.html',{'chat_messages': chat_messages})