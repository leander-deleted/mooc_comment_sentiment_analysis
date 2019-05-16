import requests
from bs4 import BeautifulSoup

'''
API:
    dict get_comment(url:string)
    return dict of all comments:string

'''

def get_comment(url):
    '''
    div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content
    '''
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        comment_tag_list = soup.select("div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content")
        #get dict of comment
