FROM alpine

# Set up OS-level dependencies
RUN apk --no-cache add curl zsh

# Copy the shell script into container
RUN mkdir /app
WORKDIR /app
COPY . /app

# Run shell script that will poke API every N seconds
CMD ["./run_etl.zsh"]