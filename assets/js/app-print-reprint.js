$(document).ready(function(){

  $('#btn-reprint-button').click(function(e){
    e.preventDefault();
    
    let url= $(this).attr('data-url');
    let invoice =$(this).attr("data-invoice")
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
    console.log(typeof(invoice))
    console.log('invoice :'+invoice)  
    
    // pass value to print_invoice_ajax  (app_print:print-invoice-ajax)
    mydata= {
      'new_invoice':Math.floor(invoice),
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
