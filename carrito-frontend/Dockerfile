FROM node:22-alpine3.20

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN npm install 

COPY ./src ./src

COPY ./public ./public

COPY ./index.html ./

COPY ./vite.config.js ./ 

EXPOSE 5173

CMD ["npm","run","dev-host"]