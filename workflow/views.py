from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Message
from .forms import MessageForm
from .models import WorkflowManager
from django.shortcuts import render
from account.models import CustomUser
from django.http import HttpResponseRedirect

class MessageListView(View):
    model = Message
    template_name = 'workflow/workflow.html'

    def get(self, request, *args, **kwargs):
        context = {}
        manager = WorkflowManager()
        context['inbox'] = manager.inbox(self.request.user)
        context['sent'] = manager.sent(self.request.user)
        context['unread_count'] = manager.inbox_unread_count(self.request.user)
        context['users'] = CustomUser.objects.all()
        print(context['users'])

        return render(request, self.template_name, context)

    def get_context(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)

        manager = WorkflowManager()
        context['inbox'] = manager.inbox(self.request.user)
        print(context['inbox'], "that's all we got")
        context['sent'] = manager.sent(self.request.user)
        context['unread_count'] = manager.inbox_unread_count(self.request.user)

        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        # instance.sender = self.request.user.email
        instance.save()


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'workflow/workflow.html'

    def get(self, request, *args, **kwargs):
        context = {}
        manager = WorkflowManager()
        context['inbox'] = manager.inbox(self.request.user)
        context['sent'] = manager.sent(self.request.user)
        context['unread_count'] = manager.inbox_unread_count(self.request.user)
        context['users'] = CustomUser.objects.all()
        print(context['users'])

        return render(request, self.template_name, context)

    def get_context(self, **kwargs):
        context = super(MessageCreateView, self).get_context_data(**kwargs)

        manager = WorkflowManager()
        context['inbox'] = manager.inbox(self.request.user)
        print(context['inbox'], "that's all we got")
        context['sent'] = manager.sent(self.request.user)
        context['unread_count'] = manager.inbox_unread_count(self.request.user)

        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.sender = self.request.user
        instance.save()

        return HttpResponseRedirect("/workflow/")
