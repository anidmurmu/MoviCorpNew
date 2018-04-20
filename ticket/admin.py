from django.contrib import admin

# Register your models here.

from ticket.models import Comments, Tickets, Employee, Departments, DepartmentsAdmin, CommentsAdmin, TicketsAdmin, EmployeeAdmin



admin.site.register( Comments, CommentsAdmin )
admin.site.register( Tickets, TicketsAdmin )
admin.site.register(Employee, EmployeeAdmin)
admin.site.register( Departments, DepartmentsAdmin )
