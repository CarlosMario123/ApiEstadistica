# controllers/email_controller.py
from dotenv import load_dotenv
import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from flask import jsonify

# Cargar las variables de entorno
load_dotenv()
key = os.getenv("SENDGRIDAPI")
email = os.getenv("EMAILGRID")

def send_email(problema,descripcion):
    try:
        to_email = "danielhernandezgomez103@gmail.com"
        subject = "notificacion de avitech"
        
        # Variables del problema
       
        tipo_problema = problema
        descripcion_problema = descripcion

        enlace_sistema = "sin enlace"
        
        # Contenido HTML
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Avitech - Notificación de Problema</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 80%;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                .header {{
                    text-align: center;
                    background-color: #d9534f;
                    color: #fff;
                    padding: 10px 0;
                    border-radius: 8px 8px 0 0;
                }}
                .header h1 {{
                    margin: 0;
                }}
                .content {{
                    padding: 20px;
                }}
                .content h2 {{
                    color: #d9534f;
                }}
                .content p {{
                    line-height: 1.6;
                }}
                .footer {{
                    text-align: center;
                    padding: 10px 0;
                    color: #999;
                }}
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    margin-top: 20px;
                    background-color: #d9534f;
                    color: #fff;
                    text-decoration: none;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Avitech</h1>
                </div>
                <div class="content">
                    <h2>Notificación de Problema Crítico</h2>
                    <p>Estimado Usuario,</p>
                    <p>Se ha detectado un problema crítico en su sistema de gestión de aves. A continuación se detallan los pormenores del problema:</p>
                    <ul>
                       
                        <li><strong>Tipo de Problema:</strong> {tipo_problema}</li>
                        <li><strong>Descripción:</strong> {descripcion_problema}</li>
                    
                    </ul>
                    <p>Este problema requiere su atención inmediata para asegurar el bienestar de las aves y el funcionamiento óptimo del sistema.</p>
                    <p>Por favor, acceda al sistema para tomar las medidas necesarias.</p>
                    <p>Gracias por su atención.</p>
                    <p>Atentamente,</p>
                    <p>El equipo de Avitech</p>
                    <a href="{enlace_sistema}" class="button">Acceder al Sistema</a>
                </div>
                <div class="footer">
                    <p>&copy; 2024 Avitech. Todos los derechos reservados.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        mensaje = Mail(
            from_email=email,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        
        sg = SendGridAPIClient(key)
        respuesta = sg.send(mensaje)
        
        return jsonify({
            "status_code": respuesta.status_code,
            "body": respuesta.body.decode('utf-8'),
            "headers": dict(respuesta.headers)
        }), respuesta.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
