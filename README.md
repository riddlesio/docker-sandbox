# Sandbox Docker Image

This repository contains the sandbox docker image used by all
microservices.

## Usage

This guide assumes the user has the Google Cloud SDK with beta
components and kubectl, as well as Jarvis installed.

### Building the container

Jarvis is used to build the container. You can build the container
by running the following command:
```
jarvis build image sandbox
```

To force a build on a dirty working tree:
```
jarvis force build image sandbox
```

### Publishing the container

Jarvis can also be used to publish the container to the
Google Container Registry.

Run the following command to publish the container:
```
jarvis publish image sandbox
```

Note that you cannot publish a container which has been built using the
force flag.

### Using the Docker image

This docker image is used by the match-runner. It spins up this image
each time a game needs to run. In the matchrunner configuration (.env
locally or in a deployment on k8s) you need to make sure that the
following variables are properly set:
```
SANDBOX_CONTAINER_NAME=sandbox
SANDBOX_CONTAINER_VERSION=df9eb17
```

The sandbox container version is a docker image tag, which is based on
the commit hash of the commit the image was built for.
Instead of a commit hash you can also use ```latest```, but this is not
recommended to use because when a new image will be pushed, you can no
longer easily see that latest is now the previous version.

## Contributions

This repository uses the Github branching model with the following
branch specification:

- master
- feature/FeatureName

The master branch is closed for writing, contributions should be
submitted through a pull request from a feature branch.

Each pull request must describe the changes made and why these changes
are necessary (for future reference).
