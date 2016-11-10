import tornado.ioloop
import tornado.web
import uuid

class CreditCardHandler(tornado.web.RequestHandler):

    def initialize(self, tokenizer):
        self.tokenizer = tokenizer

    def get(self, token = None):
        """retrieving a stored credit card"""
        message = ""
        try:
            if token in self.tokenizer.keys():
                message = '{"credit-card":"' + token + '"}'
            else:
                message = 'token does not exist'
        except:
            message = 'Invalid Input'

        self.write(message)

    def post(self):
        """"inserting a new credit card"""
        message = 'Invalid Input'
        try:
            creditcard = str(tornado.escape.json_decode(self.request.body)["credit-card"])
        except: pass
        else:
            if creditcard:
                token = str(uuid.uuid3(uuid.NAMESPACE_DNS, creditcard))
                self.tokenizer[token] = creditcard
                # The response is a unique id that represents the credit card token
                message = '{"token" : "' + token + '"}'

        self.write(message)


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