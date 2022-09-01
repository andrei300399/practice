# -*- coding: utf-8 -*-
from django_jenkins.runner import CITestSuiteRunner
from django_selenium.jenkins_runner import JenkinsTestRunner, SeleniumTestRunner
from django.test.testcases import TestCase
from django.test.simple import reorder_suite


class ProjectRunner(JenkinsTestRunner):
    """
    Project test runner
    """

    def __init__(self, **kwargs):
        super(ProjectRunner, self).__init__(**kwargs)
        self.selenium_only = True

    def build_suite(self, test_labels, **kwargs):
        suite = SeleniumTestRunner.build_suite(self, test_labels, **kwargs)
        suite.addTest(CITestSuiteRunner.build_suite(self, test_labels, **kwargs))

        return reorder_suite(suite, (TestCase,))