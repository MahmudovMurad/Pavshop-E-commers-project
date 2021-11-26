import pywhatkit
from store.models import *
from store.views import *
from store.form import *
from store.form_views import *

def send_whatsapp_message(message, phone_number):
    try:

        pywhatkit.sendwhatmsg("+994 sizin nomreniz", "Təşəkkür edirik bizi seçdiyiniz üçün. Təklif və iradlarınızı dəstək xəttimizə bildirə bilərsiniz ", 
                                                        12, 30)
        print("Message sent successfully")


    except:
        print("Error")