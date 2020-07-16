FROM ruby

WORKDIR /opt

EXPOSE 3000

RUN gem install rails bundler
RUN gem install rails
RUN apt update -qq && apt install -y nodejs sqlite3
#RUN apt remove cmdtest
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install yarn
RUN rails new app

WORKDIR /opt/app

RUN rails db:migrate && rails db:seed

ENTRYPOINT [ "/bin/bash" ]
