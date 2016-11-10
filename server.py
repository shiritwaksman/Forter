import tornado.ioloop
import tornado.web
import config
import external_storage
import credit_card_handler

def router(storage_instance):
    """Routing http requests to http handlers"""
    return tornado.web.Application([
        (r"/creditcard/([^/]+)", credit_card_handler.MainHandler, dict(storage_instance=storage_instance)),
        (r"/creditcard", credit_card_handler.MainHandler, dict(storage_instance=storage_instance))
    ])

def main():
    """Main Logic to run the server"""

    # init server
    storage_instance = external_storage.ExternalStorage()
    app = router(storage_instance)
    app.listen(config.PORT)

    # run
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
