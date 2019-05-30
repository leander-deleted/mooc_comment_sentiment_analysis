import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
'''
API:
    get_comment(url:string)
    write comment into file ./spider/comment.txt
'''

def get_comment(url):
    option = Options()
    option.headless=True
    driver = WebDriver(options=option)
    driver.get(url)
    # css selector: span.course-title.f-ib.f-vam find title of course
    title = BeautifulSoup(driver.page_source,"lxml").select("span.course-title.f-ib.f-vam")[0].get_text()+"\n"
    print("title :",title)
    driver.find_element_by_id("review-tag-button").click()
    comment_page_btns = driver.find_elements_by_class_name("th-bk-main-gh")
    page = 1
    file = open("./spider/comment.txt","w")
    file.write(title.encode("utf-8"))
    for btn in comment_page_btns:
        # click each button in list
        btn.click()
        soup = BeautifulSoup(driver.page_source,"lxml")
        '''
        css selector: div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content
        '''
        comment_tag_list = soup.select("div.ux-mooc-comment-course-comment_comment-list_item div.ux-mooc-comment-course-comment_comment-list_item_body_content")
        comment_count = len(comment_tag_list)
        print("in:",page," comment count: ", comment_count)
        #index = "page"+str(page)+"\n"
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