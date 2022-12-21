FROM node:16.15.1

WORKDIR /app


COPY package.json ./
COPY package-lock.json ./


RUN npm install
RUN npm install -g serve

COPY . ./

RUN chown -R node:node /app/node_modules
RUN mv /app/node_modules/.vite/deps_temp /app/node_modules/.vite/deps
EXPOSE 5173
CMD ["npm", "run", "dev"]