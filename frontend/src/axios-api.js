import axios from 'axios';

const getAPI = axios.create({
  baseURL: 'https://appinspector.herokuapp.com',
});

export { getAPI };
