import tornado.ioloop
import tornado.web
import uuid
import redis

class CreditCardHandler(tornado.web.RequestHandler):

    def initialize(self, redis_instance):
        self.redis_instance = redis_instance

    def get(self, token=None):
        """retrieving a stored credit card"""
        if self.redis_instance.exists(token):
            output = {
                'credit-card': self.redis_instance.get(token)
            }

            message = tornado.escape.json_encode(output)
        else:
            message = 'Token does not exist'

        self.write(message)

    def post(self):
        """"inserting a new credit card"""
        try:
            credit_card = str(tornado.escape.json_decode(self.request.body)["credit-card"])
        except ValueError:
            message = 'Expects to receive a JSON object in the following format: ' \
                      '{"credit-card": "<credit card number>"}'
        except KeyError:
            message = 'The key "credit-card" does not exist in the request'
        else:
            if not credit_card:
                message = 'No value exist for key "credit-card" in the request'
            else:
                token = str(uuid.uuid5(uuid.NAMESPACE_DNS, credit_card))
                self.redis_instance.set(token, credit_card)

                # The response is a unique id that represents the credit card token
                output = {
                    'token': token
                }
                message = tornado.escape.json_encode(output)

        self.write(message)


def make_app(redis_instance):
    return tornado.web.Application([
        (r"/creditcard/([^/]+)", CreditCardHandler, dict(redis_instance=redis_instance)),
        (r"/creditcard", CreditCardHandler, dict(redis_instance=redis_instance))
    ])


def main():
    redis_instance = redis.StrictRedis(host='192.168.21.102', port=6379, db=0)
    app = make_app(redis_instance)
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
