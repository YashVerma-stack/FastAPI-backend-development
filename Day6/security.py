from passlib.context import CryptContext

bcrypt_context = CryptContext(['bcrypt'], deprecated = 'auto')
