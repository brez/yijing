from setuptools import setup

setup(name='yijing',
            version='0.1',
            description='I Ching predictor',
            url='http://github.com/brez/yijing',
            author='de la brez',
            license='MIT',
            test_suite='nose.collector',
            tests_require=['nose'],
            packages=['yijing'],
            zip_safe=False)
