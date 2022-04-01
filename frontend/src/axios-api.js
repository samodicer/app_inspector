import axios from 'axios';

const getAPI = axios.create({
  baseURL: 'https://appinspector-api.herokuapp.com',
  //baseURL: 'http://127.0.0.1:8000',
});

export { getAPI };
