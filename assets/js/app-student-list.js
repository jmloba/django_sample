$(document).ready(function(){
  const alertBox = document.getElementById('alert-box')
  const form = document.getElementById('course-form');
  const handleAlerts =(type, text)=>{
    alertBox.innerHTML=`<div class="alert alert-${type}" role="alert"> ${text}</div>`
    }
  let clear_data_entries=() =>{
    $('#id_name').val('')
    }

  $('#btn-create-course').click(function(e){
      e.preventDefault();    
      console.log('create-course pressed')
      let html_template=''
      let id = $('#hidden-course-id').val()
      mythis = $(this)

      let course_name = $('#id_name').val()
      let url= $(this).attr('data-url'); //app_student:course-save
      let csrf_token = $('input[name=csrfmiddlewaretoken]').val()
      if (course_name ==''){
          swal('Please enter Name','Category name is required ','error')        } 
      else {
        mydata = {'csrfmiddlewaretoken':csrf_token,'h_course_uid':id, name:course_name}
        $.ajax({
          url: url,
          method : 'POST',
          data : mydata,
          success: function(data){
            x = data.course_data
            console.log('** passed list from view')
            console.log('list :',x)
            if (data.status=='Success'){
              swal('Data has been Saved','Record saved','success')
              for ( i=0; i < x.length; i++ ){
                html_template += '<tr  id="course-rec-id-'+x[i].id+'"><th scope="row">'+x[i].name+'</th><td><button class="btn btn-info btn-sm" data-sid="'+x[i].id+'" id="btn-course-edit" data-url="/app_student/course-edit/"><i class="bi bi-pencil"></i></button> &ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm"data-sid="'+x[i].id+'" id="btn-course-delete" data-url="/app_student/course-delete/"><i class="bi bi-trash3"></i></button></td></tr>'
              }
              
              $('#tbody').html(html_template)        
              $('#course-form')[0].reset()

            }
          }
        })
      }
  });  
  $('#tbody').on('click','#btn-course-delete', function(e){
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
  $('#tbody').on('click','#btn-course-edit', function(e){  
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
       $('#hidden-course-id').val(data.id)
       $('#id_name').val(data.name)
  
      }
    });

  
  

  });


  $('#btn-create-stud').click(function(e){
    e.preventDefault();    
    console.log('create-student pressed')
    let html_template=''
    let id = $('#hidden-stud-id').val()
    mythis = $(this)

    let firstname = $('#id_firstname').val()
    let lastname = $('#id_lastname').val()
    let email = $('#id_email').val()
    let course = $('#id_course').val()

    console.log('firstname  :'+ firstname)
    console.log('lastname  :'+ lastname)
    console.log('email  :'+ email)
    console.log('course  :'+ course)
    let url= $(this).attr('data-url'); //app_student:student-save
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val()

    
    if (firstname ==''){
        swal('Please enter FirstName','Firstname name is required ','error')        } 
    else if (lastname ==''){
      swal('Please enter LastName','lastname name is required ','error')        } 
    else  if (!$('#id_course').val()){
        swal('Course Value is empty' , 'please select course','danger')
      } 
    else if (email ==''){
      swal('Please enter Email','Emmail is required ','error')        } 
    else {      
      mydata = {'csrfmiddlewaretoken':csrf_token,'hidden-stud-id':id, 'firstname':firstname, 'lastname': lastname, 'email':email, 'course':course}
      $.ajax({
        url: url,
        method : 'POST',
        data : mydata,
          success: function(data){
            x = data.student_data
            console.log('** passed list from view')
            console.log('list :',x)
            if (data.status=='Success'){
              swal('Data has been Saved','Record saved','success')
              for ( i=0; i < x.length; i++ ){
                html_template += '</tr><tr id="student-rec-id-'+x[i].id+'"><th scope="row">'+x[i].firstname+'</th><th >'+x[i].lastname+'</th><th >'+x[i].course__name+'</th><th >'+x[i].email+'</th><td><button class="btn btn-info btn-sm"data-sid="'+x[i].id+'" id="btn-student-edit" data-url="/app_student/student-edit/"><i class="bi bi-pencil"></i></button>&ensp;&ensp;&ensp;<button class="btn btn-danger btn-sm" data-sid="'+x[i].id+'" id="btn-student-delete" data-url="/app_student/student-delete/"><i class="bi bi-trash3"></i></button></td></tr>'
              }
              
              $('#tbody-student').html(html_template)        
              $('#student-form')[0].reset()

            }
          }
        
      })
    } 
      
  });

  $('#tbody-student').on('click','#btn-student-delete', function(e){
    e.preventDefault()
    console.log('btn pressed delete student')

      
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

  $('#tbody-student').on('click','#btn-student-edit', function(e){  
    e.preventDefault();
    console.log('*** button edit')
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
      success: function(data){


        $('#hidden-stud-id').val(data.sid)
        $('#id_firstname').val(data.firstname)       
        $('#id_lastname').val(data.lastname)
        $('#id_email').val(data.email)
        console.log('course '+data.course)
        


      }
    });
 
  });


});