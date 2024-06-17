from reportlab.lib.units import inch,cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, XPreformatted
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def draw_line(c):
    # line
    c.setStrokeColorRGB(1, 0, 0)  # line color in red
    c.setLineWidth(1)  # line width
    c.line(-.5*inch, 7.3 * inch, 6.8 * inch, 7.3 * inch)  

def logo_draw(c):
    #  logo print ---
    
    c.drawImage('c:\\reportlab\\logo\\logo_red.png', -.4 * inch, 9 * inch, 1.0 * inch, 1.0 * inch)    



def set_canvas(c):
    c.translate(inch, inch)  

def draw_a4_borderrectangle(c):
    # draw the rectangle
    c.setLineWidth(2)
    c.setStrokeColor("black")
    c.setFillColor("lightgreen")
    c.roundRect(-.8 * inch, -.5 * inch, 7.9 * inch, 10.7 * inch, stroke=1, radius=.1)    

def import_date(c):
    c.setFont("Helvetica", 10)
    c.setFillColorCMYK(27, 2, 5, 3)  # font color
    from datetime import date
    inv_date = date.today().strftime('%d-%b-%Y')
    str_date = "Date"
    
    c.drawString(-.5 *inch, 7.5*inch,str_date+": "+inv_date)    


def rectangle_address(c):
    c.setLineWidth(3)
    c.setStrokeColor("lightblue")
    c.setFillColor("lightyellow")
    c.roundRect(2*inch, 8 * inch, 4.8*inch, 2.0 * inch, fill=1, stroke=1, radius=.1*inch) 


def print_data_labels(c,y_axis,employee_data)  :
  
  c.setFillColorCMYK(1,0,0,89)
  c.setFont("Helvetica", 10)

  c.drawString( -0.5  * inch, y_axis * inch, 'First Name:')
  c.drawString( 3  * inch, y_axis * inch, 'Last Name:')
  y_axis -= 0.3
  c.drawString( -0.5  * inch, y_axis * inch, 'Designation:')
  c.drawString( 3  * inch, y_axis * inch, 'Email Address:')
  y_axis -= 0.3
  c.drawString( -0.5  * inch, y_axis * inch, 'Phone Number:')
  c.drawString( 3  * inch, y_axis * inch, 'Deaprtment:')


def print_data(c,y_axis,employee_data,photo_url)  :
  
  c.setFillColor('#EE4E4E')
  c.setFont("Helvetica", 10)

  c.drawString( 1.0  * inch, y_axis * inch, employee_data[0]['first_name'])
  c.drawString( 4  * inch, y_axis * inch, employee_data[0]['last_name'])
  y_axis -= 0.3
  c.drawString( 1  * inch, y_axis * inch, employee_data[0]['designation'])
  c.drawString( 4.3  * inch, y_axis * inch,  employee_data[0]['email_address'])
  
  y_axis -= 0.3
  c.drawString( 1  * inch, y_axis * inch, employee_data[0]['phone_number'])
  c.drawString( 4.3  * inch, y_axis * inch,  employee_data[0]['department__name'])
  print(f'\n\n photo_url : {photo_url}')
  
#   c.drawImage(new_url, -.4 * inch, 9 * inch, 1.0 * inch, 1.0 * inch)    


def print_pageno(c,y_axis,pageno):    
  c.setFillColor('#C80036')
  c.setFont("Helvetica",12)
  c.drawString( 6.0*inch, y_axis * inch, 'Page No: '+str(pageno))



def print_template(c , employee_data,photo_url):

    logo_draw(c)
    draw_a4_borderrectangle(c)
    draw_line(c)
    rectangle_address(c)
    # draw_watermark(c)
    import_date(c)
    y_axis= 6.8
    print(f'\n\n\n before print data labels ')
    print_data_labels(c,y_axis,employee_data) 
    y_axis= 6.8
    print_data(c,y_axis,employee_data,photo_url) 
    y_axis -= .3
    # print_pageno(c,7.5,pageno)
    
 
    
    return c