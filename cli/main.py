#!/usr/bin/env python3

import click
import subprocess
import os
import config


# java -jar junit5.jar -cp ../examples/junit-example/target/test-classes/ --scan-classpath
# java -jar junit5.jar -cp ../examples/junit-example/target/test-classes/ -c com.unittest.AppTest


@click.group()
def cli():
    pass


@cli.command()
@click.argument("cwd", required=False, type=click.Path(exists=True))
@click.option(
    "-junit", "--junit-jar", "junit_jar_file_path", type=click.Path(exists=True)
)
@click.option(
    "-jd", "--java-package-dir", "java_package_dir", type=click.Path(exists=True)
)
@click.option("-pd", "--python-dir", "python_dir", type=click.Path(exists=True))
@click.option(
    "-jf",
    "--java-file",
    "java_file",
    nargs=2,
    type=(click.Path(exists=True), click.STRING),
)
@click.option("-pf", "--python-file", "python_file_path", type=click.Path(exists=True))
def test(
    cwd, junit_jar_file_path, java_package_dir, python_dir, java_file, python_file_path
):
    """
    Provide the test case files or directory to run the test cases.
    """

    target = cwd or os.path.abspath(os.getcwd())
    junit_jar_file_path = junit_jar_file_path or config.JUNIT_JAR_FILE_DEFAULT_PATH
    dirpath, dirnames, filenames = next(os.walk(target), (None, None, []))

    if java_package_dir:
        subprocess.run(
            [
                "java",
                "-jar",
                junit_jar_file_path,
                "-cp",
                java_package_dir,
                "--scan-classpath",
            ]
        )
    if python_dir:
        subprocess.run(
            [
                "pytest",
                python_dir,
            ]
        )
    if java_file:
        subprocess.run(
            [
                "java",
                "-jar",
                junit_jar_file_path,
                "-cp",
                java_file[0],
                "-c",
                java_file[1],
            ]
        )
    if python_file_path:
        subprocess.run(
            [
                "pytest",
                python_file_path,
            ]
        )
    else:
        click.echo(
            click.style(
                "ATTENTION! TESTING CAN NOT PROCEED",
                blink=True,
                bold=True,
                bg="bright_magenta",
            )
        )
        click.echo(
            click.style(
                "No option was selected - see --help for more information",
                fg="red",
                bold=True,
            )
        )
        click.echo(
            click.style(
                "You should choose the target test case platform, either JUnit or PyTest or Python Standard Unit Test",
                fg="yellow",
                bold=True,
            )
        )


if __name__ == "__main__":
    cli()
