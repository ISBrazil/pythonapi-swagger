#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
import os
from api.resources.ping import ns as ping_ns
from api.resources.product import ns as product_ns
from api.resources.restplus import api

def create_app():
    app = Flask(__name__)
    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False
    # Enable or disable the mask field, by default X-Fields
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    blueprint = Blueprint('', __name__)
    api.init_app(blueprint)
    api.add_namespace(ping_ns)
    api.add_namespace(product_ns)

    # register each active blueprint
    app.register_blueprint(blueprint)

    return app