$('#btn-form-save').on('click',function(e){
  e.preventDefault();
// console.log ('button save click')
output=''
let sid = $('#stuid').val() // coming from hidden 

let m_firstname = $('#id_first_name').val()
let m_lastname  = $('#id_last_name').val()

// var m_photo = $('#id-photo').prop('files')[0];
// let m_photo = $('#id-photo')[0]
var m_photo = document.getElementById("id-photo").files[0];


let m_designation   = $('#id_designation').val()

let m_email  = $('#id_email_address').val()
let m_phone  = $('#id_phone_number').val()
let m_department  = $('#id_department').val()

// console.log('mfirstname ', m_firstname)
// console.log('lastname ', m_lastname)
// console.log('photo ', m_photo)
// console.log('designation ', m_designation)
// console.log('email ', m_email)
// console.log('phone ', m_phone)
// console.log('department ', m_department)

var csrf_token = $('input[name=csrfmiddlewaretoken]').val()


mythis = $(this)
if (m_firstname==''){
  swal('Please enter firstname','required','error')
}else if(m_lastname==''){
  swal('Please enter Lastname','required','error')
} else if(m_photo==''){
  swal('Please select a Photo ','required','error')
} else  if(m_designation ==''){
  swal('Please enter designation  ','required','error')

} else if(m_email ==''){
  swal('Please enter email  ','required','error')
} else  if(m_phone==''){
  swal('Please enter phone  ','required','error')
} else  if(m_department==''){
  swal('Please enter department  ','required','error')
} else {



  // create record
  url= $(this).attr('data-url');
  mydata={
    empid:sid, // cming from hidded
    first_name : m_firstname, 
    last_name : m_lastname,
    
    designation :m_designation,
    email_address:m_email,
    phone_number : m_phone,
    department :m_department,

    'csrfmiddlewaretoken':csrf_token,
  };
  mydata.append('imagePath',file1)
  console.log(' to be passed ajax mydata', mydata)

  $.ajax({
    url : url,
    type : 'POST',
    data : mydata,

    contentType: 'multipart/form-data',
    cashe:false,
    processData:false,

    // returned whole list
    success:function(data){
      console.log('status:',data.status)
      // adding all record from list   
      x = data.emp_data
      if (data.status=='Saved'){
        console.log('sending data...')
        
        for (i=0; i<x.length; i++){
          output +='<tr id='+x[i].id+'><td>'+x[i].first_name+'</td><td>'+x[i].last_name+'</td><td>'+x[i].designation+'</td><td>'+x[i].department+'</td><td><a href="/app_hr/employee_profile/">view</a></td></tr>'
        }
        $('#tbody').html(output)
        // $('#form')[0].reset()
        document.getElementById('form').reset()
      }
    }
    
  });
}
});