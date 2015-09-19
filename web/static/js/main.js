var buttonOptions = {
    success: function(files) {
    	onFiles(files);
    },
    multiselect: true,
    extensions: ['.jpg', '.png']
};
var button = Dropbox.createChooseButton(buttonOptions);
$("#container").append(button);

function onFiles(files){
	//main (normally would do with backbone...)
}