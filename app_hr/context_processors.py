from app_hr.models import Employee, Department

def get_departments(request):

  
  return {'departments': Department.objects.all()}
