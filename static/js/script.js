$(document).ready(function(){
  /**
  * Convert an image
  * to a base64 url
  * @param  {String}   url
  * @param  {Function} callback
  * @param  {String}   [outputFormat=image/png]
    */

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
          url: 'http://localhost:5000/upload',
          data: {
            "image":b64
          },
          success: function(){
            console.log("sent data");
          },
          error: function(e){
            console.log("error"+e);
          },
          timeout:15000
        });
      };
      reader.readAsBinaryString(file);
    }
  }

  $('#uploadbutton').click(function(e){
    console.log("got click");
    uploadPhoto();
  });
});

