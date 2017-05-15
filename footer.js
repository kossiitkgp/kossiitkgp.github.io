document.write('\
     <div class="ui inverted vertical footer segment">\
        <div class="ui center aligned container">\
            <div class="ui stackable inverted divided grid">\
                <div class="three wide column">\
                    <h4 class="ui inverted header">Main Menu</h4>\
                    <div class="ui inverted link list">\
                        <a href="./index.html" class="item">Home</a>\
                        <a href="./events/index.html" class="item">Events</a>\
                        <a href="./team/index.html" class="item">Our Team</a>\
                        <a href="./projects/index.html" class="item">Projects</a>\
                    </div>\
                </div>\
                <div class="three wide column">\
                    <h4 class="ui inverted header">Contact Us</h4>\
                    <div class="ui inverted link list">\
                        <a href="https://www.facebook.com/kossiitkgp/" class="item">Facebook</a>\
                        <a href="mailto:kossiitkgp@gmail.com" class="item">kossiitkgp@gmail.com</a>\
                    </div>\
                </div>\
                <div class="three wide column">\
                    <h4 class="ui inverted header">Group 3</h4>\
                    <div class="ui inverted link list">\
                        <a href="#" class="item">Link One</a>\
                        <a href="#" class="item">Link Two</a>\
                        <a href="#" class="item">Link Three</a>\
                        <a href="#" class="item">Link Four</a>\
                    </div>\
                </div>\
                <div class="seven wide column">\
                    <h4 class="ui inverted header">Footer Header</h4>\
                    <p>Extra space for a call to action inside the footer that could help re-engage users.</p>\
                </div>\
            </div>\
            <div class="ui inverted section divider"></div>\
            ');
        if (location.pathname == "/index.html")
        {
        document.write('\
            <img src="./assets/images/kosslogo.png" class="ui centered mini image">\
            ');
       }
        else{
            document.write('\
            <img src="../assets/images/kosslogo.png" class="ui centered mini image" >\
            ');
        }
        document.write('\
            <div class="ui horizontal inverted small divided link list">\
                <a class="item" href="#">Site Map</a>\
                <a class="item" href="#">Contact Us</a>\
            </div>\
        </div>\
    </div>\
</div>\
');
