from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from ticket.models import Tickets, Employee, Departments, Comments
from ticket.forms import FormTicket
# Create your views here.

def all_tickets( request ):
	return render( request, "ticket/list.html", {})


def login_view( request ):
	if request.method == 'POST':
		#return render( request, 'hi', {})
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login the user
			user = form.get_user()
			login(request, user)
			return redirect('ticket:all_tickets')
	else:
		form = AuthenticationForm()
	return render( request, 'ticket/login.html', {'form': form})	

def list_view(request):
	data = Tickets.objects.all()
	return render(request, 'ticket/list.html', {'data':data})


def info_view(request):
	data = Tickets.objects.get(pk=1)
	return render(request, 'ticket/info.html', {'data':data})

def add_ticket_view(request):
	if request.method == 'POST':
		form = FormTicket(request.POST)
		if form.is_valid():
			#form_items = form.save(commit=False)
			#form_items.save()
			subject = request.POST.get('subject')
			description = request.POST.get('description')
			status = request.POST.get('status')
			priority = request.POST.get('priority')
			ticket_owner = request.POST.get('ticket_owner')
			assign_to = request.POST.get('assign_to')
			ticket_owner_name = Employee.objects.get(id=ticket_owner)
			assing_name = Employee.objects.get(id=assign_to)
			print (ticket_owner_name)
			ticket_obj = Tickets(subject=subject, description=description, status=status, priority=priority, ticket_owner=ticket_owner_name, assigned_to=assing_name)
			ticket_obj.save()
			return redirect('ticket:add_ticket')
	else:
		form = FormTicket()
	return render(request, 'ticket/ticket_form.html', {'form': form})