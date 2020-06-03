FROM ruby:latest

RUN apt update
	&& apt upgrade -y
	&& apt install yarn -y
	&& apt install git -y
	&& gem install rails
	&& mkdir -p /opt/tsek

ONBUILD WORKDIR /opt/tsek

ONBUILD ADD . /opt/tsek

ONBUILD EXPOSE 3000

ONBUILD RUN bundle install --witout production
	&& rails db:migrate
	&& rails db:seed
	&& rails test


