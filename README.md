# Sandbox Docker Images

This repository contains the sandbox images used by the match runner. There is a compiler, as well as a runtime image
for each supported programming language.

## Usage

This guide assumes the user has python3 with access to the Riddles.io pypi server as well as the Google Cloud SDK with
beta components and kubectl installed.

When running the scripts for the first time, ensure all dependencies are installed correctly by running the following 
command:

```
pip install -r requirements/requirements.txt
```

### Building the containers

To build the containers, run following command:

```
bin/sandbox-scripts build
```

### Publishing one or all containers

The script can also be used to publish the container to the Google Container Registry.

Run the following command to build and publish a specific container:

```
bin/sandbox-scripts publish <container_name>
```

In order to publish all containers, run the following command instead:

```
bin/sandbox-scripts publish all
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
