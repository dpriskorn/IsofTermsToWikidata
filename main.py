import logging

from models.public_org import PublicOrgHandler

logging.basicConfig(level=logging.INFO)

handler = PublicOrgHandler()
handler.start()
