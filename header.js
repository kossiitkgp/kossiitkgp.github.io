function header(location)
{
    var home_loc="index.html";
    var events_loc="events/index.html";
    var projects_loc="projects/index.html";
    var team_loc="team/index.html";
    var help_loc="help/index.html";
    if (location==="home"){
        string=
			'<a class="active item" href="./'.concat(home_loc,'">Home</a><a class="item" href="./',events_loc,'">Events</a><a class="item" href="./',projects_loc,'">Projects</a><a class="item" href="./',team_loc,'">Our Team</a><a class="item" href="./',help_loc,'">Help</a>');}
    else if (location==="events"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="active item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',team_loc,'">Our Team</a><a class="item" href="./',help_loc,'">Help</a>');}
    else if (location==="projects"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',events_loc,'">Events</a><a class="active item" href="../',projects_loc,'">Projects</a><a class="item" href="../',team_loc,'">Our Team</a><a class="item" href="./',help_loc,'">Help</a>');}
    else if (location==="team"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="active item" href="../',team_loc,'">Our Team</a><a class="item" href="./',help_loc,'">Help</a>');}
    else if (location==="help"){
            string=
			'<a class="item" href="../'.concat(home_loc,'">Home</a><a class="item" href="../',events_loc,'">Events</a><a class="item" href="../',projects_loc,'">Projects</a><a class="item" href="../',team_loc,'">Our Team</a><a class="active item" href="./',help_loc,'">Help</a>');}
 
    document.write(string);
}
