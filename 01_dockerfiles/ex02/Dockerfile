# Use the latest Ruby image from Docker Hub as the base image.
FROM ruby:latest
# Set an environment variable named $PORT on your bash terminal to be '3000'.
ENV PORT 3000
# Expose port 3000 of the virtual container to your local machine.
EXPOSE $PORT
# Use a directory called /opt/app/ in which to store the ruby application's files.
RUN mkdir -p /opt/
WORKDIR /opt/
# Install Ruby on Rails app dependencies
RUN gem install rails bundler
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -yf nodejs yarn
# Generate and configure hello_world rails app
RUN rails new app 
WORKDIR /opt/app/
RUN bundle update && bundle install