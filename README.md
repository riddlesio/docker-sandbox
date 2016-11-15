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

This container is not intended to be deployed. Instead, all Docker
containers should inherit from the sandbox image. To do so, add the
following line at the top of your Dockerfile:

```
FROM gcr.io/riddles-microservices/sandbox:latest
```

## Contributions

This repository uses the Github branching model with the following
branch specification:

- master
- feature/FeatureName

The master branch is closed for writing, contributions should be
submitted through a pull request from a feature branch.

Each pull request must describe the changes made and why these changes
are necessary (for future reference).
