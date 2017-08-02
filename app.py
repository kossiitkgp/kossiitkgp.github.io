import json
import os
import requests
f=open("members.txt","r")
repos=[]
openissues=0
closedissues=0
openprs=0
closedprs=0
itercount=0
os.system("git pull --rebase origin master")
while (1):
            name=f.readline()
            if not name: break
            name=name.strip()
            url = "https://api.github.com/graphql"
            headers = {"Authorization": "Basic "+str(os.environ['OUATH_KEY'])}
            repo_cur=issue_cur=pr_cur="first: 100"
            while (1):
                query = json.dumps({"query": "query{user(login: \"" + name +
                                        "\") { repositories("+str(repo_cur)+"){edges{node{url isFork}} pageInfo{endCursor hasNextPage}} issues("+str(issue_cur)+")\
                                        {edges{node{state}} pageInfo {endCursor hasNextPage}} pullRequests("+str(pr_cur)+"){edges{node{state}} pageInfo \
                                        {endCursor hasNextPage}} }}"})
                print("query",query)
                r = requests.post(url, headers=headers, data=query)
                data_dict = json.loads(str(r.content))
                try:
                    next_repo=data_dict['data']['user']['repositories']['pageInfo']['endCursor']
                except:
                    next_repo="errored"
                try:
                    next_issue=data_dict['data']['user']['issues']['pageInfo']['endCursor']
                except:
                    next_issue="errored"
                try:
                    next_pr=data_dict['data']['user']['pullRequests']['pageInfo']['endCursor']
                except:
                    next_pr="errored"

                print ("data dict",data_dict)


                if next_repo!="errored":
                    for repo in data_dict['data']['user']['repositories']['edges']:
                        if repo['node']['isFork']==False:
                            repos.append(repo['node']['url'])
                    if next_repo!=None and data_dict['data']['user']['repositories']['pageInfo']['hasNextPage']!=False:
                        repo_cur='first:100 after:"'+str(next_repo)+'" '
                    else:
                        repo_cur='first: 0'

                if next_issue!="errored":
                    for issue in data_dict['data']['user']['issues']['edges']:
                        if issue['node']['state']=='CLOSED':
                            closedissues+=1
                        else:
                            openissues+=1
                        if next_issue!=None and data_dict['data']['user']['issues']['pageInfo']['hasNextPage']!=False:
                            issue_cur='first: 100 after:"'+str(next_issue)+'" '
                        else:
                            issue_cur='first: 0'

                if next_pr!="errored":
                    for pr in data_dict['data']['user']['pullRequests']['edges']:
                        if pr['node']['state']=='MERGED':
                            closedprs+=1
                        elif pr['node']['state']=='OPEN':
                            openprs+=1
                        if next_pr!=None and data_dict['data']['user']['pullRequests']['pageInfo']['hasNextPage']!=False:
                            pr_cur='first: 100 after:"'+str(next_pr)+'" '
                        else:
                            pr_cur='first: 0'
                
                if (data_dict['data']['user']['repositories']['pageInfo']['hasNextPage']==False or next_repo==None) and (data_dict['data']['user']\
                    ['issues']['pageInfo']['hasNextPage']==False or next_issue==None) and (data_dict['data']['user']['pullRequests']['pageInfo']\
                    ['hasNextPage']==False or next_pr==None): break
                itercount+=1

                    


repos=set(repos)
print repos
print "open issues: "+str(openissues)
print "closed issues: "+str(closedissues)
print "open prs: "+str(openprs)
print "closed prs: "+str(closedprs)
print "repeated: "+str(itercount)
# import os<!-- Closed issues -->
lines_of_code=0
for repo in repos:
  os.system("git clone --depth 1 "+str(repo)+".git ")
  os.system("cloc "+str(repo).split('/')[-1]+" > out")
  f=open("out","r")
  alltext=f.read()
  # print alltext
  # print alltext.split(' ')[-1].split('-')[0]
  try:
    lines_of_code+=int(alltext.split(' ')[-1].split('-')[0])
    os.system("rm -rf "+str(repo.split('/')[-1]))
  except:
    pass
  print ("lines of code",lines_of_code)

print lines_of_code

f=open("index.tmpl","r")
all_lines=f.read()
all_lines=all_lines.replace("<!-- Open PRs -->",str(openprs))
all_lines=all_lines.replace("<!-- Closed PRs -->",str(closedprs))
all_lines=all_lines.replace("<!-- Open Issues -->",str(openissues))
all_lines=all_lines.replace(" <!-- Closed issues -->",str(closedissues))
all_lines=all_lines.replace("<!-- Lines -->",str(lines_of_code))
f=open("index.html","r")
all_prev_lines=f.read()
if all_prev_lines!=all_lines:
    f=open("index.html","w")
    f.write(all_lines)
