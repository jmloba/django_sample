$(document).ready(function(){
  
  $('#btn-reportlab-password-protected').click(function(e){
    e.preventDefault();
    console.log('button password protected')
    let url= $(this).attr('data-url');
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    let pass_data = 'joven ***'
    mydata= {
      'pass_data':pass_data,
      'csrfmiddlewaretoken':csrf_token,
    }
    console.log('url is :' ,url)


    $.ajax({
      url:url,
      data : mydata,
      method:'POST',
      success:function(response){
        if (response.status=='Success'){
          swal(response.status,response.Message,'success')
        }
        if (response.status=='No Record Found') {
          swal(response.status,response.Message,'warning')

        }
      }

    })   

  });  




});  