$(document).ready(function(){
  /**
  * Convert an image
  * to a base64 url
  * @param  {String}   url
  * @param  {Function} callback
  * @param  {String}   [outputFormat=image/png]
    */
  function gen(elements) {
    elements = JSON.parse(elements);
    var $container = $('hi');
    $(elements).each(function(index,item){
      console.log(item);
      document.getElementById('hi').innerHTML += '<div class="entry"><img class="gen-image" src="'+item+'"/></div>';
    });
  }

  function expand() {
    console.log('expand box');
  }
  function uploadPhoto(){
    var b64;
    var file = $("#uploadform")[0].files[0];
    if (file) {
      var reader = new FileReader();
      reader.onload = function(readerEvt) {
        var binaryString = readerEvt.target.result;
        b64 = btoa(binaryString);
        console.log(b64);
        $.ajax({
          type: "POST",
          url: '/upload',
          data: {
            "image":b64
          },
          success: function(e){
            console.log("success");
            gen(e);
          },
          error: function(e){
            console.log("error",e);
          },
          timeout:15000
        });
      };
      reader.readAsBinaryString(file);
    }
  }

  $('#submitButton').click(function(e){
    console.log("got click");
    uploadPhoto();
  });
});

