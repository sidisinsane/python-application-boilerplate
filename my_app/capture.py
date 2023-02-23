import subprocess


def capture(command):
    """
    Runs a command in a subprocess and captures its output.

    Args:
        command (str or list): The command to run. Can be a string or a list
            of strings, where each string represents a command and its arguments.

    Returns:
        tuple: A tuple containing three values:
            - stdout (bytes): The standard output of the command.
            - stderr (bytes): The standard error of the command.
            - returncode (int): The return code of the command.

    Raises:
        CalledProcessError: If the command exits with a non-zero status code.
    """
    with subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ) as proc:
        out, err = proc.communicate()
        return out, err, proc.returncode
