import tornado.ioloop
import tornado.web

class CreditCardHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("get")

    def post(self):
        self.write("post")

def make_app():
    tokenize_credit_cards = {}
    return tornado.web.Application([
        (r"/creditcard", CreditCardHandler)
    ])

def main():
    app = make_app()
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()