const imgBox = document.getElementById('img-box')
const image = document.getElementById('id_photo')
const alertBox = document.getElementById('alert-box')

image.addEventListener('change',()=>{
  const img_data = image.files[0]
  const url = URL.createObjectURL(img_data)

  console.log(url)
  imgBox.innerHTML= `<img src="${url}" width="200px">`

});

const handleAlerts =(type, text)=>{
  
  alertBox.innerHTML=`<div class="alert alert-${type}" role="alert">
                       ${text}
                    </div>`
}


$('#btn-create-employee').on('click',function(e){
  e.preventDefault();
  

  var m_firstname = $('#id_first_name').val()
  var m_lastname = $('#id_last_name').val()
  var m_designation = $('#id_designation').val()
  var m_email = $('#id_email_address').val()
  
  var m_phone = $('#id_phone_number').val()
  var m_department = $('#id_department').val()
  let image = document.getElementById('id_photo')
  let myportfolio = document.getElementById('id_myportfolio')

  
  let csrf_token = $('input[name=csrfmiddlewaretoken]').val()

  mythis = $(this)
  url= $(this).attr('data-url');
  const fd = new FormData()
  fd.append('csrfmiddlewaretoken',csrf_token)

  fd.append('first_name',m_firstname)
  fd.append('last_name',m_lastname)

  fd.append('designation',m_designation)
  fd.append('email_address',m_email)

  fd.append('phone_number',m_phone)
  fd.append('department',m_department)

  fd.append('photo', image.files[0])
  fd.append('myportfolio',myportfolio.files[0])
  $.ajax({
    type : 'POST',
    url:url,
    contentType:false,
    processData:false,
    data:fd,
    success:function(response){
      
      const sText = `Record successfully saved ${response.first_name}`
      handleAlerts('success',sText)
      setTimeout(()=>{
        // clear entries
        imgBox.innerHTML=''
        alertBox.innerHTML=''
      },2000)
    
      html_template = ' <tr id="emp-id-'+response.id+'"><td>'+response.first_name+'</td><td>'+response.last_name+'</td><td>'+response.designation+'</td><td>'+response.department+'</td><td><a href="/app_hr/employee_profile/'+response.id+'/">view</a> &ensp;&ensp;<button class="btn btn-danger btn-sm" data-sid='+response.id+' id="btn-employee-delete" data-url="/app_hr/employee_delete/"><i class="bi bi-trash3"></i></button></td></tr>'
      
      $('#tbody').append(html_template)
      clear_data_entries()
    },
    error:function(response){
      console.log(response.error)
      handleAlerts('danger','upps .. something went wrong')
    },
    cache :false,
    contentType: false, 
    processData: false
  })
});


let clear_data_entries=() =>{
  $('#id_first_name').val('')
  $('#id_last_name').val('')
  $('#id_designation').val('')

  $('#id_email_address').val('')
  $('#id_phone_number').val('')
  $('#id_department').val('')
  $('#id_photo').val('')

}



$('#tbody').on('click','#btn-employee-delete', function(e){

  e.preventDefault();  
  let id = $(this).attr("data-sid")
  var csrf_token = $('input[name=csrfmiddlewaretoken]').val()
  url= $(this).attr('data-url');
  console.log ('id is   : ', id)

  mydata= {'sid':id ,
  'csrfmiddlewaretoken':csrf_token,}
  
  mythis = $(this)
  console.log ('mydata   : ', mydata)
  $.ajax({
    url:url,
    method :"POST",
    data : mydata,
    
    success:function(data){
      console.log(data)
      if (data.status==1){
        console.log('employee deleted')
        $(mythis).closest("tr").fadeOut()
        
          // swal(response.status,response.message,'success')
        }
        if (data.status==0)

        {
          console.log('student --- unable to deleted')
        }

    },
    
  })

})
  


