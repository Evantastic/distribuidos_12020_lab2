FROM node:alpine AS development

WORKDIR /code

COPY package.json /code
COPY package-lock.json /code
RUN npm ci

COPY . /code

CMD ["npm", "run", "serve"]