import datetime
from jira import JIRA


def jira_setup(project, assignee, title, description, filename='', due=1, comment=''):
    apiKey = 'QnucOPUGJMdyos3Yg3ZvE83C'
    jira = JIRA(basic_auth=('abcdef@gmail.com', apiKey),
                options={"server": 'https://shoregroup.atlassian.net'})
    duedate = str((datetime.date.today() + datetime.timedelta(days=due)).strftime('%Y-%m-%d'))
    issue_list = [{
        'project': {'key': project},
        'summary': title,
        'description': description,
        'issuetype': {'name': 'Task'},
        'assignee': {'name': assignee},
        'priority': {'name': 'High'},
        'duedate': duedate
    }]
    issues = jira.create_issues(issue_list)
    issueKey = issues[0]['issue'].key
    print(f'{issueKey} created')
    if filename:
        with open(filename, 'rb') as f:
            jira.add_attachment(issue=issueKey, attachment=f)
    if comment:
        jira.add_comment(issue=issueKey, body=comment)
        print(f'Comment added to {issueKey}')
    return issueKey
