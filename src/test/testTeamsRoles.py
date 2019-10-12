import unittest
import os
from core import LDAP
from model import TeamsModel



class TestTeamTools(unittest.TestCase):
    def setUp(self):
        # Patch where the ldap library is used:

	TeamsModel.removeTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer", "c3_test_team" )
	TeamsModel.removeTeamRole( "developer" , "c3_test_team")
        TeamsModel.removeTeam( "c3_test_team" )



    def tearDown(self):
	return

    def test_AddRemoveTeamGroup(self):

	# Lista de Teams
	listaTeams = TeamsModel.getTeams()

	# Create Team
	result  = TeamsModel.addTeam( "c3_test_team")
	self.assertEquals( result["retcode"] , 200 )
	listaTeams2 = TeamsModel.getTeams()
	self.assertEquals( len(listaTeams) + 1  ,len( listaTeams2 ) )

	# TEST ERROR Crear Role Ya existe	
	result = TeamsModel.addTeam ( "c3_test_team" )
	self.assertEquals ( result ["retcode"], 420 )

	
	# Borrar un Role que no existe
	result = TeamsModel.removeTeam ( "c3_test_team" )
	listaTeams2 = TeamsModel.getTeams()
	self.assertEquals ( result["retcode"] , 200 )
	self.assertEquals ( len ( listaTeams) , len (listaTeams2) )
	
	# TEST ERROR Borrar un grupo que no existe
	result = TeamsModel.removeTeam ( "c3_test_team" )
        listaTeams2 = TeamsModel.getTeams()
	print result
        self.assertEquals ( result["retcode"] , 432 )



    def test_AddRemoveTeamRoleGroup(self):
	result  = TeamsModel.addTeam( "c3_test_team")	
	listaTeams = TeamsModel.getTeamRoles ("c3_test_team")
	self.assertEquals( len(listaTeams), 0 )  
	
	# Crear Role en un Team existente
	result = TeamsModel.addTeamRole (  "developer" , "c3_test_team")
	listaTeams2 =  TeamsModel.getTeamRoles ("c3_test_team") 
	self.assertEquals( result["retcode"] , 200 )
	self.assertEquals( len ( listaTeams2 ) , 1 ) 

	# TEST ERROR intento crear un Role en un Team no existente
	result = TeamsModel.addTeamRole ( "developer" , "XXXXXX" )
	self.assertEquals ( result["retcode"] , 432 )


	# TEST ERROR borrar un Role Inexistente de un Team no existente
	result = TeamsModel.removeTeamRole ( "developerxxxx" , "c3_test_teamxxxxx" )
        self.assertEquals ( result["retcode"] , 432 )

	# TEST ERROR buscar roles en un team Inexistente
	listaTeams = TeamsModel.getTeamRoles( "xxxxxxxx" )
	self.assertEquals ( len ( listaTeams) , 0  ) 


	# borrar un Role inexistente de un TEam no existente
        result = TeamsModel.removeTeamRole ( "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )
	listaTeam =  TeamsModel.getTeamRoles ("c3_test_team")
	self.assertEquals ( len ( listaTeam ) , 0 ) 

	# borrar el team creado para la prueba
	result = TeamsModel.removeTeam ( "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )



	
    def test_AddRemoveTeamRoleMember(self):

        result = TeamsModel.addTeam( "c3_test_team")
	self.assertEquals ( result["retcode"] , 200 )
	result = TeamsModel.addTeamRole ( "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )

	
	# lista de miembros de team-role
	list_members = TeamsModel.getTeamRoleMembers( "developer", "c3_test_team" )
	self.assertEquals ( len(list_members ) , 0 )

	# TEST ERROR lista de miembors de un role inexistente
	list_members = TeamsModel.getTeamRoleMembers( "developerxxxxx", "c3_test_team" )
        self.assertEquals ( len(list_members ) , 0 )


        # TEST ERROR lista de miembors de un role inexistente
        list_members = TeamsModel.getTeamRoleMembers( "developerxxxxx", "c3_test_team_xxxx" )
        self.assertEquals ( len(list_members ) , 0 )

	
	# Add member Team Role
	result = TeamsModel.addTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer", "c3_test_team" )
	self.assertEquals ( result["retcode"] , 200 )

	
	# TEST ERROR Add member Team Role that EXIST
        result = TeamsModel.addTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer", "c3_test_team" )
        self.assertEquals ( result["retcode"] , 420 )

	# lista de miembros
        list_members = TeamsModel.getTeamRoleMembers( "developer", "c3_test_team" )
        self.assertEquals ( len(list_members ) , 1 )


	# TEST ERROR Add member Team and Role not Exist
        result = TeamsModel.addTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developerxxxxxx" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 432 )
        result = TeamsModel.addTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer" , "c3_test_teamxxx" )
        self.assertEquals ( result["retcode"] , 432 )


	# TEST ERROR Borrar team-role sin estar vacios
        result = TeamsModel.removeTeamRole (  "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 480)

	result = TeamsModel.removeTeam(  "c3_test_team" )
        self.assertEquals ( result["retcode"] , 480)

	
	# TEST ERROR Borrar miembros que no existen
        result = TeamsModel.removeTeamRoleMember ( "uid=xxxxx,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 416 )
        result = TeamsModel.removeTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developerxxx" , "c3_test_teamxxx" )
        self.assertEquals ( result["retcode"] , 432 )
		

	# Borrar Miembros
	result = TeamsModel.removeTeamRoleMember ( "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" , "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )
        
	result = TeamsModel.removeTeamRole (  "developer" , "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )
        
	result = TeamsModel.removeTeam(  "c3_test_team" )
        self.assertEquals ( result["retcode"] , 200 )



if __name__ == "__main__":
    unittest.main()

