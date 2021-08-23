#!/usr/bin/env python3

import click
import subprocess
import os
import config
import datetime

# java -jar junit5.jar -cp ../examples/junit-example/target/test-classes/ --scan-classpath
# java -jar junit5.jar -cp ../examples/junit-example/target/test-classes/ -c com.unittest.AppTest

today = [
    str(datetime.datetime.today().year),
    str(datetime.datetime.today().month),
    str(datetime.datetime.today().day),
    str(datetime.datetime.today().hour),
    str(datetime.datetime.today().minute),
    str(datetime.datetime.today().second),
]

today_formatted = "-".join(today)


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
@click.option("-o", "--output", "output", type=click.Path(exists=True))
def test(
    cwd,
    junit_jar_file_path,
    java_package_dir,
    python_dir,
    java_file,
    python_file_path,
    output,
):
    """
    Provide the test case files or directory to run the test cases.
    """

    target = cwd or os.path.abspath(os.getcwd())
    junit_jar_file_path = junit_jar_file_path or config.JUNIT_JAR_FILE_DEFAULT_PATH
    dirpath, dirnames, filenames = next(os.walk(target), (None, None, []))

    if java_package_dir:
        command = [
            "java",
            "-jar",
            junit_jar_file_path,
            "-cp",
            java_package_dir,
            "--scan-classpath",
        ]

        if output:
            result = subprocess.run(command, capture_output=True)
            log = result.stdout.decode("utf-8")
            f = open(os.path.join(output, today_formatted), "w")
            f.write(log)
            f.close()
        else:
            subprocess.run(command)

    if python_dir:
        command = [
            "pytest",
            python_dir,
        ]

        if output:
            result = subprocess.run(command, capture_output=True)
            log = result.stdout.decode("utf-8")
            f = open(os.path.join(output, today_formatted), "w")
            f.write(log)
            f.close()
        else:
            subprocess.run(command)

    if java_file:
        command = [
            "java",
            "-jar",
            junit_jar_file_path,
            "-cp",
            java_file[0],
            "-c",
            java_file[1],
        ]

        if output:
            result = subprocess.run(command, capture_output=True)
            log = result.stdout.decode("utf-8")

            f = open(os.path.join(output, today_formatted), "w")
            f.write(log)
        else:
            subprocess.run(command)
            f.close()

    if python_file_path:
        command = [
            "pytest",
            python_file_path,
        ]

        if output:
            result = subprocess.run(command, capture_output=True)
            log = result.stdout.decode("utf-8")
            f = open(os.path.join(output, today_formatted), "w")
            f.write(log)
            f.close()
        else:
            subprocess.run(command)

    if not (java_package_dir or python_dir or java_file or python_file_path):
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
