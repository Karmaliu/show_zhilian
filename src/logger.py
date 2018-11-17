import logging

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# mail_handler = SMTPHandler(
#     mailhost='127.0.0.1',
#     fromaddr='server-error@example.com',
#     toaddrs=['admin@example.com'],
#     subject='Application Error'
# )
# mail_handler.setLevel(logging.ERROR)
# mail_handler.setFormatter(logging.Formatter(
#     '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
# ))
#
# if not app.debug:
#     app.logger.addHandler(mail_handler)

logger = logging.getLogger(__name__)
