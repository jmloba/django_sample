
  console.log('hello world')
  const helloWorldBox = document.getElementById('hello-world')
  helloWorldBox.innerHTML='hello <b>World</b>  '

  $.ajax({
    type : 'GET',
    url : '/app_posts/hello-world/',
    
    success : function(response){
      // console.log('success :',response.text)
      $('#hello-world').html(response.text)
    },
    error :function(error){
    console.log('error',error)
      }
  });

  // $.ajax({
  //   type : 'GET',
  //   url : '/app_posts/load-post-data/',  
  //   success : function(response){
      
      
  //   },
  //   error :function(error){
  //   console.log('error',error)
  //     },

  // });
