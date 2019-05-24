from tornado import template
import tornado.ioloop
import tornado.web
from spider.crawl_data import get_comment
from core.code.Sentiment_svm import svm_predict
'''
/ indexRequestHandler 
POST to /second argument: {url:<url:str>} 
/result resultRequestHandler

'''

class indexRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("first.html")


class resultRequestHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.get_argument("url")
        get_comment(url)

        pos=[]
        neg=[]
        for comment in open("./spider/comment.txt"):
            if(svm_predict(comment)):
                pos.append(comment)
            else:
                neg.append(comment)
        self.render("second.html",pos_comment=pos,neg_comment = neg)


if __name__=="__main__":
    app = tornado.web.Application(
        [
            r'/',indexRequestHandler,
            r'/second', resultRequestHandler
        ],
        #FIXME:error
        template_path='./UI/static'
    )
    app.listen(8888)
    tornado.ioloop.IOLoop().current().start()

