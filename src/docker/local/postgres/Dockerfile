FROM postgres:15-bullseye

COPY ./docker/local/postgres/maintenance /maintenance

RUN chmod +x /maintenance/*
RUN mv /maintenance/* /usr/local/bin \
  && rmdir /maintenance
