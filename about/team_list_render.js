var sec= document.getElementById('profiles')
for(i=0;i<Advisors.length;i++)
{
    if((Advisors[i][1]=="gauravrpjain")||(Advisors[i][1]=="bad-smruti"))
        continue;
    sec.innerHTML+=
    `<div class="ui fluid card"> <article class="col-sm-6 profile">
    <div class="profile-header">
        <img class="ui circular image" width="100px" height="100px" src="https://avatars.githubusercontent.com/${Advisors[i][1]}">
    </div>
    <div class="profile-content">
        <h3><a href="../profiles/${Advisors[i][1]}.html">${Advisors[i][0]}</a></h3>
        <div class="lead position">Advisor</div>
        <a href="https://github.com/${Advisors[i][1]}">
            <div class="ui button"><i class="github icon"></i>Follow <i>@${Advisors[i][1]}</i></div>
        </a>
    </div>
    </article></div>`
}

for(i=0;i<Executives.length;i++)
{
    sec.innerHTML+=
    `<div class="ui fluid card"> <article class="col-sm-6 profile">
    <div class="profile-header">
        <img class="ui circular image" width="100px" height="100px" src="https://avatars.githubusercontent.com/${Executives[i][1]}">
    </div>
    <div class="profile-content">
        <h3><a href="../profiles/${Executives[i][1]}.html">${Executives[i][0]}</a></h3>
        <div class="lead position">Executive</div>
        <a href="https://github.com/${Executives[i][1]}">
            <div class="ui button"><i class="github icon"></i>Follow <i>@${Executives[i][1]}</i></div>
        </a>
    </div>
    </article></div>`
}

for(i=0;i<CTMs.length;i++)
{
    sec.innerHTML+=
    `<div class="ui fluid card"> <article class="col-sm-6 profile">
    <div class="profile-header">
        <img class="ui circular image" width="100px" height="100px" src="https://avatars.githubusercontent.com/${CTMs[i][1]}">
    </div>
    <div class="profile-content">
        <h3><a href="../profiles/${CTMs[i][1]}.html">${CTMs[i][0]}</a></h3>
        <div class="lead position">Core Team Member</div>
        <a href="https://github.com/${CTMs[i][1]}">
            <div class="ui button"><i class="github icon"></i>Follow <i>@${CTMs[i][1]}</i></div>
        </a>
    </div>
    </article></div>`
}