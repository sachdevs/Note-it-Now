var NoteView = Backbone.View.extend({
    el: $('.noteView-container'),
    initialize: function() {
        this.render();
    },
    render: function() {
    },
    destroyView: function() {
        // COMPLETELY UNBIND THE VIEW
        this.undelegateEvents();
        this.$el.removeData().unbind();

        // Remove view from DOM
        this.remove();
        Backbone.View.prototype.remove.call(this);

    }
});
