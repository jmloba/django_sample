
  const alertBox = document.getElementById('alert-box')
  const imgBox = document.getElementById('img-box')
  const form = document.getElementById('p-form')

  
  const m_name =document.getElementById('id_name')
  const description  =document.getElementById('id_description')

  const image = document.getElementById('id_image')
  

  const csrf = document.getElementsByName('csrfmiddlewaretoken')

  const url = ''
  const handleAlerts =(type, text)=>{
    alertBox.innerHTML=`<div class="alert alert-${type}" role="alert">
                         ${text}
                      </div>`
  }

  image.addEventListener('change',()=>{
      const img_data = image.files[0]
      const url = URL.createObjectURL(img_data)

      console.log(url)
      imgBox.innerHTML= `<img src="${url}" width="100%">`

    });

  
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken',csrf[0].value)
    fd.append('name', m_name.value)
    fd.append('description', description.value)
    fd.append('image', image.files[0])
    $.ajax({
      type : 'POST',
      url:url,
      enctype:'multipart/form-data',
      data:fd,
      success:function(response){
        console.log(response)
        const sText = `Record successfully saved ${response.name}`
        handleAlerts('success',sText)
        setTimeout(()=>{
          // clear entries
          imgBox.innerHTML=''
          alertBox.innerHTML=''
          
          description.value=''
          image.value=''
          m_name =''
        },2000)
    

      },
      error:function(error){
        console.log(response)
        handleAlerts('danger','upps .. something went wrong')
      },
      cashe :false,
      contentType: false, 
      processData: false

    })
    

  });

  
