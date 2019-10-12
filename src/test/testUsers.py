import unittest
import os
from core import LDAP
from model import UsersModel
from model import TeamsModel


class TestTeamTools(unittest.TestCase):
    def setUp(self):
        TeamsModel.addTeam( "c3_test_team")
        TeamsModel.addTeamRole( "developer" , "c3_test_team")
        TeamsModel.addTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer", "c3_test_team" )

    def tearDown(self):
        #TeamsModel.removeTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer", "c3_test_team" )
        #TeamsModel.removeTeamRole( "developer" , "c3_test_team")
        #TeamsModel.removeTeam( "c3_test_team" )
	return


    def testGetByUid(self):
	listaUsuarios = UsersModel.getByUID ( "N057083" )
	self.assertEquals ( len(listaUsuarios) , 2 ) 

    def testExistUserByUID (self):
	response = UsersModel.ExistUserByUID ( "N057083")
	self.assertEquals ( response["retcode"] , 200 )

	response = UsersModel.ExistUserByUID ( "N057083xxxxx")
        self.assertEquals ( response["retcode"] , 204 )


    def testExistUserByCorpAlias ( self ):
	listaUsuarios = UsersModel.getUserByCorpAlias ( "N057083" )
        self.assertEquals ( len(listaUsuarios) , 2 )

    def testGetTeamsUserDNBelongTo( self ):
	listaTeams = UsersModel.getTeamsUserDNBelongTo("uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander")
	self.assertEquals ( len(listaTeams), 1 )

    def testGetTeamsUidUsersBelongTo( self ):
        listaTeams = UsersModel.getTeamsUidBelongTo("N057083")
        self.assertEquals ( len(listaTeams), 1 )

    def testGetUserByDN(self):
        usuario= UsersModel.getUserByDN ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander")
        print usuario
        self.assertEquals ( usuario["alias"], "n057083" )
