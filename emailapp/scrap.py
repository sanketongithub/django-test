def home(request):

   send_to = request.POST["email_to"]  

   message = request.POST["email_body"]

   hdr = Emailheader.objects.all()

   fdr = Emailfooter.objects.all()

   #msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
   
   #msg_html = render_to_string('email.html',{'var1':'sanket'})

   #msg_html = render_to_string("email.html",{'headers' : hdr,'footers' : fdr , 'to' : send_to , 'message' : message})

   msg_plain = 'this is plain message'

   subject = 'Subject'
   html_message = render_to_string("header.html",{'headers' : hdr,'footers' : fdr , 'to' : send_to , 'message' : message})
   plain_message = strip_tags(msg_plain)
   from_email = 'From <from@example.com>'
   to = 'to@example.com'

   mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)



    subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
      text_content = 'This is an important message.'
      html_content = '<p>This is an <strong>important</strong> message.</p>'
      msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
      msg.attach_alternative(html_content, "text/html")
      msg.send()
   

   return


   '''subject, from_email, to = 'hello', 'from@example.com', send_to
            text_content = 'This is an important message.'
            html_content = render_to_string("email.html",{'headers' : hdr,'footers' : fdr , 'to' : send_to , 'message' : message})
      
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.content_subtype = "html"
            msg.attach_alternative(html_content, "text/html")
      
   
            fd = open('manage.py', 'r')
            msg.attach(file_root/file_name, fd.read(), 'text/plain')'''