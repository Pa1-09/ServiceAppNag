from django.shortcuts import render
from django.http import HttpResponse
from .models import Representative
from .models import Customer
from .forms import CustomerForm
from datetime import datetime as dt
import os

import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# to send attachment
from email.mime.base import MIMEBase
from email import encoders




# Create your views here.

filepath = r"D:\\Coding\\Django\\NagOrder_Intake\\files_folder"

def OrderForm(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        # print(form)
        if form.is_valid():                     
            form.save()

            process_data(request)  

    form = CustomerForm()

    context = {"form":form} 
        
 
    return render(request, "Orders/order_form.html", context=context)


def process_data(request):
    cust_obj = Customer.objects.all()

    d ={}
 
    
    for cust in cust_obj:

        current_date = str(dt.now()).split()[0]

        refined_date = str(cust.date).split()[0]
     

        if refined_date == current_date :
            

        # print(cust.date, type(cust.date))
            dummy_data =  cust.products_data.replace("\r","")
            d[cust.name] = dummy_data
           


        # writing to the files
        filename ="file_"+current_date + ".txt"
        os.chdir(filepath)
        if os.path.exists(filename):
            with open(filename, "a") as fa:
                fa.write("\n"+cust.name + 3*"\n")
                fa.write(d[cust.name]+"\n")
        else:
            with open(filename, "w") as fw:
                fw.write("\n"+cust.name + "\n")
                fw.write(d[cust.name]+"\n")


    subject = f"Orders for today {current_date}"
    msg_body = f"Please find complete orders for today"


    send_mail_attachment(subject=subject, msg_body=msg_body, filename=filename)

# sending mail with attachment
def send_mail_attachment(subject, msg_body, filename):
    os.chdir(filepath)
    port = 587
    host="smtp.gmail.com"

    sender = "vic34india@gmail.com"
    password = "osihcdmuetkiwzen"
    receiver = "vic34india@gmail.com"

    msg = MIMEMultipart()
    msg['From']= sender
    msg['To'] = receiver
    msg['Subject']=subject

    msg.attach(MIMEText(msg_body))

    # attaching text file
    filename = filename
    
    with open(filename, "rb") as attachment:     
        p=MIMEBase("application", "octet-stream")   
        p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    msg= msg.as_string()



    try:
        with sm.SMTP(host,port) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(sender,password)

            connection.sendmail(sender, receiver, msg)
            connection.quit()

    except TimeoutError:
        print("Time out error")






        


        
        



    