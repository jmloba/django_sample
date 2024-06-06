from django.shortcuts import get_object_or_404, render
from .models import GroceryCategory, GroceryMaster
from .forms import GroceryCategory_Form, GroceryMaster_Form,SearchMaster_Form


from django.http import  JsonResponse,response
from app_accounts.utils import is_ajax
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
def sales_main(request):
  context= {}
  return render(request,'app_sales/sales_main.html', context)  
#==============
def category_entry(request):
  categories=GroceryCategory.objects.all()
  form = GroceryCategory_Form()
  context= {'categories': categories, 'form': form}
  return render(request,'app_sales/category_entry.html', context) 

@csrf_exempt
def category_add_save(request):
  if request.method == 'POST':
    form = GroceryCategory_Form(request.POST or None)
    if form.is_valid():
      sid =  request.POST.get('stuid')
      name = request.POST['name']
      if sid == '':
        s=GroceryCategory(name=name)
      else:  
        print(f'data to save id : {sid}')
        s=GroceryCategory(id=sid,name=name)
      s.save()  
      groceries = GroceryCategory.objects.values()
      grocery_data = list(groceries)
      return JsonResponse({'status':'Success','grocery_data': grocery_data})
    else :
      return JsonResponse({'status':'Failed'})
 
@csrf_exempt
def category_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    category = GroceryCategory.objects.get(pk=id)
    print(f'category to  delete : {category}')
    category.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  


@csrf_exempt
def category_edit(request) :
  if request.method == "POST":  
    id = request.POST.get("sid")
    category = GroceryCategory.objects.get(pk=id)
    categ_data = {'status':'Success','id':category.id, 'name': category.name}
    return JsonResponse(categ_data)
  else:
    categ_data = {'status':'Failed'}
    return JsonResponse(categ_data)
#==============
def grocery_master_entry(request):
  grocery_master=GroceryMaster.objects.all()
  
  form = GroceryMaster_Form()
  searchform = SearchMaster_Form()

  if request.method=='POST':
    searchform = SearchMaster_Form(request.POST or None)
    grocery_master=GroceryMaster.objects.filter(description__icontains=searchform['description'].value())          

  context= {'grocery_master': grocery_master, 
              'form': form, 'searchform':searchform}
    
  return render(request,'app_sales/grocery_master_entry.html', context) 



def grocerymaster_save_entryxxx(request):
  if request.method == 'POST':
    form = GroceryMaster_Form(request.POST or None)
  
    if form.is_valid():
      sid =  request.POST.get('stuid')
      item_no     = request.POST['item_no'] 
      description = request.POST['description'] 
      costprice   = request.POST['costprice'] 
      saleprice   = request.POST['saleprice'] 

      print(f' sid is : {sid}')

      if sid == '':
        s=GroceryMaster(
          item_no=item_no, 
          description=description, 
          costprice=costprice, 
          saleprice=saleprice 
          )
      else:  
        s=GroceryMaster(
          id=sid,
          item_no=item_no, 
          description=description,
          costprice=costprice, 
          saleprice=saleprice
          )
      s.save()  
      
      grocerymaster = GroceryMaster.objects.values()
      grocerymaster_data = list(grocerymaster)
      return JsonResponse(
        {'status':'Success',
         'grocerymaster_data': grocerymaster_data}
         )
    else :
      print('form is not valid ')
      return JsonResponse({'status':'Failed'})

def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

def grocerymaster_save_entry(request):
  if request.method == 'POST':
    form = GroceryMaster_Form(request.POST or None)
  
    if form.is_valid():
      sid =  request.POST.get('stuid')
      item_no     = request.POST['item_no'] 
      description = request.POST['description'] 
      costprice   = request.POST['costprice'] 
      saleprice   = request.POST['saleprice'] 
      if sid == '':
        try:
          go =  GroceryMaster.objects.get(item_no=item_no)
          return JsonResponse({'status':'record exist'})
        except  GroceryMaster.DoesNotExist:
          go = None
        s=GroceryMaster(
          item_no=item_no, 
          description=description, 
          costprice=costprice, 
          saleprice=saleprice 
          )
      else:  
        s=GroceryMaster(
          id=sid,
          item_no=item_no, 
          description=description,
          costprice=costprice, 
          saleprice=saleprice
          )
        
      s.save()  
      
      grocerymaster = GroceryMaster.objects.values()
      grocerymaster_data = list(grocerymaster)
      return JsonResponse(
        {'status':'Success',
         'grocerymaster_data': grocerymaster_data}
         )
    else :
      print('form is not valid ')
      return JsonResponse({'status':'Failed'})



def grocery_master_edit(request) :
  if request.method == "POST":  
    id = request.POST.get("sid")
    gmaster = GroceryMaster.objects.get(pk=id)

    master_data = {'status':'Success','id':gmaster.id, 'item_no': gmaster.item_no, 'description':gmaster.description, 'costprice': gmaster.costprice, 'saleprice': gmaster.saleprice
                   
                   }
    return JsonResponse(master_data)
  else:
    master_data = {'status':'Failed'}
    return JsonResponse(master_data)

def grocery_delete(request):
  if request.method == "POST":  
    id = request.POST.get("sid")
    gmaster = GroceryMaster.objects.get(pk=id)
    print(f'gmaster to  delete : {gmaster}')
    gmaster.delete()
    return JsonResponse({"status": 1})
  else:
    return JsonResponse({"status": 0})  
  



    






  
