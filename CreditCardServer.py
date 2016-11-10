import tornado.ioloop
import tornado.web
import uuid

class CreditCardHandler(tornado.web.RequestHandler):

    def initialize(self, tokenizer):
        self.tokenizer = tokenizer

    def get(self, creditcard):
        """retrieving a stored credit card"""
        self.write('{"credit-card":"' + self.tokenizer[creditcard] + '"}')

    def post(self):
        """"inserting a new credit card"""
        creditcard = str(tornado.escape.json_decode(self.request.body)["credit-card"])
        token = str(uuid.uuid3(uuid.NAMESPACE_DNS, creditcard))
        self.tokenizer[token] = creditcard
        # The response is a unique id that represents the credit card token
        self.write('{"token" : "' + token + '"}')


def make_app():
    tokenize_credit_cards = {}
    return tornado.web.Application([
        (r"/creditcard/([^/]+)", CreditCardHandler, dict(tokenizer=tokenize_credit_cards)),
        (r"/creditcard", CreditCardHandler, dict(tokenizer=tokenize_credit_cards))
    ])

def main():
    app = make_app()
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()