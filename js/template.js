$(document)
    .ready(function() {
        // create sidebar and attach to menu open
        $('.ui.sidebar')
            .sidebar('attach events', '.openMenu.item')
        ;

    })
;
