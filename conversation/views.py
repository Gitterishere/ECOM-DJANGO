from django.shortcuts import render,get_object_or_404,redirect

from item.models import Item
from .forms import ConversationMessageForm

from .models import Conversation,ConversationMessage

def new_converastion(request,item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.created_by==request.user:
        return redirect('dashboard:index')
    conversations = Conversation.objects.filter(item = item).filter(members_in=[request.user.id])
    
    if conversations:
        pass 
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item = item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit= False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation.save()
            
            return redirect('item:detals',pk = item_pk)
    else:
        form = ConversationMessageForm()
        
    return render(request,'conversation/new.html',{
        'form':form,
    })        
            
    
    


