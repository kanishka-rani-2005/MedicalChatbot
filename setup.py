from setuptools import setup, find_packages

# Read the contents of requirements.txt
with open('requirements.txt') as f:
    requirements = [
        line.strip() for line in f
        if line.strip() and not line.startswith('-e') and not line.startswith('#')
    ]

    

setup(
    name='Medical Chatbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    description='Generative ai project',
    author='Kanishka Rani',
    author_email='kanishka22043@gmail.com',
    url='https://github.com/kanishka-rani-2005/MedicalChatbot/tree/main',
    python_requires='>=3.6',
)
