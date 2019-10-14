from django.db.models import Q
from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.core.mail import EmailMultiAlternatives

from django.core.mail import send_mail

from django.core import mail

from django.utils.html import strip_tags

from django.template.loader import render_to_string

from .models import Emailheader, Emailfooter, EmployeesTest, Employees

from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape

from django.contrib import messages



class OrderListJson(BaseDatatableView):
    # The model we're going to show
    #emp = [emp1,emp2]
    #empl = my_employee.create("1122","ramprasad","gupta","m")


    model = Employees

    # define the columns that will be returned
    columns = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['first_name', 'last_name', 'gender', '', '']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'first_name':
            # escape HTML for security reasons
            return escape('{0} {1}'.format(row.first_name, row.last_name))
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        first_name = self.request.GET.get('first_name', None)

        if first_name:
            customer_parts = first_name.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(first_name__istartswith=part) | Q(last_name__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs

 # Create your views here.

def data_test(request):

    return render(request,'data.html')



def load_form(request):
      return render(request,'autocomp.html')



def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = MODEL.objects.filter(name__startswith=q)
        results = []
        print (q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def index(request):

      return render(request,'home.html')


def emailform(request):

    messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request,'email_form.html')

    



def funtest(request):

      return HttpResponse("testing")


def home(request):

		send_to = request.POST["email_to"]  

		message = request.POST["email_body"]

		attach = request.FILES['documents']


		#hdr = Emailheader.objects.last()
		  
		#print(hdr.img)

		#fdr = Emailfooter.objects.all()

		subject, from_email, to = 'hello', 'from@example.com', send_to
		text_content = 'This is an important message.'
      
		
		html_content = render_to_string("cotrav_email_template.html")
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.content_subtype = "html"
		msg.attach_alternative(html_content, "text/html")
		msg.attach(attach.name, attach.read(), attach.content_type)
		msg.send()
			#res = msg.send()
	   
		return render("cotrav_email_template.html")
		
     # return render(request,"email.html",{'headers' : hdr,'footers' : fdr , 'to' : send_to , 'message' : message})

      #return HttpResponse('%s'%res)



    
