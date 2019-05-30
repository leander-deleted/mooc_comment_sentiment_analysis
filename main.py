from tornado import template
import tornado.ioloop
import tornado.web
from spider.crawl_data import get_comment
from core.code.Sentiment_svm import svm_predict
import os
'''
/ indexRequestHandler 
POST to /second argument: {url:<url:str>} 
/result resultRequestHandler

'''

class indexRequestHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.get_template_path())
        self.render("first.html")


class resultRequestHandler(tornado.web.RequestHandler):
    def post(self):
        url = self.get_argument("url")
        print(url)
        get_comment(url)
        print("finish get comment")

        pos=[]
        neg=[]
        first_line = True
        for comment in open("./spider/comment.txt"):
            if(first_line):
                t=comment
                first_line = False
            else:
                if(svm_predict(comment)):
                    pos.append(comment)
                    #print("pos :",comment)
                else:
                    neg.append(comment)
                    #print("neg :",comment)
        self.render("second.html",title=t,pos_comment=pos,neg_comment = neg)


if __name__=="__main__":
    app = tornado.web.Application(
        [
            (r'/',indexRequestHandler),
            (r'/second', resultRequestHandler)
        ],
        #FIXME:error
        template_path=os.path.join(os.path.dirname(__file__),"ui/template"),
        static_path=os.path.join(os.path.dirname(__file__),"ui"
                                                           "ki"
                                                           "h:wq"
                                                           ":::wq"
                                                           "/static")
    )
    app.listen(8888)
    print("server run at port 8888")
    tornado.ioloop.IOLoop().current().start()

