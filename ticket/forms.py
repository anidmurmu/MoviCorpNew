from django import forms
from .models import Tickets, Employee, Departments, Comments

class FormTicket(forms.ModelForm):
	subject = forms.CharField(required=True, max_length=350)
	description = forms.CharField(widget=forms.Textarea(), required=True)
	STATUS_CHOICES = (
			('open','OPEN'),
			('closed', 'CLOSED'),
			('fixed', 'FIXED'),
			('in_progress', 'IN PROGRESS'),
			('reopened','REOPENED')
		)
	status = forms.ChoiceField(choices=STATUS_CHOICES)

	PRIORITY_CHOICES = (
			('low', 'LOW'),
			('medium', 'MEDIUM'),
			('high', 'HIGH'),
			('critical', 'CRITICAL')
		)
	priority = forms.ChoiceField(choices=PRIORITY_CHOICES)

	#department = forms.ModelChoiceField(queryset=Departments.objects.values_list('name', flat=True))
	#department_id = forms.ChoiceField(required=False, widget=forms.Select())
	ticket_owner = forms.ModelChoiceField(queryset=Employee.objects.all())
	assign_to = forms.ModelChoiceField(queryset=Employee.objects.all())

	class Meta:
		model = Tickets
		fields = ('subject', 'description', 'status', 'priority','ticket_owner', 'assign_to' )

	# def __init__(self, *args, **kwargs):
	# 	super(FormTicket, self).__init__(*args, **kwargs)
	# 	self.fields['department'].choices = [(x.pk, x.name) for x in Departments.objects.all()]

class DepartmentForm(forms.Form):
    department = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['department'].choices = [(x.pk, x.get_full_name()) for x in Departments.objects.all()]

class FormComment(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(), required=False)
	emp_id = forms.ModelChoiceField(queryset=Employee.objects.all())

	class Meta:
		model  = Comments
		fields = ('comment',)
	