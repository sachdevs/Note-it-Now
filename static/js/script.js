$(document).ready(function(){
  $('.fab').click(function(e){
    $('.popup-create').toggleClass('popup-hidden');
  });
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
  var opts = {
    lines: 13 // The number of lines to draw
    , length: 28 // The length of each line
    , width: 14 // The line thickness
    , radius: 42 // The radius of the inner circle
    , scale: 1 // Scales overall size of the spinner
    , corners: 1 // Corner roundness (0..1)
    , color: '#FFF' // #rgb or #rrggbb or array of colors
    , opacity: 0.25 // Opacity of the lines
    , rotate: 0 // The rotation offset
    , direction: 1 // 1: clockwise, -1: counterclockwise
    , speed: 1 // Rounds per second
    , trail: 60 // Afterglow percentage
    , fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
    , zIndex: 2e9 // The z-index (defaults to 2000000000)
    , className: 'spinner' // The CSS class to assign to the spinner
    , top: '50%' // Top position relative to parent
    , left: '50%' // Left position relative to parent
    , shadow: false // Whether to render a shadow
    , hwaccel: false // Whether to use hardware acceleration
    , position: 'absolute' // Element positioning
  }
  function expand() {
    console.log('expand box');
  }
  function uploadPhoto(){
    var target = document.getElementById('centered-spinner')
    var spinner = new Spinner(opts).spin(target);

    var b64;
    for (var x in $("#uploadform")[0].files){
      var file = $("#uploadform")[0].files[x];
      //if (file) {
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
            spinner.stop();
          },
          error: function(e){
            console.log("error",e);
            spinner.stop();
          },
          timeout:15000
        });
      };
      reader.readAsBinaryString(file);
    }
  }

  $('#submitButton').click(function(e){
    console.log("got click");
    $('.popup-create').toggleClass('popup-hidden');
    uploadPhoto();
  });
});

