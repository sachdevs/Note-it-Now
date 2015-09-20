var buttonOptions = {
    success: function(files) {
        onFiles(files);
    },
    multiselect: true,
    extensions: ['.jpg', '.png']
};
var button = Dropbox.createChooseButton(buttonOptions);
$("#container").append(button);

function onFiles(files) {
    var payload = [];
    for(var i = 0; i < files.length; i++)
        payload.push(files[i].link);
    $.ajax({
        type: "POST",
        url: "http://localhost:5000/files",
        data: payload,
        success: function(res){
        	window.location.assign("http://localhost:5000/main");
        },
        dataType: "json"
    });
}
