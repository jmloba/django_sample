$(document).ready(function(){

  $('#btn-print-profile').click(function(e){
    e.preventDefault();
    console.log('print profile ')
    let url= $(this).attr('data-url');
    let emp_no =$(this).attr("data-sid")
    
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    console.log(typeof(emp_no))
    console.log('Employee number  :'+emp_no)  
    
    // pass value to print_invoice_ajax  (app_print:print-invoice-ajax)
    mydata= {
      'emp_no':Math.floor(emp_no),
      'csrfmiddlewaretoken':csrf_token,
    }
    $.ajax({
      url:url,
      data : mydata,
      method :'POST',
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
