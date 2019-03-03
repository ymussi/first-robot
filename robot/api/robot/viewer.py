from flask_restplus import Resource
from flask import request
from robot.api import api
from robot.api.robot.services import Robot
from robot.codigo.robot_mail import login_gmail

ns = api.namespace('robot', description='Robo que loga nas contas gmail via browser')


@ns.route('/login')
class StartRobot(Resource):
    def patch(self):
        login_gmail()
        response = request.json
        ci = Robot()
        ret = ci.conectouEnviou(response)
        
        return ret
