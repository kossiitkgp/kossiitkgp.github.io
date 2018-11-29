import requests
from bs4 import BeautifulSoup
import jinja2


def render_jinja_html(template_loc, file_name, **context):
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_loc+'/')
    ).get_template(file_name).render(context)


def pinned_repo_data(soup):
    pinned_repositories =[]

    desired_tags = soup.findAll("li", {"class": "pinned-repo-item"})

    for tag in desired_tags:
        repo_data = {}
        repo_data["name"] = (tag.find("span", {"class": "repo"})).text

        div_for_link = (tag.find("span", {"class": "d-block"}))
        repo_data["url"] = (div_for_link.find("a", {"class": "text-bold"}))["href"]
        repo_data["url"] = "https://github.com" + repo_data["url"]

        repo_data["description"] = (tag.find("p", {"class": "pinned-repo-desc"})).text
        repo_data["description"] = repo_data["description"].strip()

        pinned_repositories.append(repo_data)

    return (pinned_repositories)

def gh_email(soup):
    return(input('Enter the respective email-id : '))

def gh_bio(soup):
    div = soup.find("div", {"class": "user-profile-bio"})
    if div == None:
        return ''

    return div.find("div").text

def blog_link(soup, gh_link):
    blog_tag = (soup.find("a", {"class": "u-url"}))
    blog_link = ''

    if blog_tag == None:
        blog_link = gh_link
    else:
        blog_link = blog_tag['href']

    return(blog_link)

def create_page():
    username = input("Enter github username : ")
    r = requests.get("https://github.com/" + username)
    soup = BeautifulSoup(r.text, 'html.parser')

    if r.status_code == 400:
        print("Wrong username")
    else:
        member_info = {}
        member_info['name'] = username
        member_info['image'] = "http://avatars.githubusercontent.com/" + username
        member_info['gh_link'] = 'https://github.com/' + username
        member_info['full_name'] = soup.find("span", {"class": "vcard-fullname"}).text
        member_info['blog'] = blog_link(soup, member_info['gh_link'])
        member_info['bio'] = gh_bio(soup)
        member_info['email'] = gh_email(soup)
        member_info['position'] = 'Core Team Member' #input("Enter the position in the soicety")
        member_info['pinned_repos'] = pinned_repo_data(soup)

        print(member_info)


        x = render_jinja_html('templates', 'template.tmpl', name = member_info['name'],
                            pinned_repos = member_info['pinned_repos'],
                            image = member_info['image'],
                            gh_link = member_info['gh_link'],
                            bio = member_info['bio'],
                            full_name = member_info['full_name'],
                            email = member_info['email'],
                            blog = member_info['blog'],
                            position = member_info['position']
                            )
        with open("profiles/" + username + ".html", "w") as f:
            f.write(x)


if __name__ == '__main__':
    create_page()