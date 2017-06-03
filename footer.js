document.write('\
     <div class="ui inverted vertical footer segment">\
        <div class="ui center aligned container">\
            <div class="ui stackable inverted divided grid">\
                <div class="four wide column">\
                    <h4 class="ui inverted header">Main Menu</h4>\
                    <div class="ui inverted link list">\
                        <a href="./index.html" class="item">Home</a>\
                        <a href="./about" class="item">About Us</a>\
                        <a href="./events" class="item">Events</a>\
                        <a href="./projects" class="item">Projects</a>\
                    </div>\
                </div>\
                <div class="four wide column">\
                    <h4 class="ui inverted header">Contact Us</h4>\
                    <div class="ui inverted link list">\
                        <a href="https://www.facebook.com/kossiitkgp/" class="item">Facebook</a>\
                        <a href="mailto:kossiitkgp@gmail.com" class="item">kossiitkgp@gmail.com</a>\
                    </div>\
                </div>\
                <div class="six wide column">\
                    <h4 class="ui inverted header">Kharagpur Open Source Society</h4>\
                    <div class="ui inverted link list"><a href="http://iitkgp.ac.in" target="_blank" class="item">Indian Institute of Technology Kharagpur, India</a></div>\
                </div>\
            </div>\
            <div class="ui inverted section divider"></div>\
            ');
        if (location.pathname == "/index.html")
        {
        document.write('\
            <a href="index.html"><img src="./assets/images/kosslogo.png" class="ui centered mini image"></a>\
            ');
       }
        else{
            document.write('\
            <a href="../index.html"><img src="../assets/images/kosslogo.png" class="ui centered mini image" ></a>\
            ');
        }
        document.write('\
            <div class="ui horizontal inverted small divided link list">\
                <a class="item" href="https://github.com/kossiitkgp">GitHub</a>\
                <a class="item" href="./contact">Contact Us</a>\
            </div>\
        </div>\
    </div>\
</div>\
');
