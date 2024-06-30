#!/usr/bin/env python3
""" Module to test access nested map"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test access nested map"""
    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json')
    def test_org(self, url: str, mockObj: Mock):
        """ Test org method to check if get_json was called """
        cls = GithubOrgClient(url)
        cls.org()
        url_used = f'https://api.github.com/orgs/{url}'
        mockObj.assert_called_once_with(url_used)

    def test_public_repos_url(self):
        """ mock property from org as returned value """
        target = 'client.GithubOrgClient.org'
        with patch(target, new_callable=PropertyMock) as propMock:
            value = {'repos_url': 'value'}
            propMock.return_value = value
            cls = GithubOrgClient(value['repos_url'])
            result = cls._public_repos_url
            self.assertEqual(result, value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_getJson):
        """ Test public repos """
        target = 'client.GithubOrgClient._public_repos_url'
        with patch(target, new_callable=PropertyMock) as _reposMock:
            _reposMock.return_value = "repo"
            payLoad = [{"name": "repo"}, {"name": "second_repo"}]
            mock_getJson.return_value = payLoad
            Github = GithubOrgClient("repo")
            result_list = Github.public_repos()
            self.assertEqual(result_list, ["repo", "second_repo"])
            mock_getJson.assert_called_once()
            _reposMock.assert_called_once()

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False]
        ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Check if licence the same """
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected_result)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos',
                      'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for test integration Org """
    @classmethod
    def setUpClass(cls):
        """ Set up class """
        list_payLoad = [cls.org_payload, cls.repos_payload]
        vals = {'return_value.json.side_effect': list_payLoad}
        cls.get_patcher = patch('requests.get', **vals)
        cls.get_patcher.start()

    def test_public_repos(self):
        """ Test public repos """
        cls = GithubOrgClient('value')
        self.assertEqual(cls.org, self.org_payload)
        self.assertEqual(cls.repos_payload, self.repos_payload)
        self.assertEqual(cls.public_repos(), self.expected_repos)

    @classmethod
    def tearDownClass(cls):
        """ Tear down method """
        cls.get_patcher.stop()
