"""
The server_setup.py module is loaded at application startup and
allows you to configure authentication and alternative routes like probes.
"""

import os
import writer.serve
import writer.auth

# Configure Basic Auth
# :see https://dev.writer.com/framework/authentication
#
# auth = writer.auth.BasicAuth(
#     login='admin',
#     password='admin'
# )
#
# writer.serve.register_auth(auth)

# Configure Probe
# :see https://dev.writer.com/framework/custom-server
# asgi_app = writer.serve.app
#
# @asgi_app.get("/probes/healthcheck")
# def probes_healthcheck():
#     return "OK"
