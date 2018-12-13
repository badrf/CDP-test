FROM node:8

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY src/js/package*.json ./

RUN npm install

# Bundle app source
COPY src/js/* ./
COPY src/ejs/* ../ejs/

EXPOSE 8080
CMD [ "npm", "start" ]