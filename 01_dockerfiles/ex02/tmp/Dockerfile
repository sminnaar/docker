FROM ruby

#RUN bundle config --global frozen 1

WORKDIR /opt/app

COPY Gemfile .

RUN bundle install

COPY /app/* ./

CMD ["ruby", "./app.rb"]
