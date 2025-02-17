#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    # Create the Connexion app and enable Swagger UI
    app = connexion.App(
        __name__,
        specification_dir='./swagger/',
        options={
            "swagger_ui": True,  # Enable Swagger UI
            "serve_spec": True,  # Serve the OpenAPI spec
            # "swagger_ui_url": "/"  # <- Optionally serve UI at the root ("/")
        }
    )

    # Set the custom JSON encoder, if you need it
    app.json_provider_class = encoder.JSONEncoder

    # Load your OpenAPI/Swagger YAML
    app.add_api('swagger.yaml',
                arguments={'title': 'Simple Inventory API'},
                pythonic_params=True)

    # Run the server
    app.run(port=5000)


if __name__ == '__main__':
    main()