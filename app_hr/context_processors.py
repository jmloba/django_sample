from app_hr.models import Employee, Department

def get_departments(request):

  
  departments= Department.objects.all()
  return {'departments': departments}
