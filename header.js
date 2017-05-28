function header(location)
{
    var home_loc="index.html";
    var events_loc="events/index.html";
    var projects_loc="projects/index.html";
    var team_loc="about/index.html";
    var contact_loc="contact/index.html";
    var terminal_loc="terminal/index.html"
    if (location==="home"){
        string=
			'<a class="active item" href="./'.concat(home_loc,'">Home</a><a class="item" href="./',team_loc,'">About Us</a><a class="item" href="./',events_loc,'">Events</a><a class="item" href="./',projects_loc,'">Projects</a><a class="item" href="./',contact_loc,'">Contact Us</a>');}
		else if (location==="none"){
        string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',team_loc,'">About Us</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',contact_loc,'">Contact Us</a>');}
    else if (location==="events"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',team_loc,'">About Us</a><a class="active item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',contact_loc,'">Contact Us</a>');}
    else if (location==="projects"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',team_loc,'">About Us</a><a class="item" href="../',events_loc,'">Events</a><a class="active item" href="../',projects_loc,'">Projects</a><a class="item" href="../',contact_loc,'">Contact Us</a>');}
    else if (location==="team"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="active item" href="../',team_loc,'">About Us</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',contact_loc,'">Contact Us</a>');}
    else if (location==="help"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',team_loc,'">About Us</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',contact_loc,'">Contact Us</a>');}
    else if (location==="contact"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',team_loc,'">About Us</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="active item" href="../',contact_loc,'">Contact Us</a>');}
		else if (location==="home inv right"){
            string=
			'<a class="ui inverted button" href="./'.concat(terminal_loc,'">Terminal</a><a class="ui inverted button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
		else if (location==="home right"){
            string=
			'<a class="ui button" href="./'.concat(terminal_loc,'">Terminal</a>&nbsp&nbsp&nbsp<a class="ui button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
		else if (location==="inv right"){
            string=
			'<a class="ui inverted button" href="../'.concat(terminal_loc,'">Terminal</a><a class="ui inverted button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
		else if (location==="right"){
            string=
			'<a class="ui button" href="../'.concat(terminal_loc,'">Terminal</a>&nbsp&nbsp&nbsp<a class="ui button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
		else if (location==="term inv right"){
            string=
			'<a class="ui inverted secondary button" href="./'.concat(terminal_loc,'">Terminal</a><a class="ui inverted button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
		else if (location==="term right"){
            string=
			'<a class="ui primary button" href="./'.concat(terminal_loc,'">Terminal</a>&nbsp&nbsp&nbsp<a class="ui button"  target="_blank" href="https://blog.kossiitkgp.in">Blog</a>');}
			
    document.write(string);
}
