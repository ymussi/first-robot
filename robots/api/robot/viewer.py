from flask_restplus import Resource
from flask import request
from robots.api import api
from robots.api.robot.services import Robot
from robots.robot.robot_mail import login_gmail

ns = api.namespace('robot', description='Robo que loga nas contas gmail via browser')


@ns.route('/login')
class StartRobot(Resource):
    def patch(self):
        login_gmail()
        response = request.json
        ci = Robot()
        ret = ci.conectouEnviou(response)
        
        return ret
