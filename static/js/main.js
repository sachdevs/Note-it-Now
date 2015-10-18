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

function gen() {
    var elements = [
        {
            name: 'picture',
            tags: ['hi', 'hello']
        },{
            name: 'another picture',
            tags: ['cat', 'dog']
        },
    ];
    var $container = $('hi');
    $(elements).each(function(index, item){
        var name = item['name'];
        var tags = item['tags'].join(', ');
        console.log(name);
        console.log(tags);
        document.getElementById('hi').innerHTML += '<div class="entry"><h1>' + name + '</h1><p>tags: ' + tags + '</p></div>';
    });
}

function expand() {
    console.log('expand box');
}
