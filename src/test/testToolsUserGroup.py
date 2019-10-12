import unittest
import os
from core import LDAP
from model import ToolsUserGroupModel



class TestYourTestCase(unittest.TestCase):
    def setUp(self):
        # Patch where the ldap library is used:

	iRet =  ToolsUserGroupModel.removeToolsGroup("tst")
	
	iRet = ToolsUserGroupModel.removeToolsGroupMember( "tst_members", "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" )
	iRet =  ToolsUserGroupModel.removeToolsGroup("tst_members")


    def tearDown(self):
	return

    def test_addRemoveToolsGroup(self):

	
        # Register a return value with the MockLDAP object
	listaGrupos  = ToolsUserGroupModel.getToolsGroups()        
	
	print str(listaGrupos)
	result = ToolsUserGroupModel.addToolsGroup("tst")
	self.assertEquals ( result["retcode"] , 200 )

	listaGrupos2 = listaGrupos
	listaGrupos2.append ( "tst" )
	self.assertEquals( listaGrupos , listaGrupos2 )

	# Si se intenta crear el mismo grupo da error -20
        # por que existe

	result =  ToolsUserGroupModel.addToolsGroup("tst")
	self.assertEquals ( result["retcode"] , 420 )


	
	# Borramos el grupo de herramientas y dejamos el juego de pruebas
	# igual que nos lo encontramos.
        result  =  ToolsUserGroupModel.removeToolsGroup("tst")
        self.assertEquals ( result["retcode"] , 200 )



    def test_AddRemoveMembersToolsGroup(self):


	users = ToolsUserGroupModel.getToolsGroupMember("tst_members")
	self.assertEquals( len(users), 0 )
	
	# Creo el grupo de usuario para herramientas y add un usuario
	result =  ToolsUserGroupModel.addToolsGroup("tst_members")
        self.assertEquals ( result["retcode"] , 200 )


	#  incorporo un usuario en el grupo
	result = ToolsUserGroupModel.addToolsGroupMember( "tst_members", "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" )
        self.assertEquals ( result["retcode"] , 200 )

	users = ToolsUserGroupModel.getToolsGroupMember("tst_members")
	self.assertEquals( len(users), 1 )


        #  TEST ERROR intento incorporar al mismo usuario dos veces
        result = ToolsUserGroupModel.addToolsGroupMember( "tst_members", "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" )
	self.assertEquals ( result["retcode"] , 420 )
        self.assertEquals( len(users), 1 )

	
        #  TEST ERROR Borro el grupo de usuario con un usuario dentro
        result =  ToolsUserGroupModel.removeToolsGroup("tst_members")
	self.assertEquals ( result["retcode"] , 480 )



	# Borrar usuario del grupo
	result  = ToolsUserGroupModel.removeToolsGroupMember( "tst_members", "uid=n057083,ou=Usuarios, o=Produban, c=es,o=Grupo Santander,o=Grupo Santander" )
        self.assertEquals ( result["retcode"] , 200 )
	

	users = ToolsUserGroupModel.getToolsGroupMember("tst_members")
        self.assertEquals( len(users), 0 )


        # Borro el grupo de usuario para herramientas
        result =  ToolsUserGroupModel.removeToolsGroup("tst_members")
        self.assertEquals ( result["retcode"] , 200 )



if __name__ == "__main__":
    unittest.main()

