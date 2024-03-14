import hvac
from secret_lib.hsc_vault import HscVaultSecret

# Create a client instance
client = hvac.Client(url='https://vault.trustnet.app:8200')
client.auth.userpass.login(
    username='username',
    password='password'
)

secret = HscVaultSecret(client=client, paths=['secret/data/l0', 'secret/data/l1'])

first_secret = secret.get('first_secret')
