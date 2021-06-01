# ShEx Validation API

Microservice for validating RDF against Shape Expressions. This service comes with OpenAPI documentation as well as a ready-to-use Docker container.

## Getting started

After having cloned or in other ways downloaded this repository, build and run your Docker image with the following commands:

```bash
docker build -t yourimage ./
docker run --name yourcontainer -p 80:80 yourimage
```

The API should now accept POST requests at `http://127.0.0.1/validate` and documentation should be served from `http://127.0.0.1/docs`.