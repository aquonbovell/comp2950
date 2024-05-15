# from pki_helpers import generate_private_key, generate_public_key
# private_key = generate_private_key("ca-private-key.pem", "secret_password")
# print(private_key)
# generate_public_key(private_key,filename="ca-public-key.pem",country="US",state="Maryland",locality="Baltimore",org="My CA Company",hostname="my-ca.com",)

# from pki_helpers import generate_csr, generate_private_key
# server_private_key = generate_private_key("server-private-key.pem", "serverpassword")
# print(server_private_key)
# generate_csr(server_private_key,filename="server-csr.pem",country="US",state="Maryland",locality="Baltimore",org="My Company",alt_names=["localhost"],hostname="my-site.com",)

from cryptography import x509
from cryptography.hazmat.backends import default_backend
csr_file = open("server-csr.pem", "rb")
csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())
print(csr)
ca_public_key_file = open("ca-public-key.pem", "rb")
ca_public_key = x509.load_pem_x509_certificate(ca_public_key_file.read(), default_backend())
print(ca_public_key)

from getpass import getpass
from cryptography.hazmat.primitives import serialization
ca_private_key_file = open("ca-private-key.pem", "rb")
ca_private_key = serialization.load_pem_private_key(ca_private_key_file.read(),getpass().encode("utf-8"),default_backend(),)
print("Password:")
print(ca_private_key)

from pki_helpers import sign_csr
sign_csr(csr, ca_public_key, ca_private_key, "server-public-key.pem")