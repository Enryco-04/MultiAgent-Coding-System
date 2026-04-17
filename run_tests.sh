#!/bin/bash
# run_tests.sh
# Called by the Python host via:
#   docker exec java_tester /app/run_tests.sh <iteration_dir> <impl_class> <test_class>
#
# Strategy: bash only compiles and runs — it writes raw plain-text output files.
# The Python host reads those files and builds the JSON itself, which is far
# more reliable than trying to escape arbitrary compiler/JVM output in bash.
#
# Files written to /app/workspace/<iteration_dir>/ :
#   compile_ok.txt    — "true" or "false"
#   compile_out.txt   — raw javac stderr (empty on success)
#   junit_out.txt     — raw JUnit ConsoleLauncher output (empty on compile fail)

set -uo pipefail

ITERATION_DIR="$1"
IMPL_CLASS="$2"
TEST_CLASS="$3"

WORK="/app/workspace/${ITERATION_DIR}"
BIN="${WORK}/bin"
JUNIT_JAR="/app/junit.jar"

mkdir -p "${BIN}"

# ── 1. Compile ────────────────────────────────────────────────────────────────
COMPILE_OUT=$(
    javac \
        -cp "${JUNIT_JAR}" \
        -d  "${BIN}" \
        "${WORK}/${IMPL_CLASS}.java" \
        "${WORK}/${TEST_CLASS}.java" 2>&1
) || true

if [ ! -f "${BIN}/${IMPL_CLASS}.class" ]; then
    echo "false"           > "${WORK}/compile_ok.txt"
    echo "${COMPILE_OUT}"  > "${WORK}/compile_out.txt"
    echo ""                > "${WORK}/junit_out.txt"
    echo "[run_tests] Compilation failed"
    exit 0
fi

echo "true" > "${WORK}/compile_ok.txt"
echo ""      > "${WORK}/compile_out.txt"

# ── 2. Run JUnit ──────────────────────────────────────────────────────────────
java \
    -cp "${BIN}:${JUNIT_JAR}" \
    org.junit.platform.console.ConsoleLauncher \
    --select-class "${TEST_CLASS}" \
    --details verbose \
    --disable-banner \
    > "${WORK}/junit_out.txt" 2>&1 || true

echo "[run_tests] done"
