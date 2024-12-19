import sys
from subprocess import call

FAIL_UNDER = 97
COV = ["coverage"]
RUN = ["run", "--source=doit", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "-ra", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "test_execute",
    "test_sqlite_import",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K, "tests"])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
