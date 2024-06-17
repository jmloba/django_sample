import subprocess
from .models import Employee
from django.http import JsonResponse

from django.db.models import Sum, Q
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch,cm
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import Frame, Image
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,  Preformatted, XPreformatted 
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from .print_employee_profile_template import print_template
import io

def print_employee_profile_now(employee_data,mypath,empno,photo_url):

  print(f'\n\n ---->>>  print_employee_profile_now:\n\n {employee_data}\n mypath :{mypath}\n empno:{empno}\nphoto_url: {photo_url}')

  
  global mtotals 
  mtotals= 0.0
  y_axis = 6.0
  global  page_total 
  # buff = io.BytesIO()
  c=canvas.Canvas(mypath, pagesize=A4 )
  
  c.translate(inch, inch)  # x y position using inch  
  pageno =0
  c = print_template(c,employee_data,photo_url)  
  c.showPage()
  c.save()

  
  # to open pdf
  subprocess.Popen([mypath], shell=True)
  