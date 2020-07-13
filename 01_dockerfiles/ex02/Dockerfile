FROM ruby:latest

RUN apt update \
	&& apt upgrade -y \
	&& apt install yarn -y \
	&& apt install git -y \
	&& gem install rails \
	&& mkdir -p /opt/tsek

COPY ./app /opt

ONBUILD WORKDIR /opt/app

ONBUILD ADD . /opt/app

ONBUILD EXPOSE 3000

ONBUILD RUN gem install bundler:1.17.2 && bundle install --without production && bundle update --bundler && rails db:migrate && rails db:seed && rails test

# To clone app (This must be done before you build the container):
# ``` sh
#	git clone https://github.com/mhartl/hello_app_original.git app
# ```

# To build first image:
# ``` sh
# 	docker build -t ft-rails:on-build .
# ```

# Dokerfile (from exersise):
# FROM	ft-rails
#
# EXPOSE 3000
#
# CMD ["rails", "s", "-b", "0.0.0.0", "-p", "3000"]

# To generate the second Dockerfile:
#``` sh
# { echo "FROM ft-rails:on-build"; echo "EXPOSE 3000"; echo "CMD [ \"rails\", \"s\", \"-b\", \"0.0.0.0\", \"-p\",\"3000\" ]";} > app/Dockerfile
# ```

# To build second Dockerfile:
# ``` sh
#	docker build -t rails:ex02 ./app
# ```

# To run second Dockerfile:
# ``` sh
#	docker run -rm -p 3000:3000 rails:ex02
# ```
