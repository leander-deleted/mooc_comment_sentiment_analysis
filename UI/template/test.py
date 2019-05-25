import tornado.template

l = tornado.template.Loader(".")
g = l.load("second.html").generate(pos_comment = [1,2,3],neg_comment=[4,5,6])
print(__file__)