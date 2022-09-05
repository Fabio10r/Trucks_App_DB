FROM postgres:latest
ENV POSTGRES_PASSWORD=0563
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=craftable
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql