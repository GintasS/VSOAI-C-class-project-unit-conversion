"""
The flask application package.
"""
# No autoformat here because it messes with Flask order of execution.
from flask import Flask
app = Flask(__name__)

import VSOAI_c_project.application