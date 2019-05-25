import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
'''
API:
    dict get_comment(url:string)
    return dict of all comments:string
'''

def get_comment(url):
    '''
    div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content
    '''
    option = Options()
    option.headless=True
    driver = WebDriver(options=option)
    driver.get(url)
    #span.course-title.f-ib.f-vam find title of course
    title = BeautifulSoup(driver.page_source,"lxml").select("span.course-title.f-ib.f-vam")[0].get_text()+"\n"
    print("title :",title)
    driver.find_element_by_id("review-tag-button").click()
    # 1,2,3,..button
    comment_page_btns = driver.find_elements_by_class_name("th-bk-main-gh")
    page = 1
    file = open("./spider/comment.txt","w")
    file.write(title.encode("utf-8"))
    for btn in comment_page_btns:
        btn.click()
        soup = BeautifulSoup(driver.page_source,"lxml")
        #page comment list
        comment_tag_list = soup.select("div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content")
        comment_count = len(comment_tag_list)
        print("in:",page," comment count: ", comment_count)
        index = "page"+str(page)+"\n"
        #file.write(index)
        for tag in comment_tag_list:
            text = tag.get_text().rstrip().lstrip()+"\n"
            #print(text)
            file.write(text.encode("utf-8"))
        page = page+1
    file.close()

    driver.quit()
        
    

if __name__ == "__main__":
    get_comment("https://www.icourse163.org/course/PKU-1205962805")