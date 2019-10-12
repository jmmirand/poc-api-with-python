import unittest
from mock import patch
from mock import Mock
from fakeldap import MockLDAP
from core import LDAP
from apis import ToolsUserGroup

ldapbase="cn=CCC,o=Grupo Santander"
ldaptools="ou=tools," + ldapbase
ldapteams="ou=teams," + ldapbase

top = ('o=Grupo Santander', {'o': ['Grupo Santander']})
serenity = ('cn=Serenity, o=Grupo Santnader', {'cn': ['Serenity']})
groups = ('ou=groups, cn=Serenity, o=Grupo Santander', {'ou': ['groups']})
teams = ( ldapteams , {'ou': ["teams"], "cn":["teams"]})
test_team = ("ou=test_team," + ldapteams , {'ou': ['test_team'], "cn":["test_team"]})

tools = ( ldaptools, { "ou": ["tools"], "cn":["tools"] } )
tools_alm = ( "ou=alm," + ldaptools , {'ou': ['alm'], "cn":["alm"]})





directory = dict([top, serenity, groups,teams, test_team, tools,tools_alm])

_mock_ldap = MockLDAP(directory)




class TestYourTestCase(unittest.TestCase):
    def setUp(self):
        # Patch where the ldap library is used:
        self.ldap_patcher = patch('core.LDAPAlm.ldap.open')
        self.mock_ldap = self.ldap_patcher.start()
        _mock_ldap.unbind_s = Mock()
        self.mock_ldap.return_value = _mock_ldap




    def tearDown(self):
        _mock_ldap.reset()
        self.mock_ldap.stop()


    def test_sum(self):
        # Register a return value with the MockLDAP object
        l = LDAP()

        result = l.createGroupOfNames( "base", "base", ldapteams  )
        result = l.listGroupOfNames(ldapteams,"ou")
        result = l.listGroupOfNames(ldaptools,"cn")
        self.assertEqual(12, 12)



    def test_toolsusergroup(self):
        print "====================> " + ldaptools
        a = ToolsUserGroup()
        result = a.get()
        print result





#if __name__ == "__main__":
#    unittest.main()



