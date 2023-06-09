FROM mysql:8.0

COPY ./todo.sql /tmp

CMD [ "mysqld", "--init-file=/tmp/todo.sql" ]