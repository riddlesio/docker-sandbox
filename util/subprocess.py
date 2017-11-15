from collections import namedtuple
import subprocess


ExecutionResult = namedtuple('ExecutionResult', ['return_code', 'stdout', 'stderr'])


class SubprocessRunner():
    """
    The SubprocessRunner executes a certain command using the subprocess.run
    method added in Python 3.5.
    """

    def run(self, command: str, timeout=None) -> ExecutionResult:
        """
        Runs the passed command and terminates if the call did not finish
        execution within the timeout value

        Parameters
        ----------
        command : str
            The command to execute
        timeout : Optional[int]
            Amount of time in seconds after which execution should be aborted
        Returns
        -------
        ExecutionResult containing result_code, stderr and stdout
        """

        try:
            process = subprocess.run(
                command,
                timeout=timeout,
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                universal_newlines=True
            )

            return ExecutionResult(
                return_code=process.returncode,
                stderr=process.stderr,
                stdout=process.stdout
            )
        except BaseException as e:
            return ExecutionResult(
                return_code=1,
                stderr=str(e) + '\n',
                stdout='',
            )
