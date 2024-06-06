$(document).ready(function(){

const alertBox = document.getElementById('alert-box')
const form = document.getElementById('category-form');
const handleAlerts =(type, text)=>{
  alertBox.innerHTML=`<div class="alert alert-${type}" role="alert"> ${text}</div>`
}
let clear_data_entries=() =>{
  $('#id_name').val('')


}

$('#btn-create-category').click(function(e){
  e.preventDefault();
  
  let html_template=''
  let id = $('#stuid').val()
  mythis = $(this)
  let name = $('#id_name').val()
  let url= $(this).attr('data-url');
  let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  if (name ==''){
    swal('Please enter Name','Category name is required ','error')
  } else {
    console.log('name : '+ name)
    mydata = {'stuid':id, name:name}
    

    $.ajax({
      url: url,
      method : 'POST',
      data : mydata,
      success: function(data){
        x = data.grocery_data
        console.log('** passed list from view')
        console.log('list :',x)
        if (data.status=='Success'){
          swal('Data has been Saved','Record saved','success')


          for ( i=0; i < x.length; i++ ){
            html_template += '<tr id="categ-id-'+x[i].id+'"><th scope="row">'+x[i].name+'</th><td><button class="btn btn-info btn-sm" data-sid="'+x[i].id+'" id="btn-category-edit" data-url="/app_sales/category_edit/"><i class="bi bi-pencil"></i></button> &ensp; &ensp; &ensp; <button class="btn btn-danger btn-sm" data-sid="'+x[i].id+'" id="btn-category-delete" data-url="/app_sales/category_delete/"><i class="bi bi-trash3"></i></button></td></tr>'


          };
          $('#tbody').html(html_template)        
          $('#category-form')[0].reset()

          
          
          clear_data_entries()          
        }
      }
    });


  } 
 
});




$('#tbody').on('click','#btn-category-delete', function(e){
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
        console.log('Category deleted')
        $(mythis).closest("tr").fadeOut()
          // swal(response.status,response.message,'success')
        }
      if (data.status==0) {
          console.log('student --- unable to deleted')

        }
    },
    
  })
  


});


$('#tbody').on('click','#btn-category-edit', function(e){  
  e.preventDefault();

  let id = $(this).attr("data-sid")
  console.log('*** button edit')
  console.log('id to edit is  :', id)
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
    success: function(data){
     $('#stuid').val(data.id)
     $('#id_name').val(data.name)

    }
  });
 
});

});