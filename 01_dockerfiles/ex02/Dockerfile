FROM ruby:latest

RUN apt update \
	&& apt upgrade -y \
	&& apt install yarn -y \
	&& apt install git -y \
	&& gem install rails \
	&& mkdir -p /opt/tsek

ONBUILD WORKDIR /opt/app

ONBUILD ADD . /opt/app

ONBUILD EXPOSE 3000

ONBUILD RUN bundle install --witout production \
	&& rails db:migrate \
	&& rails db:seed \
	&& rails test


