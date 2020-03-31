import axios from 'axios'
// import QS from 'qs'

export function request(config) {
  const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/app01/api/',
    timeout: 10000,
  });
  instance.interceptors.request.use(config => {
    console.log(config);
    return config
  }, err => {
    console.log(err);
  });
  instance.interceptors.response.use(res => {
    console.log(res);
    return res.data
  }, err => {
    console.log(err);
  });
  return instance(config)
}


// axios.defaults.timeout = 5000; //响应时间
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'; //配置请求头
// axios.defaults.baseURL = 'http://127.0.0.1:8000/app01/api/'; //配置接口地址

// //POST传参序列化(添加请求拦截器)
// axios.interceptors.request.use((config) => {
//   console.log(config);
//   if (config.method === 'post') {
//     config.data = qs.stringify(config.data);
//   }
//   return config;
// }, (error) => {
//   console.log('错误的传参')
//   return Promise.reject(error);
// });

// //返回状态判断(添加响应拦截器)
// axios.interceptors.response.use((res) => {
//   console.log(res);
//   if (!res.data.success) {
//     return Promise.resolve(res);
//   }
//   return res;
// }, (error) => {
//   console.log('网络异常')
//   return Promise.reject(error);
// });

// //返回一个Promise(发送post请求)
// export function fetchPost(url, params) {
//   return new Promise((resolve, reject) => {
//     axios.post(url, params)
//       .then(response => {
//         resolve(response);
//       }, err => {
//         reject(err);
//       })
//       .catch((error) => {
//         reject(error)
//       })
//   })
// }
// ////返回一个Promise(发送get请求)
// export function fetchGet(url, param) {
//   return new Promise((resolve, reject) => {
//     axios.get(url, {
//         params: param
//       })
//       .then(response => {
//         resolve(response)
//       }, err => {
//         reject(err)
//       })
//       .catch((error) => {
//         reject(error)
//       })
//   })
// }
// export default {
//   fetchPost,
//   fetchGet,
// }