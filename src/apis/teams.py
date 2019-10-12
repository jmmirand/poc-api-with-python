from flask import jsonify, request
from flask_restplus import Namespace, Resource, fields
from model.teammodel import TeamsModel

api = Namespace('teams', description='Gestion Teams asociados ALM')

fields_teamname = api.model(
    'teamname',
    {'teamname': fields.String(description='Nombre Team', required=True)})

fields_team_role = api.model(
    'team_role',
    {'role': fields.String(description='Role Name Team', required=True)})

fields_team_member = api.model(
    'team_member',
    {'userdn': fields.String(description='member DN', required=True)})

model_return = api.model(
    'return_toolsgroup', {
        'message': fields.String(description='Menssage', required=True),
        'retcode': fields.Integer(description='Resturn Code', required=True)
    })


@api.route("/")
class Teams(Resource):
    @api.doc(description='list all teams')
    def get(self):
        result = TeamsModel.getTeams()
        return jsonify(result)

    @api.doc(description="Create team")
    @api.response(200, "Team Created", model=model_return)
    @api.response(400, "Error Creating Team", model=model_return)
    @api.expect(fields_teamname)
    def post(self):
        team_name = request.json["teamname"]
        response = TeamsModel.addTeam(team_name)

        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response

    @api.doc(description="Remove Team")
    @api.expect(fields_teamname)
    @api.response(200, "Team deleted", model=model_return)
    @api.response(400, "Error Deleting Team", model=model_return)
    def delete(self):
        team_name = request.json["teamname"]
        response = TeamsModel.removeTeam(team_name)

        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response


@api.route("/<teamname>")
class TeamsRole(Resource):
    @api.doc(description='list all teams roles')
    def get(self, teamname):
        result = TeamsModel.getTeamRoles(teamname)
        return jsonify(result)

    @api.doc(description="Create Role in team")
    @api.response(200, "Team Role Created", model=model_return)
    @api.response(400, "Error Creating Role", model=model_return)
    @api.expect(fields_team_role)
    def post(self, teamname):

        if ("role" not in request.json):
            response = {
                "message": "ERROR Role parameter Bad Format",
                "retcode": 400
            }
        else:
            team_role = request.json["role"]
            response = TeamsModel.addTeamRole(team_role, teamname)

        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response

    @api.doc(description="Remove Profile from team")
    @api.expect(fields_team_role)
    @api.response(200, "Team Role  DELETED", model=model_return)
    @api.response(400, "Error Creating Team Role", model=model_return)
    def delete(self, teamname):

        team_role = request.json["role"]

        response = TeamsModel.removeTeamRole(team_role, teamname)
        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response


@api.route("/<teamname>/<role>/members")
class TeamsProfileMembers(Resource):
    @api.doc(description="List role team  members")
    @api.response(200, "Return list of member from role team")
    def get(self, teamname, role):
        result = TeamsModel.getTeamRoleMembers(role, teamname)
        return result

    @api.doc(description="Add user to a role")
    @api.expect(fields_team_member)
    @api.response(200, "Member added in role", model=model_return)
    @api.response(400, "ERROR , Adding Member in role", model=model_return)
    def post(self, teamname, role):

        if ("userdn" not in request.json):
            response = {
                "message": "ERROR userdn parameter Bad Format",
                "retcode": 400
            }
        else:
            member = request.json["userdn"]
            response = TeamsModel.addTeamRoleMember(member, role, teamname)

        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response

    @api.doc(description="Remove user from role")
    @api.expect(fields_team_member)
    @api.response(200, "Member removed from role", model=model_return)
    @api.response(400, "ERROR removing member  from role", model=model_return)
    def delete(self, teamname, role):
        member = request.json["userdn"]
        response = TeamsModel.removeTeamRoleMember(member, role, teamname)
        if response["retcode"] == 200:
            response = jsonify(response)
            response.status_code = 200
        else:
            response = jsonify(response)
            response.status_code = 400

        return response
