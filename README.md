# Sandbox Docker Image

This repository contains the sandbox docker image used by all
microservices.

## Usage

This guide assumes the user has the Google Cloud SDK with beta
components and kubectl installed.

### Building the container

To build the container, run following command:
```
bin/build sandbox
```

To build and override the image version tag:
```
bin/build -v 1.0.9-RC1 sandbox
```

To force a build on a dirty working tree:
```
bin/build -f sandbox
```

All flags can be combined.

### Publishing the container

The build script can also be used to publish the container to the
Google Container Registry.

**Important:** make sure the gcloud project id is set to
`riddles-microservices`, you won't be able to push the container
otherwise.

Run the following command to build and publish the container:
```
bin/build -p sandbox
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
