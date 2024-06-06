$(document).ready(function(){

  const alertBox = document.getElementById('alert-box')
  const form = document.getElementById('grocery-master-form');
  const handleAlerts =(type, text)=>{
    alertBox.innerHTML=`<div class="alert alert-${type}" role="alert"> ${text}</div>`
  }
  let clear_data_entries=() =>{
    $('#stuid').val('')
    $('#id_description').val('')
    $('#id_item_no').val('')
    $('#id_costprice').val('')
    $('#id_saleprice').val('')
    
  }  

$('#btn-create-mastergrocery').click(function(e){
  e.preventDefault();
  console.log('create master clicked')

  let html_template=''
  let id = $('#stuid').val()  
  let item_no = $('#id_item_no').val()
  let description = $('#id_description').val()
  let costprice = $('#id_costprice').val()
  let saleprice = $('#id_saleprice').val()

  let url= $(this).attr('data-url');
  let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  mythis = $(this)
  mydata={}
  if (item_no ==''){
    swal('Please enter Itemnumber','Itemnumber is required ','error')
  } else  if (description ==''){
    swal('Please enter Description','description is required ','error')
  } else if (costprice<=0) {
    swal('Please enter Costprice','costprice should be > 0 ','error')
    
  } else if (saleprice<=0) {
    swal('Please enter saleprice','saleprice should be > 0 ','error')
  } else {

    mydata = {'csrfmiddlewaretoken':csrf_token,
    'stuid':id, 
    'item_no':item_no,
    'description':description,
    'costprice': costprice,
    'saleprice': saleprice

    }
    $.ajax({
      url: url,
      method : 'POST',
      data : mydata,
      success: function(data){    
        x = data.grocerymaster_data
        if (data.status=='record exist'){
          swal('Duplicate REcord','Record is not saved','info')
        }


        if (data.status=='Success'){
          swal('Data has been Saved','Record saved','success')

          for ( i=0; i < x.length; i++ ){
            html_template += ' <tr id="categ-id-'+x[i].item_no+'"><th>'+x[i].item_no+'</th><td>'+x[i].description+'</td> <td>'+x[i].costprice+'</td><td>'+x[i].saleprice+'</td><td><button class="btn btn-info btn-sm" data-sid="'+x[i].id+'" id="btn-grocery-edit" data-url="/app_sales/grocery-master-edit/"><i class="bi bi-pencil"></i></button> &ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm" data-sid="'+x[i].id+'" id="btn-grocery-delete" data-url="/app_sales/grocery-delete/"><i class="bi bi-trash3"></i></button></td></tr>'
          };
          $('#tbody').html(html_template)        
          $('#grocery-master-form')[0].reset()
          clear_data_entries()      
        }


      },
    
    });   
  } 
});  


$('#tbody').on('click','#btn-grocery-delete', function(e){
  e.preventDefault()
    
  let id = $(this).attr("data-sid")
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
  console.log ('id is   : ', id)
  mydata= {
    'sid':id ,
    'csrfmiddlewaretoken':csrf_token,
  }
  mythis = $(this)
  console.log ('mydata   : ', mydata)
  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    success:function(data){
      console.log(data)
      if (data.status==1){
        console.log('Item  deleted')
        $(mythis).closest("tr").fadeOut()
          // swal(response.status,response.message,'success')
        }
      if (data.status==0) {
          console.log('student --- unable to deleted')

        }
    },
    
  })
  


});

$('#tbody').on('click','#btn-grocery-edit', function(e){  
  e.preventDefault();
  let id = $(this).attr("data-sid")
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
    mydata= {
    'sid':id ,
    'csrfmiddlewaretoken':csrf_token,
  }
  mythis = $(this)
  console.log ('mydata   : ', mydata)
  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    success: function(data){
    $('#stuid').val(data.id)      
    $('#id_item_no').val(data.item_no)
    $('#id_description').val(data.description)
    $('#id_costprice').val(data.costprice)
    $('#id_saleprice').val(data.saleprice)

    $('#id_item_no').attr("readonly") = true
    
    }
  });
 
});


});  
