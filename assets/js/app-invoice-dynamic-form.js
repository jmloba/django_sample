$(document).ready(function(){
  // alert('Hello')
  $('.add-item-button').click(function(e){
    e.preventDefault(); //stop page refresh
    console.log('add item clicked')
    $('#show-item').prepend(`<div class="row">
    <div class="col-md-4 mb-3">
      <input type="text" name="product_name[]" class="form-control" placeholder="item name" required >
    </div>
    <div class="col-md-3 mb-3">
      <input type="number" name="product_price[]" class="form-control" placeholder="product price" required >
    </div>                    
    <div class="col-md-3 mb-3">
      <input type="number" name="product_quantity[]" class="form-control" placeholder="quantity" required >
    </div>   
    <div class="col-md-2 mb-3 d-grid">
      <button class="btn btn-danger remove-item-button">Remove</button>
    </div>                                              
  </div>`)


  })
  $('document').on('click','.remove-item-button', function(e){
    e.preventDefault();
    let row_item = $(this).parent().parent();
    $(row_item).remove();

  })
  // ajax request to insert all data
  $('#add-form').submit(function(e){
    e.preventDefault();
    $('#add-btn').val('Adding...')


  })




})