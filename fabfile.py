#! *-* coding: utf-8 *-*
"""convert hadoop_ecosystem.ipynb to slide"""

from fabric.api import env, run
from fabric.context_managers import cd

env.hosts = ['localhost']

def convert_1():
    """convert hadoop_ecosystem.ipynb"""
    cmd = """ipython nbconvert hadoop_ecosystem.ipynb --to slides --post serve"""
    with cd('/Users/hqlgree2/Documents/github/notebooks'):
        run('pwd')
        run(cmd)

def convert_1():
    """convert hadoop_ecosystem.ipynb"""
    cmd = """ipython nbconvert hadoop_ecosystem.ipynb --to slides --post serve --template slides_transition.tpl"""
    with cd('/Users/hqlgree2/Documents/github/notebooks'):
        run('pwd')
        run(cmd)
