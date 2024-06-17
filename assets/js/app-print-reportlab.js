
$(document).ready(function(){
  
  $("#btn-reportlab-create-password").click(function(e){
    e.preventDefault();

    console.log('reportlab create password')
    let url= $(this).attr('data-url');

    var csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    let name_pass = 'joven'
    mydata= {
      'name_pass':name_pass,
      // 'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      method :'GET',

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

