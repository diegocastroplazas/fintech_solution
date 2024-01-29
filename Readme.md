# Fintech Solution

This is a Django Rest Framework project for the Fintech Solution.

## Installing Docker Compose

To use Docker Compose for this project, follow these steps to install it:

1. Install Docker Engine: Follow the instructions for your operating system on the [Docker website](https://docs.docker.com/engine/install/).
2. Install Docker Compose: Follow the instructions for your operating system on the [Docker Compose website](https://docs.docker.com/compose/install/).

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/diegocastroplazas/fintech_solution.git`
2. Buid the project with: `make build`.
3. Start the application: `make start`

## Accessing the Documentation

Once the application is running, you can access the API documentation by navigating to the following URL in your web browser:

http://localhost:8000/

## Important

Before you can fully use the application, you need to create a superuser. This can be done by running the following command:


`make superuser`

Use this user credentials for authentication along the docs UI. 

## Makefile

The project includes a Makefile that provides shortcuts for common tasks. Here are some of the available commands:

- `make test`: Runs the project's test suite.
- `make clean`: Cleans up temporary files and directories.

Please refer to the Makefile for a complete list of available commands and their descriptions.
