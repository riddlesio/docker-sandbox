# Sandbox Docker Images

This repository contains the sandbox images used by the match runner. There is a compiler, as well as a runtime image
for each supported programming language.

## Usage

This guide assumes the user has python3 with access to the Riddles.io pypi server as well as the Google Cloud SDK with
beta components and kubectl installed.

When running the scripts for the first time, ensure all dependencies are installed correctly by running the following
command:

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements/requirements.txt
```

Next time you open your terminal, do not forget to activate your virtual environment by running `source .venv/bin/activate` after changing dir into docker-sandbox.

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

### Running the test suite

The test suite can be invoked through the following command:
```
bin/sandbox-scripts test
```

This runs the test suite in its intirety. Markers can be added if
you want to run only a subset of tests. For instance, running the
tests for the Java compiler can be done as follows:
```
bin/sandbox-scripts test java and compiler
```

Similarly, running tests for both the OCaml and Reason compilers
and runtimes can be done as follows:
```
bin/sandbox-scripts test ocaml or reason
```

**Important**: Running the test suite requires that the sandbox
images have been built and are available on your local machine.

### Adding tests to the test suite

#### Tests for new compiler or runtime implementations

All that's needed to add tests for new implementations is
a simple mutation of the `test/config.py` file.

The config file contains a list of tuples consisting of the
slug of the programming language and the command required
to execute a binary/script.

Adding support for a language, say Java, is as simple as
adding the following to the list:

```
('java', 'java -jar')
```

#### Testing for specific cases

When testing for edge cases, specific language features or implementation
details, extra tests can be added to a sub folder in the `test` folder.
All files prefixed with `test_` and ending in `.py` will be recognised
as valid tests.

Note that these tests should be marked according to the programming
language being tested and whether the test targets the compiler or
the runtime. Furthermore, all added files, folders and tests should
have a unique name.

## Contributions

This repository uses the Github branching model with the following
branch specification:

- master
- feature/FeatureName

The master branch is closed for writing, contributions should be
submitted through a pull request from a feature branch.

Each pull request must describe the changes made and why these changes
are necessary (for future reference) or reference an issue which does
so.
