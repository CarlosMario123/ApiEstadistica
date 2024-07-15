from functools import wraps
from flask import jsonify, request
import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

# Cargar la clave pública ECDSA desde el archivo
with open('public.pem', 'rb') as f:
    public_key = serialization.load_pem_public_key(
        f.read(),
        backend=default_backend()
    )

def token_required(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1] if auth_header.startswith('Bearer ') else None

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            # Verificar y decodificar el token utilizando la clave pública y el algoritmo ES256
            data = jwt.decode(token, public_key, algorithms=['ES256'])
            print("Token decodificado:", data)
        except ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        # Si el token es válido, continuar con la función original
        return fn(*args, **kwargs)

    return decorated
