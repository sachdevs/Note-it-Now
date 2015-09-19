var AppRouter = Backbone.Router.extend({
    routes: {
        "": "home",
        
    },
    initialize: function() {
      
    },
    home: function() {
      if (!window.hasOwnProperty('noteView')) {
        window.noteView = new NoteView();
      }
    }
});

app = new AppRouter();
Backbone.history.start();
