import tornado.ioloop
import tornado.web
import config
import external_storage
import credit_card_handler

def make_app(storage_instance):
    return tornado.web.Application([
        (r"/creditcard/([^/]+)", credit_card_handler.MainHandler, dict(storage_instance=storage_instance)),
        (r"/creditcard", credit_card_handler.MainHandler, dict(storage_instance=storage_instance))
    ])

def main():
    storage_instance = external_storage.ExternalStorage()
    app = make_app(storage_instance)
    app.listen(config.PORT)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
