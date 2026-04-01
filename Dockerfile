FROM eclipse-temurin:17

WORKDIR /app

RUN apt-get update && apt-get install -y wget unzip

# JUnit 5 standalone runner
RUN wget -q -O /app/junit.jar \
    https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.10.0/junit-platform-console-standalone-1.10.0.jar

# sonar-scanner CLI (runs inside this container to avoid Windows --network host issues)
RUN wget -q -O /tmp/sonar-scanner.zip \
    https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-6.2.1.4610-linux-x64.zip \
    && unzip -q /tmp/sonar-scanner.zip -d /opt \
    && mv /opt/sonar-scanner-6.2.1.4610-linux-x64 /opt/sonar-scanner \
    && rm /tmp/sonar-scanner.zip

ENV PATH="/opt/sonar-scanner/bin:${PATH}"

# run_tests.sh — compile + run JUnit, write plain-text result files
COPY run_tests.sh /app/run_tests.sh
RUN chmod +x /app/run_tests.sh

CMD ["bash"]