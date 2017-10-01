import os
import json
import requests
from collections import OrderedDict

import jinja2


def render_jinja_html(template_loc, file_name, **context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_loc+'/')
    ).get_template(file_name).render(context)


def profile(name, position=None):
    url = "https://api.github.com/graphql"
    headers = {"Authorization": "Basic "+os.environ['OUATH_KEY']}
    query = json.dumps({"query": "query{user(login: \"" + name +
                        "\") { name email avatarUrl url bio websiteUrl"
                        " pinnedRepositories(first: 6) "
                        "{ nodes { name url description } } } }"})
    r = requests.post(url, headers=headers, data=query)
    print r.content.decode("utf-8")
    data_dict = json.loads(r.content.decode("utf-8"), sorted)
    pinned_repos = data_dict['data']['user']['pinnedRepositories']['nodes']
    image = data_dict['data']['user']['avatarUrl']
    gh_link = data_dict['data']['user']['url']
    bio = data_dict['data']['user']['bio']
    full_name = data_dict['data']['user']['name']
    email = data_dict['data']['user']['email']
    blog = data_dict['data']['user']['websiteUrl']

    x = render_jinja_html('templates', 'template.tmpl', name=name,
                          pinned_repos=pinned_repos,
                          image=image,
                          gh_link=gh_link,
                          bio=bio,
                          full_name=full_name,
                          email=email,
                          blog=blog,
                          position=position
                          )
    with open("profiles/" + name + ".html", "w") as f:
        f.write(x)


def generate(id=None):
    if id is not None:
        profile(id, position="Member")
    else:
        with open("data.json") as json_data_file:
            json_data = json.load(json_data_file)
            for i in json_data:
                for j in json_data[i]:
                    try:
                        profile(j, i)
                    except Exception:
                        print "Error generating profile for :- "
                        print "ID - " + j         
    return "Completed"


generate()
